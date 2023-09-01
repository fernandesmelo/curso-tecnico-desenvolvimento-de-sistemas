# 27. Escreva um programa que solicite ao usuário uma letra e exiba se ela é
# uma vogal ou uma consoante.

letra = input("Digite uma letra: ")

if letra in "aeiouAEIOU":
    print("A letra digitada é uma vogal.")
else:
    print("A letra digitada é uma consoante.")

