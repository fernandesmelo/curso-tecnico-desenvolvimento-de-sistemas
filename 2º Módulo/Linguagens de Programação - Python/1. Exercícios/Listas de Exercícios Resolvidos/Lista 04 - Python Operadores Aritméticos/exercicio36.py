# 36. Escreva um programa que solicite ao usuário duas palavras e exiba se
# ambas têm o mesmo número de caracteres OU se a primeira palavra é
# maior que a segunda.

palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

if len(palavra1) == len(palavra2):
    print("As duas palavras têm o mesmo número de caracteres.")
elif len(palavra1) > len(palavra2):
    print("A primeira palavra é maior que a segunda.")
else:
    print("A segunda palavra é maior que a primeira")
