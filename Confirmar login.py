usuario =(input("Cadastre seu usuário: "))
senha =(input("Cadastre sua senha: "))
while (usuario == senha):
     print("Dados iguais, digite novamente!")
     usuario =(input("Digite usuário: "))
     senha =(input("Digite senha: "))

usuario1 =(input("Digite seu usuário: "))
senha1 =(input("Digite sua senha: "))

while usuario1!=usuario:
     print("Usuário invalido!")
     usuario1 =(input("Digite usuário: "))
     senha1 =(input("Digite senha: "))

while senha1!=senha:
       print("Senha incorreta!")
       usuario1 =(input("Digite usuário: "))
       senha1 =(input("Digite senha: "))
if usuario1 == usuario and senha==senha1:
    print("Seja bem vindo!")

