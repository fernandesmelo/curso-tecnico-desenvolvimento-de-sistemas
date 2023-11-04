// Fazer um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
// A) A área do triângulo retângulo que tem A por base e C por altura. 
// B) A área do círculo de raio C. (PI = 3.14159). 
// C) A área do trapézio que tem A e B por bases e C por altura.
// D) A área do quadrado que tem lado B. 
// E) A área do retângulo que tem lados A e B.

// Exemplos:
// Entrada:             Saída:
// 3.0 4.0 5.2          TRIÂNGULO: 7.800
//                      CÍRCULO: 84.949
//                      TRAPÉZIO: 18.200
//                      QUADRADO: 16.000
//                      RETÂNGULO: 12.000

using System;

class Program
{
    static void Main()
    {
        double A, B, C;
        string[] valores = Console.ReadLine().Split(' ');
        A = double.Parse(valores[0]);
        B = double.Parse(valores[1]);
        C = double.Parse(valores[2]);

        double areaTriangulo = 0.5 * A * C;
        double areaCirculo = 3.14159 * C * C;
        double areaTrapezio = 0.5 * (A + B) * C;
        double areaQuadrado = B * B;
        double areaRetangulo = A * B;

        Console.WriteLine($"TRIÂNGULO: {areaTriangulo:F3}");
        Console.WriteLine($"CÍRCULO: {areaCirculo:F3}");
        Console.WriteLine($"TRAPÉZIO: {areaTrapezio:F3}");
        Console.WriteLine($"QUADRADO: {areaQuadrado:F3}");
        Console.WriteLine($"RETÂNGULO: {areaRetangulo:F3}");
    }
}
