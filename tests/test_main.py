from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200

def test_add_route():
    response = client.post("/add", json={"a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 8.0}

def test_divide_route():
    response = client.post("/divide", json={"a": 10, "b": 2})
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}

def test_divide_by_zero_route():
    response = client.post("/divide", json={"a": 10, "b": 0})
    assert response.status_code == 400
    assert "Cannot divide by zero!" in response.json()["detail"]

def test_validation_error():
    response = client.post("/add", json={"a": "string", "b": 3})
    assert response.status_code == 400 # Fails Pydantic validation