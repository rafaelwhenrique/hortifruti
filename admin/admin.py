""" 
    Autentica o usuário administrador.

    Solicita ao usuário um login e uma senha. Em seguida, verifica se os dados inseridos 
    correspondem ao login e senha pré-definidos para o administrador.

    Retorna:
        booleano: True se o login e a senha estiverem corretos; caso contrário, False.
"""

def autenticar():
    usuario_admin = "admin"
    senha_admin = "senha123"

    usuario = input("Login admin: ")
    senha = input("Senha admin: ")


    return usuario == usuario_admin and senha == senha_admin

def autenticar_funcionario():
    usuario_admin = "funcionario"
    senha_admin = "func123"

    usuario = input("Login funcionário: ")
    senha = input("Senha funcionario: ")


    return usuario == usuario_admin and senha == senha_admin