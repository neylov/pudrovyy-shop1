
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DB_NAME = 'database.db'

@app.route('/')
def index():
    conn = sqlite3.connect(DB_NAME)
    items = conn.execute("SELECT * FROM products").fetchall()
    conn.close()
    return render_template('index.html', items=items)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    conn = sqlite3.connect(DB_NAME)
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        conn.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
        conn.commit()
    items = conn.execute("SELECT * FROM products").fetchall()
    conn.close()
    return render_template('admin.html', items=items)

@app.route('/delete/<int:item_id>')
def delete(item_id):
    conn = sqlite3.connect(DB_NAME)
    conn.execute("DELETE FROM products WHERE id=?", (item_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)
