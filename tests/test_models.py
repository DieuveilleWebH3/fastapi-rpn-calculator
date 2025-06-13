import os
import tempfile
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.models.models import Operation, Base


@pytest.fixture()
def db():
    db_fd, db_path = tempfile.mkstemp(suffix=".db")
    url = f"sqlite:///{db_path}"
    engine = create_engine(url)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)
    engine.dispose()
    os.close(db_fd)
    os.remove(db_path)

def _create_test_operation(db: Session, expression: str, result: float) -> Operation:
    op = Operation(expression=expression, result=result)
    db.add(op)
    db.commit()
    db.refresh(op)
    return op
    

def test_operation_columns():
    columns = {col.name for col in Operation.__table__.columns}
    assert "id" in columns
    assert "expression" in columns
    assert "result" in columns

def test_create_operation(db: Session):
    op = _create_test_operation(db, "2 3 +", 5.0)
    assert op.id is not None
    assert op.expression == "2 3 +"  # type: ignore
    assert op.result == 5.0  # type: ignore

def test_read_operation(db: Session):
    _ = _create_test_operation(db, "2 3 +", 5.0)
    op = db.query(Operation).filter_by(expression="2 3 +").first()
    assert op is not None
    assert op.result == 5.0  # type: ignore

def test_update_operation(db: Session):
    _ = _create_test_operation(db, "2 3 +", 5.0)
    op = db.query(Operation).filter_by(expression="2 3 +").first()
    op.result = 10.0  # type: ignore
    db.commit()
    db.refresh(op)
    assert op.result == 10.0  # type: ignore

def test_delete_operation(db: Session):
    _ = _create_test_operation(db, "2 3 +", 5.0)
    op = db.query(Operation).filter_by(expression="2 3 +").first()
    db.delete(op)
    db.commit()
    op = db.query(Operation).filter_by(expression="2 3 +").first()
    assert op is None
