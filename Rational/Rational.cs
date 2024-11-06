using System;
using System.Globalization;
using System.Reflection.Metadata.Ecma335;

namespace RationalNamespace;

public class Rational
{
  public int Numerator {get; set;}
  public int Denominator{get; set;}
  public Rational()
  {
    Numerator = 0;
    Denominator = 1;
  }
  public Rational(int Numerator, int Denominator)
  {
    if (Denominator == 0)
    throw new DivideByZeroException("Denominator cannot be zero");
        this.Numerator = Numerator;
        this.Denominator = Denominator;
  }
  public void WriteRational() => Console.WriteLine($"{Numerator} / {Denominator}");
  public void Negate() => Numerator = -Numerator;
  public void Invert()
  {
    if (Numerator == 0)
    throw new InvalidOperationException("Cannot invert a rational number with numerator zero.");
    int temp = Numerator;
    Numerator = Denominator;
    Denominator = temp;
  }
  public double ToDouble()
  {
    return (double)Numerator / Denominator;
  }
public Rational Reduce()
        {
            
            int gcd = GCD(Math.Abs(Numerator), Math.Abs(Denominator));

            int reducedNumerator = Numerator / gcd;
            int reducedDenominator = Denominator / gcd;

            if (reducedDenominator < 0)
            {
                reducedNumerator = -reducedNumerator;
                reducedDenominator = -reducedDenominator;
            }

            return new Rational(reducedNumerator, reducedDenominator);
        }

        private static int GCD(int a, int b)
        {
            if (b == 0)
                return a;
            return GCD(b, a % b);
        }
    public static Rational Add(Rational r1, Rational r2)
    {
        int newNumerator = r1.Numerator * r2.Denominator + r2.Numerator * r1.Denominator;
        int newDenominator = r1.Denominator * r2.Denominator;
        Rational sum = new Rational(newNumerator, newDenominator);
        return sum.Reduce();
    }
}
