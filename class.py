class Bankszamla:
    def __init__(self, nev, egyenleg) -> None:
        self.dupont = 1000
        self.nev = nev
        self.egyenleg = egyenleg
    
    def betesz(self, osszeg):
        self.egyenleg += osszeg
    def kivesz(self, osszeg):
        if osszeg > self.egyenleg:
            print("nincs egyenleg")
        else:
            self.egyenleg -= osszeg
    def kiiras(self):
        print("tulaj: {0}, osszeg: {1}".format(self.nev, self.egyenleg))
        
def main():
    b1 = Bankszamla("Jani", 600)
    b1.kivesz(200)
    b1.kiiras()


if __name__ == "__main__":
    main()