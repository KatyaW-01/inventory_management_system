from flask import Flask, jsonify, request
from data import inventory

app = Flask(__name__)

@app.route("/")
def home():
  return jsonify(message='Welcome to the product inventory')

@app.route("/inventory", methods = ["GET"])
def get_inventory():
  return jsonify(inventory)

@app.route("/events", methods = ["POST"])
def add_inventory():
  data = request.get_json()
  new_id = max((item["id"] for item in inventory), default=0) + 1
  if data and "product" in data and "price" in data and "stock" in data:
    new_event = {"id": new_id, "product": data["product"], data["price"], data["stock"] }
    inventory.append(new_event)
    return jsonify(new_event), 201
  return jsonify({"Error":"form cannot be blank"}), 400 

@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

if __name__ == "__main__":
  app.run(debug=True)