from fastapi.testclient import TestClient
from restapiprac.main import app

client = TestClient(app)

def test_get_item():
    response = client.get("/item/3")
    assert response.status_code == 200
    assert response.json() == {"id": 3, "category": "Earth", "size": 150}

def test_add_item():
    payload = {"id": 7, "category": "Space", "size": 1500}
    response = client.post("/item", json=payload)
    assert response.status_code == 201
    assert response.json() == {"id": 7, "category": "Space", "size": 1500}

def test_patched():
    response = client.patch("/item/1", json={"category":"ET"})
    assert response.status_code == 200

    data = response.json()
    assert data["category"] == "ET"
    assert data["id"] == 1
    assert data["size"] == 250

def test_delete():
    response = client.delete("/item/1")
    assert response.status_code == 204
    res = client.get("item/1")
    assert res.status_code == 404