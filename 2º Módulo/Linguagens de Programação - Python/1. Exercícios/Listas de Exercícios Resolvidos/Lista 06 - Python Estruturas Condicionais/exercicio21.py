# 21. Faça um programa que leia um número de 1 a 5 e imprima uma mensagem
# correspondente. Por exemplo, se o usuário digitar 1, o programa deve imprimir "Muito
# ruim". Se o usuário digitar 5, o programa deve imprimir "Excelente". Use a instrução
# MATCH.

num = int(input("Digite um número de 1 a 5: "))

match(num):
    case 1:
        print("Muito ruim")
    case 2:
        print("Ruim")
    case 3: 
        print("Regular")
    case 4:
        print("Bom")
    case 5:
        print("Excelente")
    case _:
        print("Número inválido")