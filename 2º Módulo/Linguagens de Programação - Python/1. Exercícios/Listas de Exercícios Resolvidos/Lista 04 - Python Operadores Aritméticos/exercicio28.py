# 28. Escreva um programa que solicite ao usuário sua altura e exiba se ele é
# considerado baixo, médio ou alto (levando em consideração as médias de
# altura para a sua idade e sexo).

altura = float(input("Digite sua altura em metros: "))
genero = input("Digite seu gênero (M/F): ")

if genero == "M":
    if altura < 1.67:
        print("Sua altura é considerada baixa.")
    elif altura < 1.79:
        print("Sua altura é considerada média.")
    else:
        print("Sua altura é considerada alta.")
elif genero == "F":
    if altura < 1.55:
        print("Sua altura é considerada baixa.")
    elif altura < 1.67:
        print("Sua altura é considerada média.")
    else:
        print("Sua altura é considerada alta.")
else:
    print("Gênero inválido.")
