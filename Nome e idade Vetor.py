contador=0
nome=[]
idade=[]
while (contador<10):
    nome.append(input("Digite o nome: "))
    idade.append(int(input("Digite a idade: ")))

    print(nome, "idade:", idade)

    contador=contador+1
