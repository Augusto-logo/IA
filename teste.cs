using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Wesley
{
    internal class Individuo
    {
        public int[] bit;
        public int tam;
        public double fenotipo;
        public double x;
        public double a; 
        public double b;
        public double c;
        public double min;
        public double max;
        public double adaptabilidade;
        public static Random random = new Random();  

        public double Adaptabilidade => adaptabilidade;  

        public Individuo(int tam, double a, double b, double c, double min, double max)
        {
            this.tam = tam;
            this.a = a;
            this.b = b;
            this.c = c;
            this.min = min; // Inicialização do campo min
            this.max = max; // Inicialização do campo max
            bit = new int[tam];
            InicializarBitArray();
            ConverterDecimal();
            CalcularValorDeX();
            CalcularFitness();
        }

        private void InicializarBitArray()
        {
            for (int i = 0; i < tam; i++)
            {
                bit[i] = random.Next(0, 2);
            }
        }

        private void ConverterDecimal()
        {
            double result = 0;
            for (int i = 0; i < tam; i++)
            {
                result += bit[i] * Math.Pow(2, tam - i - 1);
            }
            fenotipo = result;
        }

        private void CalcularValorDeX()
        {
            x = min + (max-min) * (fenotipo / (Math.Pow(2, tam) - 1));
        }

        private void CalcularFitness()
        {
            adaptabilidade = (a*(x * x)) + (b * x) + c;
        }
        public void Mutar(double taxaDeMutacao)
        {
            for (int i = 0; i < tam; i++)
            {
                if (random.NextDouble() < taxaDeMutacao)
                {
                    bit[i] = 1 - bit[i];
                }
            }
            ConverterDecimal();
            CalcularValorDeX();
            CalcularFitness();
        }
        public void Imprimir()
        {
            foreach (var b in bit)
            {
                Console.Write(b + " ");
            }
            Console.WriteLine("\nFenotipo: " + fenotipo);
            Console.WriteLine("Valor de X: " + x);
            Console.WriteLine("Adaptabilidade: " + adaptabilidade);
        }
    }

}