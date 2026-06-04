# 🛒 Lista de Compras

Aplicação de lista de compras via terminal, desenvolvida em Python com persistência em SQLite.

## Funcionalidades

- Adicionar itens à lista
- Apagar itens
- Visualizar a lista

## Tecnologias

- Python 3
- SQLite3

## Estrutura

lista-de-compras/
├── main.py     # Ponto de entrada e menu interativo
├── crud.py     # Operações com o banco de dados
├── .gitignore
└── README.md


## Como usar

```bash
git clone https://github.com/lucasrasia/lista-de-compras.git
cd lista-de-compras
python main.py

O banco de dados lista.db é criado automaticamente na primeira execução.
