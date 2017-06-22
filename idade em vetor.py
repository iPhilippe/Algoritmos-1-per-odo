#Altere o exercício e armazene num vetor as idades informadas.

x=0;
contador=int(input("Quantas idades serão informadas? R: "))
idades=[]
while (x<contador):
    idades.append(input("Digite a idade: "))
    x=x+1
print (idades)
