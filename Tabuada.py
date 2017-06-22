#6) Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:


l=int(input("Digite o valor: "))
x=0

while (x<=10):

    print("%d x %d = %d" % (l,x,l*x))
    x=x+1
