using System;

namespace CSC180;
using System;
public class Person // Parent class
{
    public string name;
    public int age;

    public Person()
    {
    }

    public Person(string name, int age) {
        this.name = name;
        this.age = age;
    }
    public void DisplayNameAge()
    { System.Console.WriteLine($"{name} is {age} years old."); }
}
public class Teacher : Person { // Child class 
    public string subject;

    public Teacher()
    {
    }

    public Teacher(string name, int age, string subject) : base(name, age)
    { this.subject = subject; }

    public void DisplayTeacher(){
        System.Console.WriteLine($"Name: {name}, Age: {age}, Subject: {subject}");
    }
}
public class Student : Person { // Child class
    public double gpa;

    public Student()
    {
    }

    public Student(string name, int age, double gpa) : base(name, age)
    { this.gpa = gpa; }
    public void DisplayStudent()
    {
        System.Console.WriteLine($"Name: {name}, Age: {age}, GPA: {gpa}");
    }
}


