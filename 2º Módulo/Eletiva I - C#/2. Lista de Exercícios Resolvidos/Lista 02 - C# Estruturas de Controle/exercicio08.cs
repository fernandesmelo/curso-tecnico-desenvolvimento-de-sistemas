// Em um país imaginário denominado Lisarb, todos os habitantes ficam felizes em pagar seus impostos, pois sabem que nele não existem políticos corruptos e os recursos arrecados são utilizados em benefício da população, sem qualquer desvio. A moeda deste país é o Rombus, cujo símbolo é o R$.

// Leia um valor com duas casas decimais, equivalente ao salário de uma pessoa de Lisarb. Em seguida, calcule e mostre o valor que esta pessoa deve pagar de Imposto de Renda, seguindo a tabela abaixo. 

// RENDA 			                IMPOSTO DE RENDA		
// e R$ 0.0 A R$ 2000,00			Isento		
// De R$ 2000,01 a R$ 3000,00		8%		
// De R$ 3000,01 a R$ 4500, 00 	    18%		
// Acima de R$ 4500,00			    28%

// Lembre que, se o salário for R$ 3002,00, a taxa que incide é de 8% apenas sobre R$ 1000,00, pois a faixa de salário que fica de R$ 0,00 até R$ 2000,00 é isenta de Imposto de Renda. No exemplo fornecido (abaixo), a taxa é de 8% sobre R$ 1000,00 + 18% sobre R$ 2,00, o que resulta em R$ 80,36 no total. O valor deve ser impresso com duas casas decimais. 

// Exemplos:
// Entrada:      Saída:
// 3002,00       R$ 80,36

using System;

class Program
{
    static void Main()
    {
        Console.Write("Digite o salário: R$ ");
        double salario = double.Parse(Console.ReadLine());

        double imposto;

        if (salario <= 2000.00)
        {
            imposto = 0.0;
        }
        else if (salario <= 3000.00)
        {
            imposto = (salario - 2000.00) * 0.08;
        }
        else if (salario <= 4500.00)
        {
            imposto = 1000.00 * 0.08 + (salario - 3000.00) * 0.18;
        }
        else
        {
            imposto = 1000.00 * 0.08 + 1500.00 * 0.18 + (salario - 4500.00) * 0.28;
        }

        Console.WriteLine($"Imposto de Renda: R$ {imposto:F2}");
    }
}

