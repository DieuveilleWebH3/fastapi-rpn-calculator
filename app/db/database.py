import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from dotenv import load_dotenv

load_dotenv()
Base = declarative_base()

_engine = None
_SessionLocal = None

def get_engine_and_session():
    global _engine, _SessionLocal
    
    if _engine is None or _SessionLocal is None:
        DATABASE_URL = os.getenv("DATABASE_URL")
        if not DATABASE_URL:
            raise RuntimeError("The DATABASE_URL environment variable is not set. Please configure it before running the application.")

        _engine = create_engine(DATABASE_URL)
        _SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=_engine)

    return _engine, _SessionLocal

def get_db():
    _engine, SessionLocal = get_engine_and_session()
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def set_session_local(session_local: sessionmaker[Session]) -> None:
    global _SessionLocal
    _SessionLocal = session_local
