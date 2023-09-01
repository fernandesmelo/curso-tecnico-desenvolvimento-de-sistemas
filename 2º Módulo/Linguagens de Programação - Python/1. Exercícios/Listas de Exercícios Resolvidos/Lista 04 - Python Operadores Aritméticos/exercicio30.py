# 30. Escreva um programa que solicite ao usuário um número e exiba se ele é
# primo ou não (um número é primo se é divisível apenas por 1 e por ele
# mesmo).

num = int(input("Digite um número: "))

if num == 2:
    print(num, "é primo.")
    exit()

if num % 2 == 0 or num == 1:
    print(num, "não é primo.")
    exit()

for i in range(3, int(num ** 0.5) + 1, 2):
    if num % i == 0:
        print(num, "não é primo.")
        exit()

print(num, "é primo.")
