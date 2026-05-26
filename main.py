import sys
import os
import sqlite3

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

#função limpar terminal
def limparterminal():
    os.system("cls" if os.name == "nt" else "clear")

while True: 
    print("\nLista de compras com python :D")
    print("=============================")
    print(" [1] Adicionar \n [2] Apagar \n [3] Ver lista \n [x] Fechar")
    acao=input("o que deseja fazer? ")
    if acao=="1":
        limparterminal()
        print("[x]\nOk! Vamos adicionar itens")
        while True:
            item=input("Item: ")
            if item=="x":
                break
            cursor.execute('''
                INSERT INTO itens(nome)
                VALUES (?)
                ''', (item,))
            conn.commit()
        limparterminal()
        continue
    elif acao=="2":
        limparterminal()
        print("[x]")
        while True:
            item=input("Digite o item que deseja apagar: ")
            if item=="x":
                break

            cursor.execute('''
                SELECT*FROM itens
                WHERE nome=?  
                ''', (item,))  #se item=arroz -> WHERE nome=arroz
            item_delet=cursor.fetchone() # vê se tem algum item arroz se não tiver retorna none      fetchone significa pegue o resultado encontrado

            if item_delet:
                cursor.execute('''
                DELETE FROM itens
                where id=?
                ''', (item_delet[0],)) # id -> existe[0]
                conn.commit()
                print(f"{item} foi removido\n")
                continue
            else:
                print(f"Desculpe, {item} não está na lista, digite novamente\n")
                continue
        limparterminal()
        continue
    elif acao=="3":
        limparterminal()
        cursor.execute("SELECT*FROM itens")
        todos_itens=cursor.fetchall()  #fetchall pega todos os itens
        if len(todos_itens)==0:
            print("Desculpe, não há itens na lista")
            continue
        print("\nSua lista:")
        n=1
        for i in todos_itens:
            print(n, i[1]) #i[0]=id i[1]=nome do item
            n+=1
        continue
    elif acao=="x":
        print("Ok, Tchau!")
        conn.close()
        sys.exit()
    else:
        print("Escolha uma funcão válida")
        limparterminal()
        continue        
