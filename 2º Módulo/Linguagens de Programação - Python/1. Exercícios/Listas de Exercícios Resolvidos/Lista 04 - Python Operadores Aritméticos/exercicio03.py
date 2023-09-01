# 3. Escreva um programa que solicite ao usuário o raio de um círculo e exiba
# sua área e circunferência. (Dica: use a constante pi, que é aproximadamente igual a 3,14)

from math import pi

raio = float(input("Digite o raio do círculo: "))

area = pi * raio ** 2
circunferencia = 2 * pi * raio

print("A área do círculo é:", area)
print("A circunferência do círculo é:", circunferencia)

