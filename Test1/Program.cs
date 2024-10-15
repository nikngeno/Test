// See https://aka.ms/new-console-template for more information
//Console.WriteLine("Hello, World!");
﻿namespace PlayWithStrings
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string abc = "abcefghi";

            int count = 0;
            for (int i = 0; i < abc.Length; i++)
            {
                Console.Write(count);
                Console.Write(abc[i]);
                count++;

            }

            Console.WriteLine();
            string name1 = "Alan Turing";
            string name2 = "Ada Lovelace";
            int flag = name1.CompareTo(name2);
            if (flag == 0)
            {
                Console.WriteLine("The names are the same.");
            }
            else if (flag < 0)
            {
                Console.WriteLine($"{name1} comes before {name2}.");
            }
            else //if (flag > 0)
            {
                Console.WriteLine($"{name2} comes before {name1}");
            }


        }
    }
}
