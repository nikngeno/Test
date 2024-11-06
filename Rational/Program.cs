// See https://aka.ms/new-console-template for more information
//Console.WriteLine("Hello, World!");
// Program.cs
using System;
using RationalNamespace;
using System.Collections.Generic;
public class Program
{
    public static void Main(string[] args)
    {
        Console.Write("Default Rational: ");
        
        var r1 = new Rational();
        r1.WriteRational();

        
        r1.Numerator = 3;
        r1.Denominator = 4;
        Console.Write("After setting values: ");
        r1.WriteRational();

        
        r1.Negate();
        Console.Write("After Negate: ");
        r1.WriteRational();

        
        r1.Invert();
        Console.Write("After Invert: ");
        r1.WriteRational();

        
        double value = r1.ToDouble();
        Console.WriteLine($"As double: {value}");

        
        Rational r2 = new Rational(8, 12);
        Console.Write("Before Reduce: ");
        r2.WriteRational();
        Rational reduced = r2.Reduce();
        Console.Write("After Reduce: ");
        reduced.WriteRational();

        
        Rational sum = Rational.Add(r1, r2);
        Console.Write("Sum of ");
        r1.WriteRational();
        Console.Write(" and ");
        r2.WriteRational();
        Console.Write(" is ");
        sum.WriteRational();
    }
}

