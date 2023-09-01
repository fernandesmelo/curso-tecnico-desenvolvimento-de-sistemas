# 29. Escreva um programa que solicite ao usuário um número e exiba se ele é
# múltiplo de 3 e/ou de 5.

num = int(input("Digite um número inteiro: "))

if num % 3 == 0 and num % 5 == 0:
    print("O número é múltiplo de 3 e de 5.")
elif num % 3 == 0:
    print("O número é múltiplo de 3.")
elif num % 5 == 0:
    print("O número é múltiplo de 5.")
else:
    print("O número não é múltiplo nem de 3 nem de 5.")

