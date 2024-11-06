// See https://aka.ms/new-console-template for more information
using System;
using System.IO;

class Program
{
    static void Main(string[] args)
    {
        if (args.Length != 2)
        {
            Console.WriteLine("Usage: Program.exe <InputFilePath> <OutputFilePath>");
            return;
        }

        string inputFilePath = args[0];
        string outputFilePath = args[1];

        
        if (!File.Exists(inputFilePath))
        {
            Console.WriteLine($"Error: The file '{inputFilePath}' does not exist.");
            return;
        }

        try
        {
            
            using (StreamReader reader = new StreamReader(inputFilePath))
            {
                
                using (StreamWriter writer = new StreamWriter(outputFilePath))
                {
                    string line;
                    int lineNumber = 1;

                    
                    while ((line = reader.ReadLine()) != null)
                    {
                        
                        writer.WriteLine($"{lineNumber}: {line}");
                        lineNumber++;
                    }
                }
            }

            Console.WriteLine($"Successfully wrote to '{outputFilePath}'.");
        }
        catch (Exception ex)
        {
            
            Console.WriteLine("An error occurred:");
            Console.WriteLine(ex.Message);
        }
    }
}

