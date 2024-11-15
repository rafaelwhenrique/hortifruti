from admin.admin import autenticar, autenticar_funcionario
from admin.cadastrar import menu_cadastro
from admin.listar import menu_listar
from admin.setup_db import menu_banco_de_dados
from admin.deletar import deletar_menu
from funcionario.caixa import sistema_caixa
from funcionario.cadastrar_cliente import cadastrar_cliente
from admin.atualizar import menu_atualizar
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


def menu_principal():
    print(" -- Bem-vindo ao sistema de gerenciamento do hortifruti! -- ")
    print("1. Acessar como administrador")
    print("2. Acessar como funcionário")
    print("3. Sair")

    escolha = input("Selecione uma opção (1-3): ")
    return escolha

def menu_admin():
    print("\n--- Menu do Administrador ---")
    print("1. Criar tabela no banco de dados")
    print("2. Cadastrar")
    print("3. Listar")
    print("4. Atualizar")
    print("5. Deletar")
    print("6. Deslogar")

    escolha = input("Selecione uma opção (1-6): ")
    return escolha

def menu_funcionario():
    
    print("\n--- Menu do Funcionário ---")
    print("1. Realizar venda")
    print("2. Cadastrar cliente")
    print("3. Deslogar")

    escolha = input("Selecione uma opção (1-3): ")
    return escolha

def iniciar_sistema():
    while True:
        limpar_tela()
        escolha_principal = menu_principal()
        
        if escolha_principal == "1":
            if autenticar():
                while True:
                    escolha_admin = menu_admin()

                    if escolha_admin == "1":
                        menu_banco_de_dados()

                    elif escolha_admin == "2":
                        menu_cadastro()

                    elif escolha_admin == "3":
                        menu_listar()

                    elif escolha_admin == "4":
                        menu_atualizar()

                    elif escolha_admin == "5":
                        deletar_menu()

                    elif escolha_admin == "6":
                        break  
            else:
                print("Acesso negado. Usuário ou senha incorretos.")

        elif escolha_principal == "2":
            if autenticar_funcionario():
                while True:
                    escolha_funcionario = menu_funcionario()

                    if escolha_funcionario == "1":
                        sistema_caixa()
                    elif escolha_funcionario == "2":
                        cadastrar_cliente()
                    elif escolha_funcionario == "3":
                        print("Deslogando...")
                        break  
                    else:
                        print("Opção inválida, tente novamente (1-3).")
            else:
                print("Acesso negado. Usuário ou senha incorretos.")

        elif escolha_principal == "3":
            break  
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    iniciar_sistema()