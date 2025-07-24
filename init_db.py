
import sqlite3
conn = sqlite3.connect('database.db')
conn.execute('CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, price INTEGER)')
conn.commit()
conn.close()
