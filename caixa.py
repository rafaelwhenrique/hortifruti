from produtos import get_produtos
import os

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def mostrar_produtos(produtos):
    print("Produtos disponíveis: ")
    for categoria, itens in produtos.items():
        print(f"\nCategoria: {categoria}")
        for nome, info in itens.items():
            print(f"Produto: {nome}, Preço: R${info['preco']} - Quantidade: {info['quantidade']}")

def forma_pagamento():
    print("\nFormas de pagamento disponíveis:")
    print("1. Crédito")
    print("2. Débito")
    print("3. Dinheiro")
    print("4. Pix")
    
    escolha = input("Escolha a forma de pagamento (1-4): ")
    
    if escolha == '1':
        return "Crédito"
    elif escolha == '2':
        return "Débito"
    elif escolha == '3':
        return "Dinheiro"
    elif escolha == '4':
        return "Pix"
    else:
        print("Escolha inválida! Tente novamente.")
        return forma_pagamento()

def verificar_cadastro():
    cadastro = input("Você já possui cadastro na loja? (S/N): ").lower()
    
    if cadastro == 's':
        cpf = input("Por favor, insira o seu CPF: ")
        print(f"CPF {cpf} verificado!")
    else:
        print("Continuando sem cadastro...")

def realizar_compra(produtos):
    total = 0.0
    itens_comprados = []

    while True:
        categoria = input("\nEscolha uma categoria de produtos (frutas, verduras, folhagens) ou digite 'sair' para finalizar a compra: ").lower()
        if categoria == 'sair':
            break

        if categoria in produtos:
            print(f"\nProdutos da categoria {categoria}:")
            for nome, info in produtos[categoria].items():
                print(f"{nome}: R${info['preco']} - Quantidade: {info['quantidade']}")

            produto_escolhido = input("\nDigite o nome do produto que deseja comprar ou 'voltar' para escolher outra categoria: ").title()

            if produto_escolhido == 'Voltar':
                continue

            if produto_escolhido in produtos[categoria]:
                qtd = int(input(f"Quantos {produto_escolhido}(s) deseja comprar? "))
                preco_produto = produtos[categoria][produto_escolhido]['preco']
                subtotal = preco_produto * qtd
                total += subtotal
                itens_comprados.append((produto_escolhido, qtd, subtotal))
                print(f"{qtd} {produto_escolhido}(s) adicionado(s) ao carrinho. Subtotal: R${subtotal:.2f}")
            else:
                print("Produto não encontrado. Tente novamente.")
        else:
            print("Categoria inválida. Tente novamente.")

    return total, itens_comprados

def finalizar_compra(total, itens_comprados):
    if itens_comprados:
        print("\nResumo da Compra:")
        for item in itens_comprados:
            print(f"{item[1]}x {item[0]} - Subtotal: R${item[2]:.2f}")
        print(f"\nTotal a pagar: R${total:.2f}")

        pagamento = forma_pagamento()
        print(f"Forma de pagamento escolhida: {pagamento}")
        print("Pagamento realizado com sucesso! Obrigado pela sua compra.")
    else:
        print("Nenhum item foi comprado.")

def sistema_caixa():
    limpar_tela()
    print("Bem-vindo ao sistema de caixa do hortifruti!")
    
    verificar_cadastro()
    produtos = get_produtos()
    mostrar_produtos(produtos)
    
    total, itens_comprados = realizar_compra(produtos)
    finalizar_compra(total, itens_comprados)

if __name__ == "__main__":
    sistema_caixa()
