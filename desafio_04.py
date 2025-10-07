from desafio_03.main import criar_elementos, criar_tabela, conectar, find_all

conn = conectar("loja")
criar_tabela(
    table_name="produtos",
    fields="id INTEGER PRIMARY KEY, nome TEXT, preco float",
    conn=conn
)
criar_elementos(
    table_name="produtos",
    fields="(nome, preco)",
    values=[("macarrão", 7.5),("arroz", 5.15),("feijão", 12)],
    conn=conn
)
find_all("produtos", conn)