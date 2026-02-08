#!/usr/bin/env python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# ---------- JSON ----------
def read_products_json():
    with open('products.json', 'r') as file:
        return json.load(file)

# ---------- CSV ----------
def read_products_csv():
    products = []
    with open('products.csv', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products

# ---------- SQLite ----------
def read_products_sql():
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row  # dictionary-like access
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        products = []
        for row in rows:
            products.append({
                "id": row["id"],
                "name": row["name"],
                "category": row["category"],
                "price": row["price"]
            })
        conn.close()
        return products
    except Exception as e:
        print("Database error:", e)
        return None

# ---------- Flask Route ----------
@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    products = []
    error = None

    # Determine data source
    if source == 'json':
        products = read_products_json()
    elif source == 'csv':
        products = read_products_csv()
    elif source == 'sql':
        products = read_products_sql()
        if products is None:
            error = "Database error"
            return render_template('product_display.html', products=None, error=error)
    else:
        error = "Wrong source"
        return render_template('product_display.html', products=None, error=error)

    # Filter by ID if provided
    if product_id:
        try:
            product_id = int(product_id)
            products = [p for p in products if p["id"] == product_id]
            if not products:
                error = "Product not found"
        except ValueError:
            error = "Product not found"

    return render_template('product_display.html', products=products, error=error)

# ---------- Run Flask ----------
if __name__ == '__main__':
    app.run(debug=True, port=5000)
