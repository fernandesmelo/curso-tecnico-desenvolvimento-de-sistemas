// Fazer um programa para ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Calcule e mostre o valor a ser pago. 

// Exemplos:
// Entrada:       Saída:
// 12 1 5.30      VALOR A PAGAR: R$ 15.50
// 16 2 5.10

using System;

class Program
{
    static void Main()
    {
        string[] peca1 = Console.ReadLine().Split(' ');
        int codigoPeca1 = int.Parse(peca1[0]);
        int numeroPecas1 = int.Parse(peca1[1]);
        double valorUnitarioPeca1 = double.Parse(peca1[2]);

        string[] peca2 = Console.ReadLine().Split(' ');
        int codigoPeca2 = int.Parse(peca2[0]);
        int numeroPecas2 = int.Parse(peca2[1]);
        double valorUnitarioPeca2 = double.Parse(peca2[2]);

        double totalPeca1 = numeroPecas1 * valorUnitarioPeca1;
        double totalPeca2 = numeroPecas2 * valorUnitarioPeca2;
        double valorTotal = totalPeca1 + totalPeca2;

        Console.WriteLine($"VALOR A PAGAR: R$ {valorTotal:F2}");
    }
}
