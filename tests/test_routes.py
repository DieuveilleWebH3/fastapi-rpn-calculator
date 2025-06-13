import os
import tempfile
import pytest
from fastapi.testclient import TestClient

from typing import Any


@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp(suffix=".db")
    url = f"sqlite:///{db_path}"
    os.environ["DATABASE_URL"] = url

    # Import app AFTER setting env var
    from main import create_app
    from app.db.database import get_engine_and_session, set_session_local, reset_engine_and_session

    # --- Force engine/session reset ---
    reset_engine_and_session()
    # Recreate tables for each test
    app = create_app()
    engine, SessionLocal = get_engine_and_session()
    # Base.metadata.create_all(bind=engine)
    set_session_local(SessionLocal)

    with TestClient(app) as c:
        yield c

    engine.dispose()
    os.close(db_fd)
    os.remove(db_path)

def test_calculate_success(client: TestClient):
    response = client.post("/calculate", json={"expression": "2 3 +"})
    assert response.status_code == 200
    data = response.json()
    assert data["expression"] == "2 3 +"
    assert data["result"] == 5.0

def test_calculate_invalid_expression(client: TestClient):
    response = client.post("/calculate", json={"expression": "2 +"})
    assert response.status_code == 400
    assert "insufficient operands" in response.json()["detail"].lower()

def test_calculate_invalid_operator(client: TestClient):
    response = client.post("/calculate", json={"expression": "2 3 &"})
    assert response.status_code == 400
    assert "invalid" in response.json()["detail"].lower()

def test_calculate_empty_expression(client: TestClient):
    response = client.post("/calculate", json={"expression": ""})
    assert response.status_code == 400
    assert "empty" in response.json()["detail"].lower()

def test_export_route(client: TestClient):
    # Ensure there is at least one operation to export
    client.post("/calculate", json={"expression": "2 3 +"})
    response = client.get("/export")
    assert response.status_code == 200
    assert 'attachment; filename="operations.csv"' in response.headers.get("content-disposition", "")
    content = response.content.decode()
    assert "ID,Expression,Result" in content
    assert "2 3 +" in content

def test_list_operations_route(client: TestClient):
    # Add some operations
    client.post("/calculate", json={"expression": "9 9 +"})
    client.post("/calculate", json={"expression": "4 5 +"})
    client.post("/calculate", json={"expression": "6 7 +"})

    for _ in range(5):
        client.post("/calculate", json={"expression": "7 8 +"})

    response = client.get("/operations?skip=0&limit=5")
    assert response.status_code == 200

    assert len(response.json()) == 5  # Ensure we get exactly 5 results

    data: list[dict[str, Any]] = response.json()
    assert isinstance(data, list)
    assert any(op["expression"] == "9 9 +" for op in data)
    assert any(op["expression"] == "4 5 +" for op in data)
    assert any(op["expression"] == "6 7 +" for op in data)
    assert any(op["expression"] == "7 8 +" for op in data)
