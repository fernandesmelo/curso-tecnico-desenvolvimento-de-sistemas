# 33. Como criar uma lista a partir de uma lista de strings em Python?

lista_strings = ['maçã', 'banana', 'laranja']
lista_resultante = []

for string in lista_strings:
    lista_resultante.append(len(string))

print(lista_resultante)  
