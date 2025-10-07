import requests
import sqlite3

def conectar(name_banco: str):
    return sqlite3.connect(f"{name_banco}.db")

def criar_tabela(table_name: str, fields: str, conn):
    #conn = conectar()
    cursor = conn.cursor()

    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name}(
            {fields}
        )
    """)

    conn.commit()


def criar_elemento(table_name: str, fields:str, values: tuple, conn):
    """ Cria um registro de estudante na tabela table_name """
    #conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        f"""
            INSERT INTO {table_name}{fields} VALUES (?, ?)
        """, values
    )

    conn.commit()

def find_all(table_name: str, conn):
    """ Lista todos os elementos cadastrados na tabela table_name """
    # conn = conectar()
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {table_name}")
    elements = cursor.fetchall()

    for element in elements:
        print(element)


if __name__ == "__main__":
    conn = conectar("desafio_03/hotelplus")
    criar_tabela("usuarios", " id INTEGER PRIMARY KEY, nome TEXT, email TEXT ", conn)
    response = requests.get("https://fakerapi.it/api/v1/users?_quantity=1000")
    if(response.status_code==200):
        for pessoa in response.json()["data"]:
            criar_elemento(
                table_name="usuarios",
                fields="(nome, email)",
                values=(f"{pessoa['firstname']} {pessoa['lastname']}", pessoa["email"]),
                conn=conn
                )
    find_all("usuarios", conn)