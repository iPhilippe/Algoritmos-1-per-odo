n1=int(input("Digite a primeira nota: "))
n2=int(input("Digite a segunda nota: "))

m=(n1+n2)/2

if m>=9 and m<=10:
    print("Ótimo")
elif m>=7 and m<=8.9:
    print("Bom")
elif m>=6 and m<=6.9:
    print("Suficiente")
elif m>=0 and m<=5.9:
    print("Insuficiente")
