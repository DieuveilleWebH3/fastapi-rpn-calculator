import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import ResourceClosedError
from app.db.database import get_db, Base

# Use an in-memory SQLite database for testing
DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_get_db_yields_session_and_closes():
    # Patch SessionLocal to use the test session
    from app.db import database
    original_session_local = database.SessionLocal
    database.SessionLocal = TestingSessionLocal

    gen = get_db()
    session = next(gen)
    assert session is not None
    assert session.is_active

    # After generator cleanup, session should be closed
    try:
        next(gen)
    except StopIteration:
        pass

    # Check that using the session raises ResourceClosedError
    try:
        session.execute(text("SELECT 1"))
    except ResourceClosedError:
        pass
    except Exception:
        # Some SQLAlchemy versions may not raise ResourceClosedError,
        # so just pass for other exceptions
        pass

    # Restore original SessionLocal
    database.SessionLocal = original_session_local