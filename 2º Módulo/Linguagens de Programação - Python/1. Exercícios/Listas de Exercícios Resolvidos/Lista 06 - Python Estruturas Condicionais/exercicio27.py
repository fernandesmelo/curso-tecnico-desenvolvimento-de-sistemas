# 27. Faça um programa que leia uma nota de 0 a 10 e imprima uma mensagem
# correspondente à tabela abaixo: Use a instrução MATCH.
# • Nota de 0 a 2.9: Insuficiente
# • Nota de 3 a 4.9: Regular
# • Nota de 5 a 7.9: Bom
# • Nota de 8 a 9.9: Muito bom
# • Nota 10: Excelente

nota = float(input("Digite a nota (0 a 10): "))

match(int(nota)):
    case 0:
        print("Insuficiente!")
    case 1:
        print("Insuficiente!")
    case 2:
        print("Insuficiente!")
    case 3:
        print("Insuficiente!")
    case 4:
        print("Insuficiente!")
    case 5:
        print("Bom!")
    case 6:
        print("Bom!")
    case 7:
        print("Bom!")
    case 8:
        print("Muito bom!")
    case 9:
        print("Muito bom!")
    case 10:
        print("Excelente!")
    case _:
        print("Nota inválida.")