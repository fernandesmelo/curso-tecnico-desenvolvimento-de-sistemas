// Fazer um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora é calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais. 

// Exemplos:
// Entrada:       Saída:
// 25             NUMBER = 25
// 100            SALARY = U$ 550.00
// 5.50

using System;

class Program
{
    static void Main()
    {
        Console.Write("Digite o número do funcionário: ");
        int numeroFuncionario = int.Parse(Console.ReadLine());

        Console.Write("Digite o número de horas trabalhadas: ");
        int horasTrabalhadas = int.Parse(Console.ReadLine());

        Console.Write("Digite o valor que recebe por hora: ");
        double valorPorHora = double.Parse(Console.ReadLine());

        double salario = horasTrabalhadas * valorPorHora;

        Console.WriteLine($"NUMBER = {numeroFuncionario}");
        Console.WriteLine($"SALARY = U$ {salario:F2}");
    }
}
