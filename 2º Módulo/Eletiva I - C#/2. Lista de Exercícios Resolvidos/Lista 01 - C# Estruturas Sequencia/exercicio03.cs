// Fazer um programa para ler quatro valores inteiros A, B, C, e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENÇA = (A * B - C * D).

// Exemplos:
// Entrada:       Saída:
// 5              DIFERENÇA = - 26
// 6
// 7
// 8

using System;

class Program
{
    static void Main()
    {
        Console.Write("Digite o valor de A: ");
        int A = int.Parse(Console.ReadLine());

        Console.Write("Digite o valor de B: ");
        int B = int.Parse(Console.ReadLine());

        Console.Write("Digite o valor de C: ");
        int C = int.Parse(Console.ReadLine());

        Console.Write("Digite o valor de D: ");
        int D = int.Parse(Console.ReadLine());

        int diferenca = (A * B) - (C * D);

        Console.WriteLine($"DIFERENÇA = {diferenca}");
    }
}
