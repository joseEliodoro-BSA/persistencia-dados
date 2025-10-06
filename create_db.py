import sqlite3

# Cria e realiza uma conexão com o banco
conn = sqlite3.connect("escola.db")

# através desse cursor podemos inserir comandos sql no banco
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS estudantes(
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS disciplinas(
        id INTEGER PRIMARY KEY,
        nome TEXT,
        id_estudante INTEGER,
        FOREIGN KEY (id_estudante) REFERENCES estudantes(id)
    )
""")

# Salvando alterações no banco
conn.commit()

# Encerrando conexão com o banco
conn.close()