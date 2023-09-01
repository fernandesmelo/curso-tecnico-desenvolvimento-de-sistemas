# Desafio de Contagem de Vogais:

# Utilizando a linguagem de programação Python, crie um algoritmo que receba uma string como entrada e 
# retorne o número de vogais presentes nessa string.

texto = input("Escreva um texto ou palavra: ")  # Solicita ao usuário que digite um texto ou palavra e armazena na variável "texto".

listaVogais = ['a', 'e', 'i', 'o', 'u']  # Cria uma lista com as vogais.

contadorVogais = 0  # Inicializa uma variável para contar o número de vogais.

for letra in texto:  # Percorre cada letra do texto.
    if letra in listaVogais:  # Verifica se a letra está presente na lista de vogais.
        contadorVogais += 1  # Incrementa o contador de vogais.

print("Existem", contadorVogais, "vogais no seu texto.")  # Imprime o número de vogais encontrado na variável "contadorVogais".
