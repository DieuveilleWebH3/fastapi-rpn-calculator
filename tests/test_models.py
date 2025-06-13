import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.models.models import Operation, Base

# Use an in-memory SQLite database for testing
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

def test_operation_columns():
    columns = {col.name for col in Operation.__table__.columns}
    assert "id" in columns
    assert "expression" in columns
    assert "result" in columns

def test_create_operation(db: Session):
    op = Operation(expression="2 3 +", result=5.0)
    db.add(op)
    db.commit()
    db.refresh(op)
    assert op.id is not None
    assert op.expression == "2 3 +"  # type: ignore
    assert op.result == 5.0  # type: ignore

def test_read_operation(db: Session):
    op = db.query(Operation).filter_by(expression="2 3 +").first()
    assert op is not None
    assert op.result == 5.0  # type: ignore

def test_update_operation(db: Session):
    op = db.query(Operation).filter_by(expression="2 3 +").first()
    op.result = 10.0  # type: ignore
    db.commit()
    db.refresh(op)
    assert op.result == 10.0  # type: ignore

def test_delete_operation(db: Session):
    op = db.query(Operation).filter_by(expression="2 3 +").first()
    db.delete(op)
    db.commit()
    op = db.query(Operation).filter_by(expression="2 3 +").first()
    assert op is None
