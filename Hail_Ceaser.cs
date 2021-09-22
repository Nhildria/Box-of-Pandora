using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp7
{
    class Program
    {
        static void Main(string[] args)
        {

            Console.Title = "Ceaser Cypher";

            Console.WriteLine("Enter Message");

            string Message = Console.ReadLine();

            int key = 0;

            try
            {
                Console.WriteLine("Enter A Key : ");

                key = Convert.ToInt32(Console.ReadLine());
            }


            catch (Exception exp)
            {
                Console.WriteLine();
                Console.WriteLine("Key  Must be type : Integer ");
                Console.WriteLine(exp.StackTrace);

            }

            char[] Character = new char[Message.Length];


            for (int i = 0; i < Character.Length; i++)
                Character[i] = Message[i];

            int temp = 0;
            
            for (int j = 0; j < Character.Length; j++)
            {

                temp = Message[j] + key;

                if (temp > 'z')
                {
                    temp -= 26;
                }
                else if (temp < 'a')
                {
                    temp += 26;
                }

                Character[j] = (char)temp;

            }

            Console.WriteLine("Encoded Message");
            Console.WriteLine(Character) ;

            Console.ReadLine();



        }
    }
}
