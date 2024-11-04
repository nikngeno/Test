using System;

namespace SimpleClass;

public class Car
{
    public string model;
    public string color;
    public int year;
public Car (string model, string color, int year)
{
 this.model = model;
 this.color = color;
 this.year = year;
}

public void DisplayModelColorYear()
{
    Console.WriteLine($"Model: {model}, Color: {color}, Year: {year}");
}
}

public class Truck : Car
{
private int load_capacity;
public Truck(string model, string color, int year, int capacity) : base (model, color,year) => load_capacity = capacity;
public void DisplayInfo()
    { DisplayModelColorYear();
    Console.WriteLine($"Load capacity: {load_capacity}");
}

public class Sedan : Car
{
private int seat_capacity;
        public Sedan(string model, string color, int year, int capacity) : base(model, color, year) => seat_capacity = capacity;
        public void DisplayInfo()
{
    DisplayModelColorYear();
    Console.WriteLine($"Seat capacity: {seat_capacity}");
}
}
}
