// Um posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes. Escreva um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma: 1. Álcool 2. Gasolina 3. Diesel 4. Fim). Caso o usuário informe um código inválido (fora da faixa de 1 a 4 deve ser solicitado um novo código (até que seja válido). O programa será encerrado quando o código informado for o número 4. Deve ser escrito a mensagem: "MUITO OBRIGADO" e a quantidade de clientes que abstaceram cada tipo de combustível, conforme exemplo. 

// Exemplo:
// Entrada:          Saída: 
// 8                 MUITO OBRIGADO 
// 1                 Álcool: 1
// 7                 Gasolina: 2
// 2                 Diesel: 0

using System;

class Program
{
    static void Main()
    {
        int alcool = 0, gasolina = 0, diesel = 0;

        while (true)
        {
            Console.WriteLine("Informe o tipo de combustível:");
            Console.WriteLine("1. Álcool");
            Console.WriteLine("2. Gasolina");
            Console.WriteLine("3. Diesel");
            Console.WriteLine("4. Fim");

            int escolha = int.Parse(Console.ReadLine());

            switch (escolha)
            {
                case 1:
                    alcool++;
                    break;
                case 2:
                    gasolina++;
                    break;
                case 3:
                    diesel++;
                    break;
                case 4:
                    Console.WriteLine("MUITO OBRIGADO");
                    Console.WriteLine($"Álcool: {alcool}");
                    Console.WriteLine($"Gasolina: {gasolina}");
                    Console.WriteLine($"Diesel: {diesel}");
                    return;
                default:
                    Console.WriteLine("Código inválido. Tente novamente.");
                    break;
            }
        }
    }
}
