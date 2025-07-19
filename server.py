from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
from data import inventory

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
  return jsonify(message='Welcome to the product inventory')

@app.route("/inventory", methods = ["GET"])
def get_inventory():
  return jsonify(inventory)

@app.route("/inventory/<int:product_id>", methods=["GET"])
def get_product(product_id):
  item = next((product for product in inventory if product["id"] == product_id),None)
  if item:
    return jsonify(item), 200
  return jsonify(message="Product not found"), 404

@app.route("/inventory", methods = ["POST"])
def add_inventory():
  data = request.get_json()
  new_id = max((item["id"] for item in inventory), default=0) + 1
  if data and "product" in data and "price" in data and "stock" in data:
    new_product = {"id": new_id, "product": data["product"], "price": data["price"], "stock": data["stock"] }
    inventory.append(new_product)
    return jsonify(new_product), 201
  return jsonify({"Error":"form cannot be blank"}), 400 

@app.route("/inventory/<int:product_id>", methods=["PATCH"])
def update_product(product_id):
  data = request.get_json()
  item = next((product for product in inventory if product["id"] == product_id), None)
  if not item:
    return jsonify(message="Product not found"), 404
  
  if "product" in data:
    item["product"] = data["product"]
  if "price" in data:
    item["price"] = data["price"]
  if "stock" in data:
    item["stock"] = data["stock"]

  return jsonify(item)

@app.route("/inventory/<int:product_id>", methods=["DELETE"])
def delete_item(product_id):
  global inventory
  item = next((product for product in inventory if product["id"] == product_id), None)
  if not item:
    return jsonify({"message": "Product not found"}), 404
  inventory[:] = [product for product in inventory if product["id"] != product_id]
  return jsonify({"message": "Product deleted"}), 200

# @app.route("/https://world.openfoodfacts.net/api/v2/product/<int:product_barcode>.json", methods=["GET"])
# def get_product_info(product_barcode):
#   data = request.json()
#   return jsonify(data._keywords)

@app.route("/<int:barcode>", methods = ["GET"])
def open_food_api(barcode):
  url = f"https://world.openfoodfacts.org/api/v2/product/{barcode}"
  response = requests.get(url)
  if response.status_code == 200:
    data = response.json()
    product = data.get("product")
    ingredients = product.get("ingredients_text")
    return jsonify({"ingredients": ingredients})
  else:
    return jsonify({"error": "Product not found"}), 404


@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'DELETE'
    return response

if __name__ == "__main__":
  app.run(debug=True)