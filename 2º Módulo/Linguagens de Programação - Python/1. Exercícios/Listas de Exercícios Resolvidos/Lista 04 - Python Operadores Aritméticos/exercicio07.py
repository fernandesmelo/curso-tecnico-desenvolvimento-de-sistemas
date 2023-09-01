# 7. Escreva um programa que solicite ao usuário a idade de uma pessoa em
# anos e exiba a idade em meses e em dias. (Dica: um ano tem 12 meses e
# um mês tem aproximadamente 30 dias)

idade_anos = int(input("Digite a idade em anos: "))

idade_meses = idade_anos * 12
idade_dias = idade_anos * 365

print("Idade em meses:", idade_meses)
print("Idade em dias:", idade_dias)
