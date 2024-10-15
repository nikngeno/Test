// See https://aka.ms/new-console-template for more information
//Console.WriteLine("Hello, World!");
﻿using System.Text;

namespace StringFormat
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string myString = "My \"so-called\" life\n is fun";
            string myString2 = "Go to your c:\\ drive";
            string myString3 = @"Go to your c:\ drive";

            string myString4 = string.Format("{0:C}", 123.45);
            string myString5 = string.Format("{0:N}", 10030000000);
            string myString6 = string.Format("Percentage {0:P}", .05);

            string customMystring = string.Format("Phone Number {0:(###) ###-####}", 2536712346);

            string lyric = " That summer we took to them streets ";
            lyric = string.Format("length before: {0} -- Length after: {1}", lyric.Length,lyric.Trim().Length);
            //lyric = lyric.Replace(" ", "--");

            StringBuilder myString7 = new StringBuilder();
            for (int i = 0; i < 100; i++)
            {
                //myString6 += "--" + i.ToString();
                myString7.Append("--");
                myString7.Append(i);
            }

            Console.WriteLine(myString);
            Console.WriteLine(myString2);
            Console.WriteLine(myString3);
            Console.WriteLine(myString4);
            Console.WriteLine(myString5);
            Console.WriteLine(myString6);
            Console.WriteLine(customMystring);
            Console.WriteLine(lyric);
            Console.WriteLine(myString7);
            Console.ReadLine();
        }
    }
}
