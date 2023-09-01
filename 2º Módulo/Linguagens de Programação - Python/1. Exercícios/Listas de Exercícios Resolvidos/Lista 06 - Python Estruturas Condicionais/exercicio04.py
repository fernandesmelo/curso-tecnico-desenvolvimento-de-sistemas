# 4. Escreva um programa que verifique se um número é par ou ímpar. Use a
# instrução IF.

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print(numero, "é um número par.")
else:
    print(numero, "é um número ímpar.")
