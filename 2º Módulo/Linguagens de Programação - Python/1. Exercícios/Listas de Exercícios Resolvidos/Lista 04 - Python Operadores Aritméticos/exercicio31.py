# 4 OPERADORES LÓGICOS 

# 31. Escreva um programa que solicite ao usuário sua idade e exiba se ele é
# maior de idade E menor que 65 anos.

idade = int(input("Digite sua idade: "))

if idade >= 18 and idade < 65:
    print("Você é maior de idade e menor que 65 anos.")
else:
    print("Você não é maior de idade e/ou não é menor que 65 anos.")
