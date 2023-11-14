// Fazer um programa para ler um número inteiro, e depois dizer se este número é negativo ou não.

// Exemplos:                   
// Entrada:           Saída:
// - 10               NEGATIVO 

using System;

class Program
{
    static void Main()
    {
        Console.Write("Digite um número inteiro: ");
        int numero = int.Parse(Console.ReadLine());

        if (numero < 0)
        {
            Console.WriteLine("NEGATIVO");
        }
        else
        {
            Console.WriteLine("NÃO NEGATIVO");
        }
    }
}
