# 9. Escreva um programa que solicite ao usuário o valor de um empréstimo, a
# taxa de juros mensal e o número de meses do empréstimo, e exiba o valor
# total a ser pago (incluindo juros).

valor_emprestimo = float(input("Valor do empréstimo: "))
taxa_juros = float(input("Taxa de juros mensal (em decimal): "))
numero_meses = int(input("Número de meses do empréstimo: "))

valor_total = valor_emprestimo * (1 + taxa_juros) ** numero_meses

print(f"Valor total a ser pago: R$ {valor_total:.2f}")
