// Escreva um programa para ler as coordenadas (X, Y) de uma quantidade indeterminada de pontos no sistema cartesiano. Para cada ponto escrever o quadrante a que ele pertence. O algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação sem escrever mensagem alguma). 

// Exemplo:           Saída:
// 2 2                Primeiro

using System;

class Program
{
    static void Main()
    {
        while (true)
        {
            Console.Write("Digite as coordenadas (X, Y) separadas por espaço: ");
            string[] coordenadas = Console.ReadLine().Split(' ');

            int x = int.Parse(coordenadas[0]);
            int y = int.Parse(coordenadas[1]);

            if (x == 0 || y == 0)
            {
                break;
            }

            if (x > 0)
            {
                if (y > 0)
                {
                    Console.WriteLine("Primeiro");
                }
                else
                {
                    Console.WriteLine("Quarto");
                }
            }
            else
            {
                if (y > 0)
                {
                    Console.WriteLine("Segundo");
                }
                else
                {
                    Console.WriteLine("Terceiro");
                }
            }
        }
    }
}
