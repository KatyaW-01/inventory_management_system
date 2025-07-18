from flask import Flask, jsonify, request
from data import inventory

app = Flask(__name__)

@app.route("/")
def home():
  return jsonify(message='Welcome to the product inventory')

if __name__ == "__main__":
  app.run(debug=True)