# 32. Como criar uma lista de números ímpares em Python? 

numeros_impares = []

for i in range(1, 11):
    if i % 2 != 0:
        numeros_impares.append(i)

print(numeros_impares) 