# 25. Escreva um programa que solicite ao usuário um número e exiba se ele é
# positivo, negativo ou igual a zero.

num = float(input("Digite um número: "))

if num > 0:
    print("O número é positivo.")
elif num < 0:
    print("O número é negativo.")
else:
    print("O número é igual a zero.")
