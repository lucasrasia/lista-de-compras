import os

def limparterminal():
    os.system("cls" if os.name == "nt" else "clear")

def adicionar(conn, cursor):
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

def apagar(conn, cursor):
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

def ver_lista(conn, cursor):
    limparterminal()
    cursor.execute("SELECT*FROM itens")
    todos_itens=cursor.fetchall()  #fetchall pega todos os itens
    if len(todos_itens)==0:
        print("Desculpe, não há itens na lista")
        return
    print("\nSua lista:")
    n=1
    for i in todos_itens:
        print(n, i[1]) #i[0]=id i[1]=nome do item
        n+=1