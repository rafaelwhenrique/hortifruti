import sqlite3
def criar_tabela_produtos():
    banco = sqlite3.connect('hortifruti.db')
    entrada = banco.cursor()
    entrada.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        categoria TEXT NOT NULL,
        preco REAL NOT NULL,
        unidade TEXT NOT NULL,
        lançamento DATE
    )
    ''')
    banco.commit()
    banco.close()

def criar_tabela_clientes():
    banco = sqlite3.connect('hortifruti.db')  
    entrada = banco.cursor()
    entrada.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        contato INTEGER NOT NULL
    )
    ''')
    banco.commit()
    banco.close()

def criar_tabela_fornecedor():
    banco = sqlite3.connect('hortifruti.db')  
    entrada = banco.cursor()
    entrada.execute('''
    CREATE TABLE IF NOT EXISTS fornecedores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        contato INTEGER NOT NULL,
        email TEXT NOT NULL,
        produto TEXT NOT NULL
    )
    ''')
    banco.commit()
    banco.close()

def menu_banco_de_dados():
    print("\n--- Criar  tabela no banco de dados ---")
    print("1. Criar tabela de produtos")
    print("2. Criar tabela de clientes")
    print("3. Criar tabela de fornecedores")

    escolha = input("Selecione uma opção (1-3): ")
    if escolha == '1':
        criar_tabela_produtos()
    elif escolha == '2':
        criar_tabela_clientes()
    elif escolha == '3':
        criar_tabela_fornecedor()