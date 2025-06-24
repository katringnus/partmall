from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products').fetchall()
    conn.close()
    return render_template('home.html', products=products)

@app.route('/product/<slug>')
def product_detail(slug):
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products WHERE slug = ?', (slug,)).fetchone()
    conn.close()
    if product is None:
        return "Product not found", 404
    return render_template('product.html', product=product)