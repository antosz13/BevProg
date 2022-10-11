from operator import concat


class Fejlesztok:
    def __init__(self, nev, fizu, ev = 0, rang = "junior"):
        self.nev = nev
        self.rang = rang
        self.ev = ev
        self.fizu = fizu
    
    def Raise(self, amount = 10000):
        self.fizu += amount

    def Year(self):
        self.ev += 1
        
    def Rang(self):
        if self.ev < 1:
            self.rang = "Intern"
        elif self.ev < 3:
            self.rang = "Junior"
        elif self.ev < 5:
            self.rang = "Medior"
        elif self.ev >= 5:
            self.rang = "Senior"    
    
    
def main ():
    f = Fejlesztok("Zoli", 10000,)
    f.Raise(50000)
    f.Raise()
    f.Year()
    f.Year()
    f.Year()
    f.Year()
    f.Rang()
    print(f.nev, f.fizu, f.ev, f.rang)

if __name__ == "__main__":
    main()