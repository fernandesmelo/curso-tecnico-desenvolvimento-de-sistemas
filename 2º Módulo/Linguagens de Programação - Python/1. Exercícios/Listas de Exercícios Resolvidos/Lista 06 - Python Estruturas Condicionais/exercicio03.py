# 3. Crie um programa que verifique se uma pessoa pode votar ou não. Considere que a
# pessoa pode votar se tiver mais de 18 anos. Use a instrução IF.

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você pode votar!")
else:
    print("Você ainda não pode votar.")
