# 32. Escreva um programa que solicite ao usuário sua altura e exiba se ele é
# considerado baixo OU se ele tem menos de 18 anos.

altura = float(input("Digite a sua altura em metros: "))
idade = int(input("Digite a sua idade: "))

if altura < 1.60 or idade < 18:
    print("Você é considerado baixo.")
else:
    print("Você não é considerado baixo.")

