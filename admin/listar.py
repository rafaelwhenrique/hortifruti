import sqlite3
import os

def limpar_tela():
    """Limpa a tela do terminal, compatível com Windows e Unix."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def listar_clientes():
    caminho_banco = os.path.join(os.path.dirname(__file__), '..', 'hortifruti.db')
    conexao = sqlite3.connect(caminho_banco)
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    
    if clientes:
        limpar_tela()
        print("Lista de clientes cadastrados:")
        for cliente in clientes:
            id_cliente, nome, contato = cliente
            print(f"ID: {id_cliente}, Nome: {nome}, Contato: {contato}")
    else:
        print("Não há clientes cadastrados.")
    
    conexao.close()

def listar_fornecedor():
    caminho_banco = os.path.join(os.path.dirname(__file__), '..', 'hortifruti.db')
    conexao = sqlite3.connect(caminho_banco)
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM fornecedores")
    fornecedores = cursor.fetchall()
    limpar_tela()
    if fornecedores:
        print("Lista de fornecedor cadastrados:")
        for fornecedor in fornecedores:
            id_fornecedor, nome, contato, email, produto = fornecedor
            print(f"ID: {id_fornecedor}, Nome: {nome}, Contato: {contato}, email: R${email}, produto fornecido: {produto}")
    else:
        print("Não há fornecedores cadastrados.")
    
    conexao.close()

def listar_produtos():
    caminho_banco = os.path.join(os.path.dirname(__file__), '..', 'hortifruti.db')
    conexao = sqlite3.connect(caminho_banco)
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    limpar_tela()
    if produtos:
        print("Lista de produtos cadastrados:")
        for produto in produtos:
            id_produto, nome, categoria, preco, unidade, lançamento = produto
            print(f"ID: {id_produto}, Nome: {nome}, Categoria: {categoria}, Preço: R${preco:.2f}, Unidade: {unidade}, Lançamento: {lançamento}")
    else:
        print("Não há produtos cadastrados.")
    
    conexao.close()

def menu_listar():
    print("\n--- Listar  tabela no banco de dados ---")
    print("1. Listar tabela de produtos")
    print("2. Listar tabela de clientes")
    print("3. Listar tabela de fornecedores")

    escolha = input("Selecione uma opção (1-4): ")
    if escolha == "1":
        listar_produtos()
    elif escolha == "2":
        listar_clientes()
    elif escolha == "3":
        listar_fornecedor()