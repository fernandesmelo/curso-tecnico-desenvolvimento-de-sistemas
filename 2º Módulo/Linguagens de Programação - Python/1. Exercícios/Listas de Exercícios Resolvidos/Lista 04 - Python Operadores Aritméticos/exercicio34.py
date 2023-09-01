# 34. Escreva um programa que solicite ao usuário uma letra e exiba se ela é
# uma vogal OU uma consoante.

letra = input("Digite uma letra: ")

if letra in "AEIOUaeiou":
    print("A letra é uma vogal.")
else:
    print("A letra é uma consoante.")
