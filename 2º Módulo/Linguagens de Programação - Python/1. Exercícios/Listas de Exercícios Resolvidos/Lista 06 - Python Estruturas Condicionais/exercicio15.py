# 15. Faça um programa que leia um número de 1 a 5 e imprima uma mensagem
# correspondente. Por exemplo, se o usuário digitar 1, o programa deve imprimir "Muito
# ruim". Se o usuário digitar 5, o programa deve imprimir "Excelente". Use a instrução
# ELIF.

numero = int(input("Digite um número de 1 a 5: "))

if numero == 1:
    print("Muito ruim")
elif numero == 2:
    print("Ruim")
elif numero == 3:
    print("Regular")
elif numero == 4:
    print("Bom")
elif numero == 5:
    print("Excelente")
else:
    print("Número inválido.")
