# 12. Escreva um programa que receba um número de 1 a 7 e imprima o dia da semana
# correspondente. Use a instrução ELIF. 

numero = int(input("Digite um número de 1 a 7: "))

if numero == 1:
    print("Domingo")
elif numero == 2:
    print("Segunda-feira")
elif numero == 3:
    print("Terça-feira")
elif numero == 4:
    print("Quarta-feira")
elif numero == 5:
    print("Quinta-feira")
elif numero == 6:
    print("Sexta-feira")
elif numero == 7:
    print("Sábado")
else:
    print("Número inválido. Digite um número de 1 a 7.")
