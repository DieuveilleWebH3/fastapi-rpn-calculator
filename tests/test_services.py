import os
import pytest
from fastapi import BackgroundTasks
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from unittest.mock import patch
from app.models.models import Base, Operation
from app.services.services import compute_and_save, export_csv, get_operations_paginated

DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def db():
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)

def test_compute_and_save(db: Session):
    result = compute_and_save("2 3 +", db)
    assert result["expression"] == "2 3 +"
    assert result["result"] == 5.0
    op = db.query(Operation).filter_by(expression="2 3 +").first()
    assert op is not None
    assert op.result == 5.0  # type: ignore

def test_get_operations_paginated(db: Session):
    # Add more operations
    compute_and_save("4 5 +", db)
    compute_and_save("6 7 +", db)
    ops = get_operations_paginated(0, 2, db)
    assert len(ops) == 2
    assert isinstance(ops[0], Operation)

def test_export_csv(db: Session):
    background_tasks = BackgroundTasks()
    with patch.object(background_tasks, "add_task", lambda *args, **kwargs: None):  # type: ignore
        response = export_csv(db, background_tasks)
        assert response.status_code == 200
        assert response.filename == "operations.csv"
        assert os.path.exists(response.path)
        # Check CSV content
        with open(response.path, "r") as f:
            lines = f.readlines()
            assert lines[0].strip() == "ID,Expression,Result"
            assert any("2 3 +" in line for line in lines)
        os.remove(response.path)
