# 40. Escreva um programa que solicite ao usuário um número e exiba se ele é
# positivo OU se ele é divisível por 3 OU se ele é menor que -10.

num = int(input("Digite um número: "))

if num > 0 or num % 3 == 0 or num < -10:
    print("O número é positivo OU é divisível por 3 OU é menor que -10.")
else:
    print("O número não é positivo OU não é divisível por 3 OU não é menor que -10.")

