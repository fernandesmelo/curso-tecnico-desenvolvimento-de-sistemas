// Faça um programa para ler dois valores inteiros, e depois mostrar na tela a soma desses números com uma mensagem explicativa, conforme exemplos.

// Exemplos:
// Entrada:        Saída:
// 10              SOMA = 40
// 30

using System;

class Program
{
    static void Main()
    {
        Console.Write("Digite o primeiro valor inteiro: ");
        int valor1 = int.Parse(Console.ReadLine());

        Console.Write("Digite o segundo valor inteiro: ");
        int valor2 = int.Parse(Console.ReadLine());

        int soma = valor1 + valor2;

        Console.WriteLine($"SOMA = {soma}");
    }
}
