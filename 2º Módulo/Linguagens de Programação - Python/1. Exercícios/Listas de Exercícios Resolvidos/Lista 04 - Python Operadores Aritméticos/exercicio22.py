# 22. Escreva um programa que solicite ao usuário dois números e exiba se o
# primeiro número é maior, menor ou igual ao segundo número.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print(f"{num1} é maior que {num2}.")
elif num1 < num2:
    print(f"{num1} é menor que {num2}.")
else:
    print(f"{num1} é igual a {num2}.")

