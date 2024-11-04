// See https://aka.ms/new-console-template for more information
//using System;

//namespace SimpleClasses;

using SimpleClass;
using static SimpleClass.Truck;

public class Program
{
    public static void Main(string[] args)
    {
       var car = new Sedan("Honda Accord","Red", 2019, 5);
       var truck = new Truck("kenworth W990","Black", 2020, 50);
      car.DisplayInfo();
      truck.DisplayInfo();


        Person FirstPerson = new Person();
        FirstPerson.name = "John";
        FirstPerson.age = 25;
        Console.WriteLine("{0} {1}", FirstPerson.name, FirstPerson.age);

        Person SecondPerson = new Person(15,"Nick");
        Console.WriteLine("{0} {1}", SecondPerson.name, SecondPerson.age);
    }
}
 //class Car
/* {
    public required string Brand { get; set; }
    public required string Model { get; set; }
    public int Year { get; set; }
    public required string Color { get; set; }
 }*/

