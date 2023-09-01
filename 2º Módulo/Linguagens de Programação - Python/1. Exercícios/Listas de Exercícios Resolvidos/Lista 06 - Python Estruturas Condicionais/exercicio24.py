# 24. Faça um programa que leia uma letra do alfabeto e verifique se é uma vogal, uma
# consoante ou outro caractere. Use a instrução MATCH.

letra = str(input("Digite uma letra: "))

match(letra):
    case "a":
        print("Essa letra é uma vogal.")
    case "e":
        print("Essa letra é uma vogal.")
    case "i":
        print("Essa letra é uma vogal.")
    case "o":
        print("Essa letra é uma vogal.")
    case "u":
        print("Essa letra é uma vogal.")
    case "b":
        print("Essa letra é uma consoante.")
    case "c":
        print("Essa letra é uma consoante.")
    case "d":
        print("Essa letra é uma consoante.")
    case "f":
        print("Essa letra é uma consoante.")
    case "g":
        print("Essa letra é uma consoante.")
    case "h":
        print("Essa letra é uma consoante.")
    case "j":
        print("Essa letra é uma consoante.")
    case "k":
        print("Essa letra é uma consoante.")
    case "l":
        print("Essa letra é uma consoante.")
    case "m":
        print("Essa letra é uma consoante.")
    case "n":
        print("Essa letra é uma consoante.")
    case "p":
        print("Essa letra é uma consoante.")
    case "q":
        print("Essa letra é uma consoante.")
    case "r":
        print("Essa letra é uma consoante.")
    case "s":
        print("Essa letra é uma consoante.")
    case "t":
        print("Essa letra é uma consoante.")
    case "v":
        print("Essa letra é uma consoante.")
    case "w":
        print("Essa letra é uma consoante.")
    case "x":
        print("Essa letra é uma consoante.")
    case "y":
        print("Essa letra é uma consoante.")
    case "z":
        print("Essa letra é uma consoante.")
    case _:
        print("Isso é outro caractere.")