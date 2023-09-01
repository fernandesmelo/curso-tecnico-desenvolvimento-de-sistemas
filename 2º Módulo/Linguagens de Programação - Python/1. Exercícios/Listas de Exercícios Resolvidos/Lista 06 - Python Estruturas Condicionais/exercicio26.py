# 26. Crie um programa que leia o peso e a altura de uma pessoa e calcule o índice de massa
# corporal (IMC). De acordo com o IMC, imprima se a pessoa está abaixo do peso, no peso
# normal, com sobrepeso ou obesa. Use a instrução MATCH.

peso = float(input("Digite seu peso em quilogramas: "))

altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura * altura)

match(imc):
    case imc if imc < 18.5:
        print("Seu IMC é: {:.2f}".format(imc))
        print("Você está abaixo do peso.")
    case  imc if imc >= 18.5 and imc < 25:
        print("Seu IMC é: {:.2f}".format(imc))
        print("Você está no peso normal.")
    case imc if imc >= 25 and imc < 30:
        print(f"Seu IMC é: {imc:.2f}")
        print("Você está com sobrepeso.")
    case _:
        print(f"Seu IMC é: {imc:.2f}")
        print("Você está obeso.")


    