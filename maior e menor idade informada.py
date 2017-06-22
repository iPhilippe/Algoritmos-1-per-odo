
i=int(input("Informe quantas idades serão informadas "))
m=0
me=1000
cont=0
while cont<i:
    a=int(input("Digite a sua idade: "))
    if a>m:
       m=a
    if a<me:
       me=a
    cont=cont+1
print("A maior idade é:", m, "e a menor idade é ", me)

# Forma algoritmica
'''
m=0;
i1=int(input("Digite a idade: "))
if (i1>m):
    m=i1
i2=int(input("Digite a idade: "))
if (i2>m):
    m=i2
i3=int(input("Digite a idade: "))
if (i3>m):
    m=i3
i4=int(input("Digite a idade: "))
if (i4>m):
    m=i4
i5=int(input("Digite a idade: "))
if (i5>m):
    m=i5
print(m)
'''
