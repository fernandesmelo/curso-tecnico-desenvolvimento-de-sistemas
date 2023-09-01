# 20. Como ordenar uma lista com base em uma função personalizada em Python?

lista = [4, 2, 8, 3, 6, 1, 5, 7]

def minha_funcao(elemento):
    return abs(elemento)

lista_ordenada = sorted(lista, key=minha_funcao)

print(lista_ordenada)

