x="s"
while x=="s":

    n=input("digite seu nome:   ")
    print("Ola"+n)
    n1=int(input("Digite n1:  "))
    n2=int(input("Digite n2:  "))
    n3=int(input("Digite n3:  "))
    n4=int(input("Digite n4:  "))

    m=(n1+n2+n3+n4)/4
    print("Ola %s vou exibir sua nota: "%n)
    print (m)
    print("Ola %s sua nota foi %4.1f"%(n, m))

    if m>=9:
         sit="Otimo"
    elif m>=7:                                   #elif = else + if#
         sit="Bom"
    elif m>=6:
         sit="suficiente"
    else:
         sit="insuficiente"

         print(sit)
    print("Ola %s sua nota foi %4.1f e seu nível é %s"%(n, m, sit))
    x=x+1
    x= input("s/n")
