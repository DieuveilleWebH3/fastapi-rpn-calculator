import os
os.environ["DATABASE_URL"] = "sqlite:///./test.db"

from fastapi.testclient import TestClient
from main import app
from app.db.database import Base, get_engine_and_session

from typing import Any

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

def test_export_route():
    # Ensure there is at least one operation to export
    client.post("/calculate", json={"expression": "2 3 +"})
    response = client.get("/export")
    assert response.status_code == 200
    assert 'attachment; filename="operations.csv"' in response.headers.get("content-disposition", "")
    content = response.content.decode()
    assert "ID,Expression,Result" in content
    assert "2 3 +" in content

def test_list_operations_route():
    # Add some operations
    client.post("/calculate", json={"expression": "4 5 +"})
    client.post("/calculate", json={"expression": "6 7 +"})

    for _ in range(5):
        client.post("/calculate", json={"expression": "7 8 +"})

    response = client.get("/operations?skip=0&limit=5")
    assert response.status_code == 200
    assert len(response.json()) == 5  # Ensure we get exactly 5 results

    data: list[dict[str, Any]] = response.json()
    assert isinstance(data, list)
    assert any(op["expression"] == "2 3 +" for op in data)
    assert any(op["expression"] == "4 5 +" for op in data)
    assert any(op["expression"] == "6 7 +" for op in data)
    assert any(op["expression"] == "7 8 +" for op in data)


def teardown_module(_):
    try:
        engine, _ = get_engine_and_session()
        engine.dispose()  # Close all connections and release the file
        os.remove("test.db")
    except FileNotFoundError:
        pass
    except PermissionError:
        pass