usuario=input("Digite seu nome para dar continuidade: ")
print("\nOlá,", usuario); print("Hoje iremos aprender sobre a tabela verdade!")

op=int(input("\nSelecione uma das opções para saber mais:  Conjunção [1];  Disjunção [2];  Condição [3];  Bi Condição [4];  Negação [5];  Ordem de execução[6];  Continuar para exemplo [7]: "))

while (op!=7):

    if op==1:
      print("\nConjunção[^] - Representa o “p e q” e tem a saída verdadeira somente quando as dois condições forem verdadeiras")
      op=int(input("Selecione para continuar: Conjunção [1] - Disjunção [2] - Condição [3] - Bi Condição [4] Negação [5] Ordem de execução[6] - Continuar para exemplo [7] "))
    if op==2:
      print ("\nDisjunção[v] - Representa o “p ou q” e tem a saída falsa somente quando as dois condições forem falsas)")
      op=int(input("Selecione para continuar: Conjunção [1] - Disjunção [2] - Condição [3] - Bi Condição [4] Negação [5] Ordem de execução[6] - Continuar para exemplo [7]"))
    if op==3:
      print ("\nCondição[->] - (Representa o “se p então q” e tem a saída falsa somente quando a primeira condição for verdadeira e a segunda falsa)")
      op=int(input("Selecione para continuar: Conjunção [1] - Disjunção [2] - Condição [3] - Bi Condição [4] Negação [5] Ordem de execução[6] - Continuar para exemplo [7]"))
    if op==4:
      print("\nBi condição[<->] - (Representa o “p se e somente se q” e tem a saída verdadeira somente quando as dois condições forem iguais)")
      op=int(input("Selecione para continuar: Conjunção [1] - Disjunção [2] - Condição [3] - Bi Condição [4] Negação [5] Ordem de execução[6] - Continuar para exemplo [7]"))
    if op==5:
      print("\nNegação[¬] - (Tem o poder de inverter o valor de origem)")
      op=int(input("Selecione para continuar Conjunção [1] - Disjunção [2] - Condição [3] - Bi Condição [4] Negação [5] Ordem de execução[6] - Continuar para exemplo [7]"))
    if op==6:
      print("\nA ordem de prioridades na resolução, é respectivamente: \n1º- Parenteses; \n2º- Negação; \n3º- Conjunção; \n4º- Disjunção; \n5º- Condição; \n6º-Bi condição ")
      op=int(input("Selecione para continuar Conjunção [1] - Disjunção [2] - Condição [3] - Bi Condição [4] Negação [5] Ordem de execução[6] - Continuar para exemplo [7]"))


p=0
while p!= "sair":
    print('\nDada a expressão,____ P v (Q ^ R) <--> (P v Q) ^(P v R) ____, apresente o valor desejado e obtenha a resposta correspondente, digite "sair" para terminar.')
    p=(input('Para a porta "P", escolha: V ou F'))
    q=(input('Para a porta "Q", escolha: V ou F'))
    r=(input('Para a porta "R", escolha: V ou F'))
    print("De acordo com as regras de Conjunção; Disjunção; Condição; Bi Condição; Negação;  apresentadas anteriorente, temos: ")


    if p=="v" and q=="v" and r=="v":
             print('(Q ^ R) = V;\n(P v Q) = V; \n(P v R) = V;\nLogo:\n(P v Q) ^ (P v R) = V; \nP v (Q ^ R) = V;\nResultado final: P v (Q ^ R) <-> (P v Q) ^ (P v R) = V')
    if p=="v" and q=="v" and r=="f":
             print('(Q ^ R) = F;\n(P v Q) = V; \n(P v R) = V;\nLogo:\n(P v Q) ^ (P v R) = V; \nP v (Q ^ R) = V;\nResultado final: P v (Q ^ R) <-> (P v Q) ^ (P v R) = V')
    if p=="v" and q=="f" and r=="v":
             print('(Q ^ R) = F;\n(P v Q) = V; \n(P v R) = V;\nLogo:\n(P v Q) ^ (P v R) = V; \nP v (Q ^ R) = V;\nResultado final: P v (Q ^ R) <-> (P v Q) ^ (P v R) = V')
    if p=="v" and q=="f" and r=="f":
             print('(Q ^ R) = F;\n(P v Q) = V; \n(P v R) = V;\nLogo:\n(P v Q) ^ (P v R) = V; \nP v (Q ^ R) = V;\nResultado final: P v (Q ^ R) <-> (P v Q) ^ (P v R) = V')
    if p=="f" and q=="v" and r=="v":
             print('(Q ^ R) = V;\n(P v Q) = V; \n(P v R) = V;\nLogo:\n(P v Q) ^ (P v R) = V; \nP v (Q ^ R) = V;\nResultado final: P v (Q ^ R) <-> (P v Q) ^ (P v R) = V')
    if p=="f" and q=="v" and r=="f":
             print('(Q ^ R) = F;\n(P v Q) = V; \n(P v R) = F;\nLogo:\n(P v Q) ^ (P v R) = F; \nP v (Q ^ R) = F;\nResultado final: P v (Q ^ R) <-> (P v Q) ^ (P v R) = V')
    if p=="f" and q=="f" and r=="v":
             print('(Q ^ R) = F;\n(P v Q) = F; \n(P v R) = V;\nLogo:\n(P v Q) ^ (P v R) = F; \nP v (Q ^ R) = F;\nResultado final: P v (Q ^ R) <-> (P v Q) ^ (P v R) = V')
    if p=="f" and q=="f" and r=="f":
             print('(Q ^ R) = F;\n(P v Q) = F; \n(P v R) = F;\nLogo:\n(P v Q) ^ (P v R) = F; \nP v (Q ^ R) = F;\nResultado final: P v (Q ^ R) <-> (P v Q) ^ (P v R) = V')
print('Fim do exercício')
