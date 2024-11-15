import sqlite3

# DELETANDO ELEMENTOS

def deletar_produto():
    """
    Deleta um produto do banco de dados.

    Esta função solicita o nome do produto que o usuário deseja deletar.
    Ela tenta encontrar e remover o produto na tabela 'produtos' com base no nome.

    Retorna:
        Uma mensagem de sucesso se o produto foi deletado,
        ou uma mensagem de erro se o produto não foi encontrado.
    """

    banco = sqlite3.connect('hortifruti.db')
    entrada = banco.cursor()
    nome = input("Digite o nome do produto que deseja deletar: ")
    entrada.execute('''
    DELETE FROM produtos WHERE nome = ?
    ''', (nome,))
    banco.commit()
    if entrada.rowcount > 0:
        print(f"Produto: '{nome}' deletado com sucesso!")
    else:
        print(f"Produto: '{nome}' não encontrado.")
    entrada.close()

def deletar_cliente():
    """
    Deleta um cliente do banco de dados.

    Esta função solicita o nome do cliente que o usuário deseja deletar.
    Ela tenta encontrar e remover o cliente na tabela 'clientes' com base no nome.

    Retorna:
        Uma mensagem de sucesso se o cliente foi deletado,
        ou uma mensagem de erro se o cliente não foi encontrado.
    """

    banco = sqlite3.connect('hortifruti.db')
    entrada = banco.cursor()
    nome = input("Digite o nome do cliente que deseja deletar: ")
    entrada.execute('''
    DELETE FROM clientes WHERE nome = ?
    ''', (nome,))
    banco.commit()
    if entrada.rowcount > 0:
        print(f"Cliente: '{nome}' deletado com sucesso!")
    else:
        print(f"Cliente: '{nome}' não encontrado.")
    entrada.close()
    
def deletar_fornecedor():
    """
    Deleta um fornecedor do banco de dados.

    Esta função solicita o nome do fornecedor que o usuário deseja deletar.
    Ela tenta encontrar e remover o fornecedor na tabela 'fornecedores' com base no nome.

    Retorna:
        Uma mensagem de sucesso se o fornecedor foi deletado,
        ou uma mensagem de erro se o fornecedor não foi encontrado.
    """

    banco = sqlite3.connect('hortifruti.db')
    entrada = banco.cursor()
    
    nome = input("Digite o nome do fornecedor que deseja deletar: ")
    entrada.execute('''
    DELETE FROM fornecedores WHERE nome = ?
    ''', (nome,))

    banco.commit()


    if entrada.rowcount > 0:
        print(f"Fornecedor: '{nome}' deletado com sucesso!")
    else:
        print(f"Fornecedor: '{nome}' não encontrado.")

    entrada.close()

# DELETANDO TABELAS
def deletar_tabela_produtos():
    """
    Deleta a tabela 'produtos' do banco de dados, se ela existir.

    Conecta-se ao banco de dados 'hortifruti.db' e executa o comando SQL
    para remover a tabela 'produtos'. Fecha a conexão ao final.
    """

    banco = sqlite3.connect('hortifruti.db')
    entrada = banco.cursor()
    entrada.execute('DROP TABLE IF EXISTS produtos')
    banco.commit()
    banco.close()

def deletar_tabela_fornecedores():
    """
    Deleta a tabela 'fornecedores' do banco de dados, se ela existir.

    Conecta-se ao banco de dados 'hortifruti.db' e executa o comando SQL
    para remover a tabela 'fornecedores'. Fecha a conexão ao final.
    """
    
    banco = sqlite3.connect('hortifruti.db')
    entrada = banco.cursor()
    entrada.execute('DROP TABLE IF EXISTS fornecedores')
    banco.commit()
    banco.close()

def deletar_tabela_clientes():
    """
    Deleta a tabela 'clientes' do banco de dados, se ela existir.

    Conecta-se ao banco de dados 'hortifruti.db' e executa o comando SQL
    para remover a tabela 'clientes'. Fecha a conexão ao final.
    """
    
    banco = sqlite3.connect('hortifruti.db')
    entrada = banco.cursor()
    entrada.execute('DROP TABLE IF EXISTS clientes')
    banco.commit()
    banco.close()

# MENU PARA ACESSO DAS FUNÇÕES DE DELEÇÃO DE ELEMENTOS
def excluir_elementos_menu():
    print("\n--- Deletar Elementos ---")
    print("1. Deletar produto")
    print("2. Deletar cliente")
    print("3. Deletar fornecedor")
    escolha = input("Qual tabela deseja edeletar? (1-3): ")
    if escolha == '1':
        deletar_produto()
        print("Produto deletado com sucesso!")
    elif escolha == '2':
        deletar_cliente()
        print("Cliente deletado com sucesso!")
    elif escolha == '3':
        deletar_fornecedor()
        print("Fornecedor deletado com sucesso!")

#MENU PARA ACESSO DAS FUNÇÕES DE DELEÇÃO DE TABELAS
def excluir_tabelas_menu():
    """
    Exibe um menu para selecionar qual tabela do banco de dados deve ser deletada.

    Dependendo da escolha do usuário, a função chama a função correspondente para 
    deletar a tabela 'produtos', 'clientes' ou 'fornecedores'.
    
    Retorna:
        Mensagem de confirmação sobre qual tabela foi deletada.
    """
    
    print("\n--- Deletar Tabelas ---")
    print("1. Tabela produtos")
    print("2. Tabela clientes")
    print("3. Tabela fornecedores")
    escolha = input("Qual tabela deseja edeletar? (1-3): ")
    if escolha == '1':
        deletar_tabela_produtos()
        print("Tabela produtos deletada com sucesso!")
    elif escolha == '2':
        deletar_tabela_clientes()
        print("Tabela clientes deletada com sucesso!")
    elif escolha == '3':
        deletar_tabela_fornecedores()
        print("Tabela fornecedores deletada com sucesso!")

# Facilitando o acesso ao usuário, esse menu acessa o menu de excluir elementos e exluir tabelas
def deletar_menu():
    """
    Exibe um menu para o usuário escolher qual tabela deseja deletar no banco de dados.
    
    - O menu oferece as opções de deletar as tabelas: 'produtos', 'clientes' e 'fornecedores'.
    - O menu oferece as opções de deletar os elementos dentro das tabelas: 'produtos', 'clientes' e 'fornecedores'.
    - O usuário escolhe uma das opções e a função correspondente é chamada.
    """
    print("\n--- Deletar ---")
    print("1. Deletar Tabelas")
    print("2. Deletar Elementos")
    print("3. Deslogar")

    escolha = input("Selecione uma opção (1-3): ")
    if escolha == "1":
        excluir_tabelas_menu()
    elif escolha == "2":
        excluir_elementos_menu()