import sqlite3

conn = sqlite3.connect("escola.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM estudantes")
estudantes = cursor.fetchall()

print(estudantes)

conn.close()