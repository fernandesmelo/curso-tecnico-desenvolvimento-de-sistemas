# 33. Escreva um programa que solicite ao usuário um número e exiba se ele é
# positivo E ímpar.

num = int(input("Digite um número: "))

if num > 0 and num % 2 != 0:
    print("O número é positivo e ímpar.")
else:
    print("O número não é positivo e/ou não é ímpar.")
