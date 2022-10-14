from cmath import sqrt
from ctypes.wintypes import POINT

class Pont():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def distcoordinates(self, x, y):
        return sqrt((self.x - x)**2 + (self.y - y)**2)
    
    def distpoint(self, b):
        return sqrt((self.x - b.x)**2 + (self.y - b.y)**2)

    def __str__(self) -> str:
        return f"{0};{1}"
    def __repr__(self) -> str:
        return '({0};{1})'.format(self.x, self.y)
def elsosiknegyed(li: list):
    li = [p for p in li if (p.x > 0 and p.y > 0)]
    return li
    
def main():
    p = Pont(5, 4)
    b = Pont(6, 7)
    c = Pont(-5, 4)
    d = Pont(8, -3)
    e = Pont(-5,-7)
    print("az ön pontja {0}".format(p))
    print(p.distpoint(b))
    l = elsosiknegyed([b, c, d, e])
    print(l)
    

if __name__ == "__main__":
    main()