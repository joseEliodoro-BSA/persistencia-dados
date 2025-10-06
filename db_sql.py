import sqlite3

conn = sqlite3.connect("escola.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS estudantes(
    id INTERGER AUTO_INCREMENT PRIMARY KEY,
    nome TEXT,
    idade INTEGER
)
""")

cursor.execute("INSERT INTO estudantes(nome, idade) VALUES(?, ?)", ("jose", 22))

conn.commit()

cursor.execute("SELECT * FROM estudantes")
print(cursor.fetchall())

conn.close()