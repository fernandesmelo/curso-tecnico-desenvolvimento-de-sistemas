# 22. Escreva um programa que verifique se um número é par ou ímpar. Use a instrução
# MATCH.

num = int(input("Digite um número: "))

match(num % 2):
    case 0:
        print("O número", num, "é par.")
    case 1:
        print("O número", num, "é ímpar.")