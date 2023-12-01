// Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada leitura de senha incorreto informada, escrever a mensagem "Senha Inválida". Quando a senha for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo encerrado. Considere que a senha correta é o valor 2002.

// Exemplo:
// Entrada:       Saída:
// 2200           Senha Inválida 

using System;

class Program
{
    static void Main()
    {
        int senhaCorreta = 2002;

        while (true)
        {
            Console.Write("Digite a senha: ");
            int senhaDigitada = int.Parse(Console.ReadLine());

            if (senhaDigitada == senhaCorreta)
            {
                Console.WriteLine("Acesso Permitido");
                break;
            }
            else
            {
                Console.WriteLine("Senha Inválida");
            }
        }
    }
}
