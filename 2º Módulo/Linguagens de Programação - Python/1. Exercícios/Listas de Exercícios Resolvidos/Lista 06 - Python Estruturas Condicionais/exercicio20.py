# 20. Crie um programa que receba um número de 1 a 7 e imprima o dia da semana
# correspondente. Use a instrução MATCH.

num = int(input("Digite um número de 1 a 7: "))

match(num):
    case 1:
         print("Domingo")
    case 2:
         print("Segunda-feira")
    case 3:
         print("Terça-feira")
    case 4:
         print("Quarta-feira")
    case 5:
         print("Quinta-feira")
    case 6:
        print("Sexta-feira")
    case 7:
         print("Sábado")
    case _:
         print("Número inválido")

