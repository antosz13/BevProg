using System;
using System.IO;

string pathdesk = Environment.GetFolderPath(Environment.SpecialFolder.Desktop);
string path = pathdesk + "/kozos.txt";

Console.Write("Hány főt szeretne felvinni?");
int db = int.Parse(Console.ReadLine());

StreamWriter sw = new StreamWriter(path, true);
for (int i = 0; i < db; i++)
{

    Console.WriteLine("Adja meg az ember nevét: ");
    string a = Console.ReadLine();

    Console.WriteLine("Adja meg az ember korát: ");
    int b = int.Parse(Console.ReadLine());

    Console.WriteLine("Adja meg az ember nemét: ");
    string c = Console.ReadLine();

    sw.WriteLine($"{a}\n{b}\n{c}");
}
sw.Flush();
sw.Close();