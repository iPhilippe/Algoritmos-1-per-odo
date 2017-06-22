n=input("digite seu nome: ")
print("Ola")
n1=int(input("Digite n1: "))
n2=int(input("Digite n2: "))
n3=int(input("Digite n3: "))
n4=int(input("Digite n4: "))

m=(n1+n2+n3+n4)/4
print("Ola %s vou exibir sua nota: "%n)
print (m)
print("Ola %s sua nota foi %4.1f"%(n, m))

if m>=9:
    print("Otimo")
elif m>=7:
    print("Bom")
elif m>=6:
    print("suficiente")
else:
    print("insuficiente")
