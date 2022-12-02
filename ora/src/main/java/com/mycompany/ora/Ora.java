package com.mycompany.ora;
import java.util.Scanner;
import java.util.ArrayList;
/**
 * @author antosz13
 */
public class Ora 
{
    public static int szoroz(int a, int b)
    {
        return a*b;
    }
    
    public static void main(String[] args) 
    {
        System.out.println("Hello world");
        String name = "Gabi";
        char c = 'c';
        int a = 13;
        float b = (float)5.77;
        boolean g = true;
        String j = "54";
        int uj = Integer.parseInt(j);
        
        int p = 5, i = 7;
        double  x = i/(p*1.0);
        System.out.println(x);
        String teszt = "hello world";
        System.out.println(teszt.length());
        System.out.println(teszt.charAt(5));
        System.out.println(teszt.indexOf("wo"));
        System.out.println(teszt.substring(6, 8));
        double d = Math.pow(2, 5);
        System.out.println(d);
        int[] szamok2 = {1, 4, 6};
        for (int i = 0; i < 10; i++) 
        {
            
        }
        for (int i : szamok2) 
        {
            System.out.println(i);
        }
       
        int i1 = 5, i2 = 5;
        System.out.println(i1++);
        System.out.println(++i2);
        Scanner be = new Scanner(System.in);
        System.out.println("szam:");
        int szam  = be.nextInt();
        System.out.println("szoveg");
        String szoveg = be.nextLine();
        
        int[] szamtomb = new int [10];
        int[] tomb2 = {1, 5, 7, 3, 8};
        int [][] matrix = new int [8][8];
        ArrayList <String> szavak8 = new ArrayList<String>();
        szavak8.add("alma");
        szavak8.add("korte");
        System.out.println(szavak8.contains("Peti"));
        System.out.println(szavak8.size());
        System.out.println(szavak8.toString());
        
        System.out.println(szoroz(6, 5));
        
    }
}
