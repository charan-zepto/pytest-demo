from fastapi.testclient import TestClient


def test_store(client: TestClient):
    response = client.post("/storage", json={"key": "customer.1", "value": "Alice"})
    assert response.json() == "success"


def test_fetch(client: TestClient):
    test_store(client)
    response = client.get("/storage", params={"key": "customer.1"})
    assert response.status_code == 200
