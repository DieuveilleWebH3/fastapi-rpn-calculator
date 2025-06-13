# load_fixtures.py
import json
from sqlalchemy.orm import Session
from app.db.database import get_engine_and_session
from app.models.models import Operation

def load_seed_data(json_path: str):
    _engine, SessionLocal = get_engine_and_session()
    session: Session = SessionLocal()
    with open(json_path, "r") as f:
        data = json.load(f)
        for item in data:
            op = Operation(**item)
            session.merge(op)  # merge avoids duplicate PK errors
        session.commit()
    session.close()
    print("Seed data loaded.")

if __name__ == "__main__":
    load_seed_data("app/fixtures/seed.json")
