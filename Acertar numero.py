n=int(input("Digite número na faixa de 0 à 10: "))

if n>10 or n<0:
      print("Inválido, tente novamente!")

while (n!=5):
    if n!=5:
        print("tente novamente")
        n=int(input("Digite número na faixa de 0 à 10: "))
    if n == 5:
       print("Você acertou!!!")
