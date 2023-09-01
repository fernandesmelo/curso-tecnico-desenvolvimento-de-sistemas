# 16. Escreva um programa que verifique se um número está dentro de um intervalo. O
# intervalo é definido pelos números 5 e 10. Use a instrução ELIF.

num = int(input("Digite um número: "))

if num < 5:
    print("O número está abaixo do intervalo.")
elif num > 10:
    print("O número está acima do intervalo.")
else:
    print("O número está dentro do intervalo.")
