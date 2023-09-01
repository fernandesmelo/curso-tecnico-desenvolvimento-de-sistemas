# 4. Escreva um programa que solicite ao usuário o valor de uma compra e
# calcule o valor final da compra com um desconto de 10%.

valor_compra = float(input("Digite o valor da compra: R$ ")) 

desconto = valor_compra * 0.1 
valor_final = valor_compra - desconto 

print(f"O valor final da compra com desconto é R$ {valor_final:.2f}") 

