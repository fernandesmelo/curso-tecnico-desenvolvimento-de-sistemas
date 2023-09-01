# 10. Crie um programa que receba a idade de uma pessoa e verifique se ela é criança (até 12
# anos), adolescente (entre 13 e 17 anos) ou adulto (maior de 18 anos). Use a instrução
# IF/ELSE.

idade = int(input("Digite a sua idade: "))

if idade <= 12:
    print("Você é uma criança.")
elif idade <= 17:
    print("Você é um adolescente.")
else:
    print("Você é um adulto.")

