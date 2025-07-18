from flask import Flask, jsonify, request
from data import inventory

app = Flask(__name__)

@app.route("/")
def home():
  return jsonify(message='Welcome to the product inventory')

@app.route("/inventory", methods = ["GET"])
def get_inventory():
  return jsonify(inventory)

@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

if __name__ == "__main__":
  app.run(debug=True)