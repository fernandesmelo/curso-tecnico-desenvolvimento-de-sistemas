# 35. Escreva um programa que solicite ao usuário um número e exiba se ele é
# múltiplo de 2 E de 3.

num = int(input("Digite um número: "))

if num % 2 == 0 and num % 3 == 0:
    print(num, "é múltiplo de 2 e de 3.")
else:
    print(num, "não é múltiplo de 2 e de 3.")

