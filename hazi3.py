
from cmath import pi


def fTeglalap(a, b):
    return(a*b)
def fKor(r):
    return(r**2*pi)


def fFibonacchi(n):
    li = [0, 1]
    for i in range(n):
        li.append(int(li[i]+li[i + 1]))
    return(li[n-1])

    
def main():
    
    #1. feladat
    print(fKor(int(input("r= "))))
    print(fTeglalap(int(input("a= ")), int(input("b= "))))
    
    #nem ertelmes a feladatt szovege, nem tudom hogy kene megoldani
    
    
    
    #2. feladat
    print(fFibonacchi(int(input("n= "))))


    #3. feladat
    num = str(input("szam: "))
    tukorszam = 1
    
    for i in range(len(num)):
        
        if num[i] != num[-i-1]:
            tukorszam = 0

    if tukorszam == 1:
        print("tukorszam")
    elif tukorszam == 0:
        print("nem tukorszam")
        

if __name__ == "__main__":
    main()