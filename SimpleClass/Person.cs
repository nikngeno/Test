using System;

namespace SimpleClass;

public class Person
{
    private int _age;
    public int age
    {
        get { return _age; }
        set { _age = value; }
    }
 private string _name;
 public string name
{
    get {return _name;}
    set {_name = value;}
}
public Person()
{
 _age = 0;
 _name = "";
}
public Person(int age, string name)
{
    _age = age;
    _name = name;
}

}
