# Desafio de Verificação de Anagramas:

# Utilizando a linguagem de programação Python, escreva um algoritmo que receba duas strings como entrada e 
# verifique se elas são anagramas, ou seja, se uma pode ser obtida a partir da outra por rearranjo das letras.
# Ex.: america e iracema são anagramas.

texto1 = input("Escreva uma palavra ou frase: ")  # Solicita ao usuário que digite a primeira palavra ou frase e armazena em "texto1".
texto2 = input("Escreva uma palavra ou frase: ")  # Solicita ao usuário que digite a segunda palavra ou frase e armazena em "texto2".

if sorted(texto1) == sorted(texto2):  # Compara se as listas de caracteres das palavras/frases ordenadas são iguais.
    print("São anagramas.")  # Se as palavras/frases são anagramas, exibe a mensagem "São anagramas.".
else:
    print("Não são anagramas.")  # Se as palavras/frases não são anagramas, exibe a mensagem "Não são anagramas.".



