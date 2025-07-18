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