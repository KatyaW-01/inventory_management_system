import sys
import os
import json
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from server import app
#from server.py import the app object (app = Flask(__name__))

@pytest.fixture
def client():
  return app.test_client()

def test_homepage_returns_welcome_message(client):
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, dict)
    assert "message" in data
    assert "welcome to the product inventory" in data["message"].lower()

def test_get_inventory_returns_inventory_list(client):
  response = client.get("/inventory")
  assert response.status_code == 200
  data = response.get_json()
  assert isinstance(data, list)
  assert all("id" in event and "product" in event and "price" in event and "stock" in event for event in data)

def test_post_inventory_add_new_item(client):
  payload = {"product": "new test product", "price": 10.99, "stock": 1}
  response = client.post("/inventory", data = json.dumps(payload), content_type="application/json")
  assert response.status_code == 201
  data = response.get_json()
  assert isinstance(data, dict)
  assert data["product"] == payload["product"]
  assert data["price"] == payload["price"]
  assert data["stock"] == payload["stock"]

def test_post_inventory_missing_data_returns_error(client):
    response = client.post("/inventory", data=json.dumps({}), content_type="application/json")
    assert response.status_code == 400

def test_patch_inventory(client):
  client.post("/inventory", json={"product": "Old Product", "price": 10.00, "stock": 2})
  response = client.patch("/inventory/1", json={"product": "Updated product"})
  assert response.status_code == 200
  assert response.get_json()["product"] == "Updated product"

def test_delete_inventory_item(client):
  client.post("/inventory", json={"product": "product to be deleted", "price": 10.00, "stock": 1})
  response = client.delete("/inventory/1")
  assert response.status_code == 204
  get_response = client.get("/inventory/1")
  assert get_response.status_code == 404
