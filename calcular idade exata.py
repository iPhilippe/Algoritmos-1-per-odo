anoNascimento=(int(input("Digite seu ano de nascimento: ")))
mesNascimento=(int(input("Digite seu mes de nascimento: ")))
diaNascimento=(int(input("Digite seu dia de nascimento: ")))

ano = 2017 - anoNascimento

if mesNascimento>= 6 and diaNascimento>=7:
    print(ano-1)
else:
        print(ano)
