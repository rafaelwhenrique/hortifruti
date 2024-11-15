import sqlite3
def atualizar_cliente():

    banco = sqlite3.connect('hortifruti.db')
    cursor = banco.cursor()
    
    id_cliente = input("Digite o ID do cliente que deseja atualizar: ")
    novo_nome = input("Digite o novo nome do cliente: ")
    novo_contato = input("Digite o novo contato do cliente: ")

    cursor.execute("UPDATE clientes SET nome = ?, contato = ? WHERE id = ?", (novo_nome, novo_contato, id_cliente))
    banco.commit()
    print("Cliente atualizado com sucesso!")
    
    cursor.close()
    banco.close()

def atualizar_fornecedor():

    banco = sqlite3.connect('hortifruti.db')
    cursor = banco.cursor()
    
    id_fornecedor = input("Digite o ID do fornecedor que deseja atualizar: ")
    novo_nome = input("Digite o novo nome do fornecedor: ")
    novo_contato = input("Digite o novo contato do fornecedor: ")
    novo_email = input("Digite o novo e-mail do fornecedor: ")
    novo_produto = input("Digite o novo produto do fornecedor: ")

    cursor.execute("UPDATE fornecedores SET nome = ?, contato = ?, email = ?, produto = ? WHERE id = ?", (novo_nome, novo_contato, novo_email, novo_produto, id_fornecedor))
    banco.commit()
    print("Fornecedor atualizado com sucesso!")
    
    cursor.close()
    banco.close()

def atualizar_produto():
    banco = sqlite3.connect('hortifruti.db')
    cursor = banco.cursor()
    
    id_produto = input("Digite o ID do produto que deseja atualizar: ")
    novo_nome = input("Digite o novo nome do produto: ")
    nova_categoria = input("Digite a nova categoria do produto: ")
    novo_preco = float(input("Digite o novo preço do produto: "))
    nova_unidade = input("Digite a nova unidade do produto (kg ou un): ")
    novo_lancamento = input("Digite a nova data de lançamento do produto (AAAA-MM-DD): ")

    cursor.execute("UPDATE produtos SET nome = ?, categoria = ?, preco = ?, unidade = ?, lançamento = ? WHERE id = ?", (novo_nome, nova_categoria, novo_preco, 
                                                                                                                        nova_unidade, novo_lancamento, id_produto))
    banco.commit()
    print("Produto atualizado com sucesso!")
    
    cursor.close()
    banco.close()

def menu_atualizar():
    print("\nEscolha o que deseja atualizar:")
    print("1 - Cliente")
    print("2 - Fornecedor")
    print("3 - Produto")
    escolha = input("Digite o número da opção: ")

    if escolha == '1':
        atualizar_cliente()
    elif escolha == '2':
        atualizar_fornecedor()
    elif escolha == '3':
        atualizar_produto()