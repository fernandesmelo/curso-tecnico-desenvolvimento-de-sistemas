// Leia 2 valores com uma casa decimal (X e y), que devem representar as coordenadas de um ponto em um plano. A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (X = y = 0).

// Se o ponto estiver na origem, escreva a mensagem "Origem".

// Se o ponto estiver sobre um dos eixos escreva "Eixo X" ou "Eixo Y", conforme for a situação.

// Exemplos:
// Entrada:        Saída:
// 4.5 - 2.2       Q4

using System;

class Program
{
    static void Main()
    {
        Console.Write("Digite a coordenada X: ");
        double x = double.Parse(Console.ReadLine());

        Console.Write("Digite a coordenada Y: ");
        double y = double.Parse(Console.ReadLine());

        if (x == 0 && y == 0)
        {
            Console.WriteLine("Origem");
        }
        else if (x == 0)
        {
            Console.WriteLine("Eixo Y");
        }
        else if (y == 0)
        {
            Console.WriteLine("Eixo X");
        }
        else
        {
            if (x > 0)
            {
                if (y > 0)
                {
                    Console.WriteLine("Q1");
                }
                else
                {
                    Console.WriteLine("Q4");
                }
            }
            else
            {
                if (y > 0)
                {
                    Console.WriteLine("Q2");
                }
                else
                {
                    Console.WriteLine("Q3");
                }
            }
        }
    }
}
