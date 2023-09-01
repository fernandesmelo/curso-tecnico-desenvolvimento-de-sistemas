# 5. Crie um programa que verifique se um número é divisível por 3 e por 5. Use a instrução
# IF.

num = int(input("Digite um número: "))

if num % 3 == 0 and num % 5 == 0:
    print("O número é divisível por 3 e por 5.")
else:
    print("O número não é divisível por 3 e por 5.")

