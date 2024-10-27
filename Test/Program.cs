// See https://aka.ms/new-console-template for more information
//Console.WriteLine("Hello, World!");
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Test
{
    public class Program
    {
        static void Main(string[] args)
        {
            int a = 1;
            int z = 2;
            string b = "Nick";
            string y = "Ngeno";
            char c = 'A';
            char w = 'B';
            decimal d = 1.095M;
            float e = 0.9F;
            long f = 1000000000000;
            byte g = 255;
            double h = 3.1415;
            bool j = true;

            Console.WriteLine(a + b);
            Console.WriteLine(c + d);
            Console.WriteLine(e + f);
            Console.WriteLine(g + h);
            Console.WriteLine((j + b).GetType());
            Console.WriteLine(a + b);
            Console.WriteLine((a + b).GetType());

            //Console.WriteLine("Hello, World!");
        }
    }
}
