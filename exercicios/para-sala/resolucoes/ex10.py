import csv
import sqlite3

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM clientes")
dados = cursor.fetchall()

with open('exportados_clientes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['id', 'nome', 'email'])
    escritor.writerows(dados)

cursor.close()
conn.close()