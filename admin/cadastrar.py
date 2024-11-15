import sqlite3
import os

def limpar_tela():
    """
    Limpa a tela do terminal.

    Essa função verifica o sistema operacional (Windows ou Unix)
    e executa o comando adequado para limpar a tela do terminal.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def cadastrar_produto():
    banco = sqlite3.connect('hortifruti.db')
    entrada = banco.cursor()
    limpar_tela()
    nome = input("Digite o nome do produto: ")
    categoria = input("Digite a categoria do produto (frutas, verduras, folhagens, etc.): ")
    preco = float(input("Digite o preço do produto: "))
    unidade = input("Digite a unidade do produto (kg ou un): ")
    lançamento_do_produto = input("Digite o dia do lançamento do produto (AAAA-MM-DD): ")


    entrada.execute('''
    INSERT INTO produtos (nome, categoria, preco, unidade, lançamento)
    VALUES (?, ?, ?, ?, ?)
    ''', (nome, categoria, preco, unidade, lançamento_do_produto))

    banco.commit()
    print(f"Produto '{nome}' inserido com sucesso!")

    entrada.close()

def cadastrar_fornecedor():
    banco = sqlite3.connect('hortifruti.db')
    entrada = banco.cursor()
    limpar_tela()
    nome = input("Digite o nome: ")
    cpnj = input("Digite o cnpj do estabelecimento (05.439.465/0001-67): ")
    email = str(input("Digite o email: "))
    produto_fornecedor = input("Qual produto você está fornecendo? (ex: temperos, verduras etc): ")
    
    entrada.execute('''
    INSERT INTO fornecedores (nome, contato, email, produto)
    VALUES (?, ?, ?, ?)
    ''', (nome, cpnj, email, produto_fornecedor))

    banco.commit()
    print(f"Fornecedor: '{nome}' cadastrado com sucesso!")

    entrada.close()

def menu_cadastro():
    """
    Exibe um menu para o usuário escolher qual cadastro deseja fazer no banco de dados.
    
    - O menu oferece as opções de cadastrar as tabelas: 'produtos' e 'fornecedores'.
    - O usuário escolhe uma das opções e a função correspondente é chamada.
    """

    print("\n--- Cadastrar ---")
    print("1. Cadastrar produto")
    print("2. Cadastrar fornecedor")

    escolha = input("Selecione uma opção (1-2): ")
    
    if escolha == "1":
        cadastrar_produto()
    elif escolha == "2":
        cadastrar_fornecedor()