# 37. Escreva um programa que solicite ao usuário sua idade e se ele é estudante
# (responda com S ou N). Exiba se ele tem direito à meia-entrada no cinema
# (condição: idade menor que 18 ou maior que 60 anos OU ser estudante).

idade = int(input("Qual é a sua idade? "))
estudante = input("Você é estudante? (S/N) ").upper()

if idade < 18 or idade > 60 or estudante == "S":
    print("Você tem direito à meia-entrada no cinema.")
else:
    print("Você não tem direito à meia-entrada no cinema.")
