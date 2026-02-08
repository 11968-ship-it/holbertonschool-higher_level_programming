#!/usr/bin/env python3
import sqlite3

def read_products_sql():
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row  # allows dictionary-like access
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
