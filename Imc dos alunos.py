#Faça um programa que o usuário informe a quantidade de alunos de uma turma, o sistema deve ler o peso e altura de cada aluno, ao final informar a média dos pesos, alturas e imc.#


qtd=int(input("Digite a quantidade de alunos da sua turma: "))
peso=0
altura=0
for i in range(0, qtd):

  peso = int(input('Informe o peso do aluno: '))

  altura = float(input('Informe a altura do aluno: '))
  peso=peso+peso
  altura=altura+altura
  imc= peso/ (altura ** 2)

mediap=peso/qtd

mediaa=altura/qtd

mediai=imc/qtd

print("As médias dos pesos, alturas e imc são respectivamente: ", mediap, mediaa, mediai)


 ##Alternativa sem media
# quantidadeAlunos=int(input("Digite a quantidade de alunos a calcular: "))
# x=0
# while x!=quantidadeAlunos:
#     nome=(input("digite o nome do aluno(a): "))
#     altura=float(input("Digite a altura dos aluno(a)"))
#     peso=float(input("Digite o peso do aluno"))
#     imc=(peso/2*altura)
#     print(nome + ", o IMC equivalente é",imc)
#     x=x+1
