import sqlite3

conn = sqlite3.connect("escola.db")
cursor = conn.cursor()

# cursor.execute(
#     """
#     INSERT INTO estudantes(nome, idade) VALUES (?, ?)
#     """,  ("Anna", 19)
# )

cursor.execute(
    """
    INSERT INTO disciplinas(nome, id_estudante) VALUES (?, ?)
    """,  ("discreta", 1)
)

conn.commit()
conn.close()