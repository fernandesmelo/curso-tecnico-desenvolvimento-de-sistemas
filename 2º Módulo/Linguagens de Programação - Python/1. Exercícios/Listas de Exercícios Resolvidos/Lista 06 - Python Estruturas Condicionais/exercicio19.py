# 19. Escreva um programa que leia uma letra do alfabeto e verifique se é uma vogal ou uma
# consoante. Use a instrução MATCH.

letra = str(input("Digite uma letra: "))

match(letra):
    case "a":
        print("A letra digitada é uma vogal.")
    case "e":
        print("A letra digitada é uma vogal.")
    case "i":
        print("A letra digitada é uma vogal.")
    case "o":
        print("A letra digitada é uma vogal.")
    case "u":
        print("A letra digitada é uma vogal.")
    case _:
        print("A letra digitada é uma consoante.")