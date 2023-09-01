# 14. Escreva um programa que receba o nome de uma fruta e imprima sua cor. Considere as
# frutas maçã (vermelha), banana (amarela) e uva (roxa). Use a instrução ELIF.

fruta = input("Digite o nome de uma fruta: ")

if fruta.lower() == "maçã":
    print("A cor da maçã é vermelha.")
elif fruta.lower() == "banana":
    print("A cor da banana é amarela.")
elif fruta.lower() == "uva":
    print("A cor da uva é roxa.")
else:
    print("Fruta desconhecida.")

