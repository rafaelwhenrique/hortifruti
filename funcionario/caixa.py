import sqlite3
import os
import time

def forma_pagamento(valor_total):
    """
    Função para escolher e processar a forma de pagamento.

    Args:
    valor_total (float): O total da compra a ser pago.

    Returns:
    string: Mensagem indicando o sucesso do pagamento.
    """
    print("\nFormas de pagamento disponíveis:")
    print("1. Crédito")
    print("2. Débito")
    print("3. Dinheiro")
    print("4. Pix")

    # Solicita ao usuário escolher uma forma de pagamento
    escolha = input("Escolha a forma de pagamento (1-4): ")
    # Verifica a escolha e executa o processo correspondente
    if escolha == '1':
        print("Você escolheu pagamento por Crédito.")
        senha = int(input("Digite a senha do cartão: ")) # Solicita a senha do cartão
        print("Processando pagamento...")
        time.sleep(.5)
        return "Pagamento com crédito aprovado."
    
    elif escolha == '2':
        print("Você escolheu pagamento por Débito.")
        senha = int(input("Digite a senha do cartão: "))
        print("Processando pagamento...")
        time.sleep(.5)
        return "Pagamento com crédito aprovado."
    
    elif escolha == '3':
        print("Você escolheu pagamento em Dinheiro.")
        while True:
            try:
                cedula = float(input("Insira o valor da cédula que possui: R$ ")) # Solicita o valor da cédula
                if cedula >= valor_total: # Verifica se o valor da cédula é suficiente para a compra
                    troco = cedula - valor_total # Calcula o troco
                    print(f"Pagamento aceito. Seu troco é: R$ {troco:.2f}")
                    return "Pagamento em dinheiro concluído."
                else:
                    print("Valor insuficiente. Por favor, insira uma cédula com valor igual ou superior ao total da compra.")
            except ValueError:
                print("Valor inválido. Tente novamente inserindo um número.") 

    elif escolha == '4':
        print("Você escolheu pagamento por Pix.")  
        chave_pix = input("Digite sua chave Pix para receber o código de pagamento: ") 
        print("Processando pagamento...")
        time.sleep(.5)
        return "Pagamento por Pix aprovado."
    else:
        print("Escolha inválida! Tente novamente.")
        return forma_pagamento()  # Se a escolha for inválida, chama a função novamente

def realizar_compra():
    """
    Função para realizar a compra de produtos no sistema.

    Esta função permite ao usuário selecionar categorias e produtos, calcular o total da compra 
    e retornar uma lista com os itens comprados.

    Returns:
    tuple: Contém o total da compra (float) e uma lista de itens comprados (lista de tuplas).
    """
    caminho_banco = os.path.join(os.path.dirname(__file__), '..', 'hortifruti.db')
    conexao = sqlite3.connect(caminho_banco)
    cursor = conexao.cursor()
    total = 0.0 # Inicializa o total da compra como 0
    itens_comprados = [] # Lista que armazenará os itens comprados

    while True:
        cursor.execute("SELECT DISTINCT categoria FROM produtos") # Consulta as categorias de produtos no banco
        categorias = [categoria[0] for categoria in cursor.fetchall()] # Extrai as categorias
        print("\nCategorias disponíveis:", ", ".join(categorias)) # Exibe as categorias disponíveis

        categoria = input("\nEscolha uma categoria de produtos ou digite 'sair' para finalizar a compra: ").lower()

        if categoria == 'sair':
            break

        if categoria in categorias: # Verifica se a categoria escolhida é válida
            cursor.execute("SELECT id, nome, preco, unidade FROM produtos WHERE categoria = ?", (categoria,))  # Consulta os produtos da categoria
            produtos = cursor.fetchall() # Pega todos os produtos da categoria

            if not produtos:  # Caso não haja produtos na categoria, avisa o usuário
                print("Nenhum produto disponível nesta categoria.") 
                continue

            print(f"\nProdutos da categoria {categoria.capitalize()}:")
            for produto in produtos: # Exibe os produtos da categoria
                id_produto, nome, preco, unidade = produto
                print(f"{id_produto}. {nome} - R${preco:.2f}/{unidade}")

            produto_id = input("\nDigite o número do produto que deseja comprar ou 'voltar' para escolher outra categoria: ")
            if produto_id == 'voltar':
                continue

            # Verifica se o ID é válido 
            if produto_id.isdigit():
                produto_id = int(produto_id)
                cursor.execute("SELECT nome, preco, unidade FROM produtos WHERE id = ?", (produto_id,))
                resultado = cursor.fetchone()

                if resultado:  # Se o produto for encontrado
                    nome_produto, preco_produto, unidade_produto = resultado
                    if unidade_produto == "kg": # Se a unidade for em kg, solicita a quantidade em kg
                        quantidade = float(input(f"Quantos kg de {nome_produto} deseja comprar? "))
                        subtotal = preco_produto * quantidade
                        print(f"{quantidade} kg do produto {nome_produto} adicionado(s) ao carrinho. Subtotal: R${subtotal:.2f}")

                    elif unidade_produto == "un": # Se a unidade for em unidades, solicita a quantidade em unidades
                        quantidade = int(input(f"Quantas unidades de {nome_produto} deseja comprar? "))
                        subtotal = preco_produto * quantidade # Calcula o subtotal
                        print(f"{quantidade} unidade(s) do produto {nome_produto} adicionado(s) ao carrinho. Subtotal: R${subtotal:.2f}")

                    else:
                        print(f"A unidade do produto {nome_produto} não é suportada.")
                        continue

                    total += subtotal # Adiciona o subtotal ao total da compra
                    itens_comprados.append((nome_produto, quantidade, subtotal)) # Adiciona o item à lista de compras
                else:
                    print("Produto não encontrado. Tente novamente.")
            else:
                print("ID inválido. Tente novamente.")
        else:
            print("Categoria inválida. Tente novamente.")
    print(f"\nTotal da compra: R${total:.2f}") # Exibe o total da compra
    return total, itens_comprados # Retorna o total e os itens comprados
    
def finalizar_compra(total, itens_comprados):
    """
    Função para finalizar a compra, exibindo o resumo e o total a pagar.

    Args:
    total (float): O total da compra a ser pago.
    itens_comprados (list): Lista de itens comprados, com nome, quantidade e subtotal.

    Returns:
    None
    """
    if itens_comprados:
        print("\nResumo da Compra:")
        for item in itens_comprados: # Exibe o resumo de todos os itens comprados
            print(f"{item[1]} de {item[0]} - Subtotal: R${item[2]:.2f}")
        print(f"\nTotal a pagar: R${total:.2f}") # Exibe o total a ser pago


        pagamento = forma_pagamento(total)  # Chama a função de forma de pagamento
        print(f"Forma de pagamento escolhida: {pagamento}")
        print("Pagamento realizado com sucesso! Obrigado pela sua compra.")
    else:
        print("Nenhum item foi comprado.") # Caso o carrinho esteja vazio


def sistema_caixa():
    """
    Função principal do sistema de caixa, gerenciando todo o processo de compras.

    Esta função é responsável por iniciar o processo de compra, chamar as funções 
    para realizar a compra, calcular o total e finalizar o pagamento.

    Returns:
    None
    """
    print("Bem-vindo ao caixa do hortifruti!")
    time.sleep(0.5) # Simula um pequeno atraso para dar tempo ao usuário
    total, itens_comprados = realizar_compra()  # Chama a função para realizar a compra
    finalizar_compra(total, itens_comprados) # Finaliza a compra e exibe o resumo