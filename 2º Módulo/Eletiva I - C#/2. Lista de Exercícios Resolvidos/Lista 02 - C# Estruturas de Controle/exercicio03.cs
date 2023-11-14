// Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "São Múltiplos" ou "Não são Múltiplos", indicando se os valores lindos são múltiplos entre si. Atenção: os números devem poder ser digitados em ordem crescente ou decrescente.

// Exemplos:
// Entrada:         Saída:
// 6 24             São múltiplos 

using System;

class Program
{
    static void Main()
    {
        Console.Write("Digite o primeiro valor inteiro: ");
        int A = int.Parse(Console.ReadLine());

        Console.Write("Digite o segundo valor inteiro: ");
        int B = int.Parse(Console.ReadLine());

        if ((A % B == 0) || (B % A == 0))
        {
            Console.WriteLine("São múltiplos");
        }
        else
        {
            Console.WriteLine("Não são múltiplos");
        }
    }
}
