import sqlite3
import csv

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

cursor.execute("""
   CREATE TABLE IF NOT EXISTS clientes (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       nome TEXT NOT NULL,
       email TEXT NOT NULL
   )
   """)

with open('../clientes.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    next(leitor)
    
    for item in leitor:
        _, nome, email = item
        cursor.execute("""
            INSERT INTO clientes (nome, email)
            VALUES (?, ?)
        """, (nome, email))
    
conn.commit()
cursor.close()
conn.close()
    