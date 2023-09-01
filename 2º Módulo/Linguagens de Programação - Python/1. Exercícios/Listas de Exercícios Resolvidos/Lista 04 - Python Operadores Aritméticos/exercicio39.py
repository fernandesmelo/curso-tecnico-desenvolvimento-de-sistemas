# 39. Escreva um programa que solicite ao usuário uma letra e exiba se ela é
# uma letra maiúscula OU uma letra minúscula.

letra = input("Digite uma letra: ")

if letra.isupper():
    print("A letra é maiúscula.")
elif letra.islower():
    print("A letra é minúscula.")
else:
    print("Não é uma letra.")
