#leia 3 numeros e coloque em ordem (do menor para o maior)

n1=int(input("Digite primeiro número "))
n2=int(input("digite segundo numero "))
n3=int(input("digite terceiro número "))

if  n1>n2 and n1>n3:
    M=n1
if  n2>n1 and n2>n3:
    M=n2
if n3>n1 and n3>n2:
    M=n3

if  n1<n2 and n1<n3:
    n=n1
if  n2<n1 and n2<n3:
    n=n2
if n3<n1 and n3<n2:
    n=n3
