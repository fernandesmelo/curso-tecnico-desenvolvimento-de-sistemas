# 18. Faça um programa que leia a idade de uma pessoa e imprima sua classificação de
# acordo com a tabela abaixo: Use a instrução ELIF.
# • Idade até 12 anos: Criança
# • Idade entre 13 e 17 anos: Adolescente
# • Idade entre 18 e 59 anos: Adulto
# • Idade a partir de 60 anos: Idoso

idade = int(input("Digite a idade: "))

if idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")
