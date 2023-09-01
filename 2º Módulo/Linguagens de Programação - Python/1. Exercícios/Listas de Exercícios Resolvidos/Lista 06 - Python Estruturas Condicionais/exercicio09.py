# 9. Escreva um programa que receba dois números e verifique se o primeiro é múltiplo do
# segundo. Use a instrução IF/ELSE.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 % num2 == 0:
    print(num1, "é múltiplo de", num2)
else:
    print(num1, "não é múltiplo de", num2)
