// See https://aka.ms/new-console-template for more information
//using System;

//namespace SimpleClasses;

using SimpleClass;

public class Program
{
    public static void Main(string[] args)
    {
        Car myCar = new()
        {
            Color = "Red",
            Year = 2020,
            Brand = "Toyota",
            Model = "Camry"
        };

        Console.WriteLine("{0} {1} {2} {3}" ,myCar.Color,myCar.Year,myCar.Brand,myCar.Model);

        Person FirstPerson = new Person();
        FirstPerson.name = "John";
        FirstPerson.age = 25;
        Console.WriteLine("{0} {1}", FirstPerson.name, FirstPerson.age);

        Person SecondPerson = new Person(15,"Nick");
        Console.WriteLine("{0} {1}", SecondPerson.name, SecondPerson.age);
    }
}
 class Car
 {
    public required string Brand { get; set; }
    public required string Model { get; set; }
    public int Year { get; set; }
    public required string Color { get; set; }
 }

