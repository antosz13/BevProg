def foo (a, b = 5 , c = 4):
    a = a + b - c
    return (a, b) #tupplet ad vissza/szamparokat/

def rec(a): #rekurziv fgv aka onmagat hivja meg
    if a < 1:
        return a
    return rec(a - 1)



def main():
    
    a = 6
    foo(a)
    print(a)
    
    
    
    
    
if __name__ == "__main__":
    main()