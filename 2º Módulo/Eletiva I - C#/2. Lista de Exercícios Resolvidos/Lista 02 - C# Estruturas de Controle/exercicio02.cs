// Fazer um programa para ler um número inteiro e dizer se este número é par ou ímpar.

// Exemplos:
// Entrada:       Saída:
// 12             PAR

using System;

class Program
{
    static void Main()
    {
        Console.Write("Digite um número inteiro: ");
        int numero = int.Parse(Console.ReadLine());

        if (numero % 2 == 0)
        {
            Console.WriteLine("PAR");
        }
        else
        {
            Console.WriteLine("ÍMPAR");
        }
    }
}
