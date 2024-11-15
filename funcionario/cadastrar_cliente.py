import sqlite3
import os

def limpar_tela():
    """Limpa a tela do terminal, compatível com Windows e Unix."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def cadastrar_cliente():
    """
    Cadastra um novo cliente no banco de dados 'hortifruti.db'.

    A função solicita ao usuário o nome e o número de celular do cliente,
    e depois insere essas informações na tabela 'clientes' do banco de dados SQLite.
    
    O fluxo de execução é o seguinte:
    1. Solicita o nome e o número de celular do cliente.
    2. Insere esses dados na tabela 'clientes'.
    3. Exibe uma mensagem de confirmação de cadastro.

    Retorno:
        Nenhum. Apenas insere os dados no banco de dados e imprime uma mensagem.
    """
    
    banco = sqlite3.connect('hortifruti.db')
    entrada = banco.cursor()
    limpar_tela()
    nome = input("Digite o seu nome: ")
    numero = int(input("Digite o seu numero de celular: "))
    
    entrada.execute('''
    INSERT INTO clientes (nome, contato)
    VALUES (?, ?)
    ''', (nome, numero))

    banco.commit()
    print(f"Cliente: '{nome}' cadastrado com sucesso!")

    entrada.close()