import os

def limpar_tela():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para Unix/Linux/Mac
    else:
        os.system('clear')

def login():
    print('\t\t TELA DE LOGIN - SISTEMA DE GERENCIAMENTO HORTIFRUTI')
    input('Insira o login: ').lower()
    input('Insira o password: ')
    confirm_login = input('digite ok para continuar: ').lower()
    return confirm_login == 'ok'

def cadastre():
    if login():
        limpar_tela()
        print('\t\t Bem vindo a tela inicial')
        confirmar_produto = input('Deseja cadastrar algum produto? (s/n): ').lower()
        print('Produtos cadastráveis: [frutas, verduras e folhagens]')
        produtos = []
        if confirmar_produto == "s":
            limpar_tela()
            cadastro_produtos = input('cadastro de produtos: ')
            produtos.append(cadastro_produtos)
            print(f'Produto cadastrado com sucesso: {cadastro_produtos}')
        elif(confirmar_produto == "n"):
            limpar_tela()
            print('Nenhum produto cadastrado.')
        else:
            print('Opção inválida. Tente novamente.')
            cadastre()
cadastre()