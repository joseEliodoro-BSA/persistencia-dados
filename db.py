import sqlite3

def conectar():
    return sqlite3.connect("escola.db")

def criar_tabela_estudantes():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estudantes(
            id INTEGER PRIMARY KEY,
            nome TEXT,
            idade INTEGER
        )
    """)

    conn.commit()
    conn.close()

def criar_tabela_matricula():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS matricula(
            id INTEGER PRIMARY KEY,
            nome TEXT,
            id_estudante INTEGER,
            FOREIGN KEY (id_estudante) REFERENCES estudantes(id)
        )
    """)

    conn.commit()
    conn.close()

def criar_estudante(nome, idade):
    """ Cria um registro de estudante na tabela estudantes """
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
            INSERT INTO estudantes(nome, idade) VALUES (?, ?)
        """, (nome, idade)
    )

    conn.commit()
    conn.close()

def listar_estudante():
    """ Lista todos os estudantes cadastrados na tabela estudantes """
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM estudantes")
    estudantes = cursor.fetchall()

    for estudante in estudantes:
        print(estudante)

    conn.close()

def criar_matricula(id_estudante, nome):
    """ Cria um registro de estudante na tabela matricula """
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
            INSERT INTO matricula(id_estudante, nome) VALUES (?, ?)
        """, (id_estudante, nome)
    )

    conn.commit()
    conn.close()

def listar_matricula():
    """ Lista todos os estudantes cadastrados na tabela estudantes """
    conn = conectar()
    cursor = conn.cursor()

    #cursor.execute("SELECT * FROM matricula")
    cursor.execute(
        """
            SELECT m.id, e.nome, m.nome 
            FROM matricula m
            JOIN estudantes e ON m.id_estudante = e.id
        """
    )
    estudantes = cursor.fetchall()

    for estudante in estudantes:
        print(estudante)

    conn.close()