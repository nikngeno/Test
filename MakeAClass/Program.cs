// See https://aka.ms/new-console-template for more information
Console.WriteLine(FactorialNumber(10));
static int FactorialNumber(int n)
{
  if (n == 1)
  {
    return 1;
  }
  else
  {
    return n * FactorialNumber(n - 1);
  }
}