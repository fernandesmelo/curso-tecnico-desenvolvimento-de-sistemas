# 38. Escreva um programa que solicite ao usuário um número e exiba se ele é
# maior que 10 E menor que 20 OU se ele é maior que 30 E menor que 40.
num = float(input("Digite um número: "))

if (num > 10 and num < 20) or (num > 30 and num < 40):
    print("O número está entre 10 e 20 ou entre 30 e 40.")
else:
    print("O número não está dentro das condições especificadas.")

