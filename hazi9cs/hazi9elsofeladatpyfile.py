import os

class Ember:
    def __init__(self, nev, kor, nem) -> None:
        self.nev = nev
        self.kor = kor
        self.nem = nem

    def kiiras(self):
        print("neve: {0}, kora: {1}, neme: {2}".format(self.nev, self.kor, self.nem))

def main():
    
    pathdesk = os.path.normpath(os.path.expanduser("~/Desktop"))
    path = pathdesk + "\kozos.txt"
    # print(path)
    li = []
    try: 
        f = open(path, 'r')
        li = f.readlines()
    except FileNotFoundError:
        print("Nincs ember az adatbázisban!")

    
    if len(li) > 0:
        for i in range(len(li)):
            if i % 3 == 0:
                a = Ember(li[i].strip(), li[i+1].strip(), li[i+2].strip())
                print(f"{i//3 + 1}. ember: ")
                a.kiiras() 
                
            else:
                continue

if __name__ == "__main__":
    main()