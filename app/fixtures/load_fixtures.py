# load_fixtures.py
import json
import logging
from sqlalchemy.orm import Session
from app.db.database import get_engine_and_session
from app.models.models import Operation

logging.basicConfig(level=logging.INFO)

def load_seed_data(json_path: str):
    _engine, SessionLocal = get_engine_and_session()
    session: Session = SessionLocal()

    try:
        with open(json_path, "r") as f:
            data = json.load(f)
            for item in data:
                op = Operation(**item)
                session.merge(op)  # merge avoids duplicate PK errors
            session.commit()
    except FileNotFoundError:
        logging.error(f"File not found: {json_path}")
        logging.exception("An error occurred while loading seed data.")
    except PermissionError:
        logging.error(f"Permission denied when accessing the file '{json_path}'.")
    except json.JSONDecodeError as e:
        logging.error(f"Failed to parse JSON from the file '{json_path}': {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    finally:
        session.close()
        logging.info("Seed data loaded.")

if __name__ == "__main__":
    load_seed_data("app/fixtures/seed.json")
