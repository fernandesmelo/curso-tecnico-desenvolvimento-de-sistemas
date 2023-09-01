# 37. Como adicionar elementos de uma lista a outra lista em Python? 

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

lista1.extend(lista2)

print(lista1)  

lista3 = [7, 8, 9]

lista4 = lista1 + lista3

print(lista4)  
