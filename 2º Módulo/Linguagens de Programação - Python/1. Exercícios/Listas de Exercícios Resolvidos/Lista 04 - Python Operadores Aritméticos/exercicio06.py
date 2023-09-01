# 6. Escreva um programa que solicite ao usuário a quantidade de horas trabalhadas em um dia e o valor da hora 
# trabalhada, e exiba o salário diário. 

horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas em um dia: "))
valor_hora = float(input("Digite o valor da hora trabalhada: R$ "))

salario_diario = horas_trabalhadas * valor_hora

print("O seu salário diário é de R$ {:.2f}".format(salario_diario))
