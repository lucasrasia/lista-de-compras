import sqlite3
import sys
from crud import limparterminal, adicionar, apagar, ver_lista
 #conectar com .db
conn=sqlite3.connect("lista.db")   # conecta com o banco(lista.db)
cursor=conn.cursor()    # executa os comando sql

#criar tabela (o IF NOT EXISTS precisa ter, senão ele cria uma nova toda vez)
cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS itens( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
''')
conn.commit()

while True: 
    print("\nLista de compras com python :D")
    print("=============================")
    print(" [1] Adicionar \n [2] Apagar \n [3] Ver lista \n [x] Fechar")
    acao=input("o que deseja fazer? ")
    if acao=="1":
        adicionar(conn, cursor)
        continue
    elif acao=="2":
        apagar(conn, cursor)
        continue
    elif acao=="3":
        ver_lista(conn, cursor)
        continue
    elif acao=="x":
        print("Ok, Tchau!")
        conn.close()
        sys.exit()
    else:
        print("Escolha uma funcão válida")
        limparterminal()
        continue        
