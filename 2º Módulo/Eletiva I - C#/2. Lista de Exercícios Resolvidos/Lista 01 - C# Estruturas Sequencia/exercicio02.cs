// Faça um programa para ler o valor do raio de um círculo, e depois mostrar o valor da área deste círculo com quatro casas decimais conforme exemplos. 

// Fórmula da área: área = π. raio*2

// Considere o valor de π = 3.14159

// Exemplos:
// Entrada:       Saída:
// 2.00           A = 12.5664

using System;

class Program
{
    static void Main()
    {
        double pi = 3.14159;

        Console.Write("Digite o valor do raio do círculo: ");
        double raio = double.Parse(Console.ReadLine());

        double area = pi * Math.Pow(raio, 2);

        Console.WriteLine($"A = {area:F4}");
    }
}
