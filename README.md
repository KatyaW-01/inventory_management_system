# Inventory Management Application

A lightweight inventory management tool built with a **Flask** backend and a **JavaScript** frontend. This app allows users to view, add, update, and delete inventory items, as well as fetch additional product information using the **OpenFoodFacts** API by entering a barcode.

---

## Features

- View all inventory items
- Add new products to the inventory
- Delete products from the inventory
- Update product information (name, price, stock)
- Lookup ingredients via barcode using OpenFoodFacts API

---

## Technologies Used

### Backend:
- Python 3
- Flask
- Flask-CORS
- OpenFoodFacts API

### Frontend:
- Vanilla JavaScript
- HTML
- CSS 

## File Structure
```
.
├── client/
│   ├── index.html
│   ├── styles.css
│   └── script.js
├── server.py
├── tests/
│   └── test_app.py
|__requirements.txt
|
├── README.md
```

## API Endpoints

| Method | Endpoint                    | Description                            |
|--------|-----------------------------|----------------------------------------|
| GET    | `/`                         | Welcome message                        |
| GET    | `/inventory`               | Get all products                       |
| GET    | `/inventory/<product_id>`  | Get a specific product by ID           |
| POST   | `/inventory`               | Add a new product                      |
| PATCH  | `/inventory/<product_id>`  | Update an existing product             |
| DELETE | `/inventory/<product_id>`  | Delete a product                       |
| GET    | `/<barcode>`               | Fetch product info from OpenFoodFacts  |

## Running the App 
1. clone the repository
2. set up and run the backend
    ```bash
    pip install -f requirements.txt
    python server.py
    ```
3. Open the application in your browser by opening the html document ('open index.html' on MacOS)

## Example Barcodes for API fetch
* Pesto: 8076809513753
* Iceberg Lettuce: 0033383650203
* Spaghetti: 6111251460469
* Grape tomatoes: 0033383655857
* Plums: 03266168