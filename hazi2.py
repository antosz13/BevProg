from cmath import pi
from math import sqrt


def main():
    
    #elso feladat
    age = int(input("Your age: "))
    if age >= 21:
        print("U can buy alcohol in America & U can smoke in Hungary & U can get a licence in Hungary & U can watch Shrek 2")
    elif age >= 18:
        print("U can smoke in Hungary & U can get a licence in Hungary & U can watch Shrek 2")
    elif age >= 17:
        print("U can get a licence in Hungary & U can watch Shrek 2")
    elif age >= 12:
        print("U can watch Shrek 2")



    #masodik feladat
    #teglatest terfogat
    x = int(input("x= "))
    y = int(input("y= "))
    z = int(input("z= "))
    print("teglatest tefogata {} ". format(x*y*z))
    
    
    
    #pitagorasz tetel
    valtozo = input("valtozo/a,b,c/: ")
    
    if valtozo == 'a':
        b = int(input("b= "))    
        c = int(input("c= "))
        a = sqrt(c**2-b**2)
        print(a)
    
    elif valtozo == 'b':
        a = int(input("a= "))    
        c = int(input("c= "))
        b = sqrt(c**2-a**2)
        print(b)
        
    elif valtozo == 'c':
        b = int(input("b= "))    
        c = int(input("a= "))
        c = sqrt(a**2+b**2)
        print(c)
        
    
    
       
    #gömbtérfogata
    r = int(input("R= "))
    print("TGömb= ", (4*(r**3)*pi)/3)
    
    
    #harmadik feladat
    nadb = int(input("Na mennyiseg= "))
    cl2db = int(input("Cl2 mennyiseg= "))

    if nadb == cl2db*2 & nadb >= 2:
        print("{} db NaCl fejlődik".format(nadb))
    elif nadb >= cl2db*2:        
        print("{} db NaCl fejlodik es {} db Na marad".format(cl2db*2, nadb-(cl2db*2)))
    elif nadb <= cl2db*2:        
        print("{} db NaCl fejlodik es {} db Cl2 marad".format(nadb, cl2db-(nadb/2)))
    
        





if __name__ == "__main__":
    main()
