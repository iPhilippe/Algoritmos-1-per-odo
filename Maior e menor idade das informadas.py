x=0;
contador=int(input("Quantas idades serão informadas? R: "))
idades=[]
while (x<contador):
    idades.append(input("Digite a idade: "))
    x=x+1
print (max(idades))
print (min(idades))


# ///////  Forma "Algorítmica"
#
# i=int(input("Informe quantas idades serão informadas "))
# m=0
# me=1000
# cont=0
# while cont<i:
#     a=int(input("Digite a sua idade: "))
#     if a>m:
#         m=a
#         if a<me:
#             me=a
#             cont=cont+1
#             print("A maior idade é:", m, "e a menor idade é ", me)
