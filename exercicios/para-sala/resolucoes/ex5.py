import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

estudantes = [
    (1,),
    (2,),
]

cursor.execute("DELETE FROM estudantes WHERE id = ?", estudantes)

conn.commit()
cursor.close()
conn.close()