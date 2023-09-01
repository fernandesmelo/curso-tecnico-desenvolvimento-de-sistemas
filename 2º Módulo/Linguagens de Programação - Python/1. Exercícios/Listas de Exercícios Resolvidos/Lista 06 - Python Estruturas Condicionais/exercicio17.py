# 17. Crie um programa que leia o peso e a altura de uma pessoa e calcule o índice de massa
# corporal (IMC). De acordo com o IMC, imprima se a pessoa está abaixo do peso, no peso
# normal, com sobrepeso ou obesa. Use a instrução ELIF.

peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obeso")
