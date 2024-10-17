// See https://aka.ms/new-console-template for more information
//using System;

//namespace SimpleClasses;

public class Program
{
    static void Main(string[] args)
    {
        Car myCar = new Car();
        myCar.Color = "Red";
        myCar.Year = 2020;
        myCar.Brand = "Toyota";
        myCar.Model = "Camry";

        Console.WriteLine("{0} {1} {2} {3}" ,myCar.Color,myCar.Year,myCar.Brand,myCar.Model);
    }
}
 class Car
 {
    public string Brand { get; set; }
    public string Model { get; set; }
    public int Year { get; set; }
    public string Color { get; set; }
 }

