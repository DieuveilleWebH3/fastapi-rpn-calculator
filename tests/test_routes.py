import os
os.environ["DATABASE_URL"] = "sqlite:///./test.db"

from fastapi.testclient import TestClient
from main import app
from app.db.database import Base, get_engine_and_session

engine, _ = get_engine_and_session()
Base.metadata.create_all(bind=engine)

client: TestClient = TestClient(app)

def test_calculate_success():
    response = client.post("/calculate", json={"expression": "2 3 +"})
    assert response.status_code == 200
    data = response.json()
    assert data["expression"] == "2 3 +"
    assert data["result"] == 5.0

def test_calculate_invalid_expression():
    response = client.post("/calculate", json={"expression": "2 +"})
    assert response.status_code == 400
    assert "insufficient operands" in response.json()["detail"].lower()

def test_calculate_invalid_operator():
    response = client.post("/calculate", json={"expression": "2 3 &"})
    assert response.status_code == 400
    assert "invalid" in response.json()["detail"].lower()

def test_calculate_empty_expression():
    response = client.post("/calculate", json={"expression": ""})
    assert response.status_code == 400
    assert "empty" in response.json()["detail"].lower()


def teardown_module(_):
    try:
        engine, _ = get_engine_and_session()
        engine.dispose()  # Close all connections and release the file
        os.remove("test.db")
    except FileNotFoundError:
        pass
    except PermissionError:
        pass