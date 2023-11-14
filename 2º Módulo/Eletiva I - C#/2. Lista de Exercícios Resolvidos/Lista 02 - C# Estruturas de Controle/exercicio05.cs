// Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

// CÓDIGO 	ESPECIFICAÇÃO 	PREÇO	
// 1		Cachorro Quente R$ 4,00	
// 2		X-Salada		R$ 4,50	
// 3		X-Bacon		    R$ 5,00	
// 4		Torrada Simples	R$ 2,00	
// 5		Refrigerante 	R$ 1,50

// Exemplos:
// Entrada:        Saída:
// 3 2             Total: R$ 10.00

using System;

class Program
{
    static void Main()
    {
        Console.Write("Digite o código do item: ");
        int codigo = int.Parse(Console.ReadLine());

        Console.Write("Digite a quantidade desejada: ");
        int quantidade = int.Parse(Console.ReadLine());

        double preco = 0.0;

        switch (codigo)
        {
            case 1:
                preco = 4.00;
                break;
            case 2:
                preco = 4.50;
                break;
            case 3:
                preco = 5.00;
                break;
            case 4:
                preco = 2.00;
                break;
            case 5:
                preco = 1.50;
                break;
            default:
                Console.WriteLine("Código inválido.");
                return;
        }

        double total = preco * quantidade;

        Console.WriteLine($"Total: R$ {total:F2}");
    }
}
