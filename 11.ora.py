import random
class Verem(list):
    def betesz(self, elem):
        self.append(elem)
    def meret(self):
        return (len(self))
    def ures(self):
        if len(self) == 0:
            return ("True")
        else:
            return ("False")
    def kivesz(self):
        if len(self) == 0:
            return "None"
        elif len(self) == 1:
            self.pop()
            return "most már üres"
        else:
            return self.pop()

def main():
    v = Verem()      # üres verem létrehozása
    print(v)         # [
    print(v.ures())  # True
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)         # [1 4 5
    print(v.meret()) # 3
    print(v.ures())  # False
    x = v.kivesz()
    print(x)         # 5
    print(v)         # [1 4
    v.kivesz()
    v.kivesz()       # most már üres
    x = v.kivesz()
    print(x)
    
    
# Írjon egy osztályt, ami megvalósítja a verem adatszerkezetet.

# Az osztályt a következőképpen szeretnénk használni:

# v = Verem()      # üres verem létrehozása
# print(v)         # [
# print(v.ures())  # True
# v.betesz(1)
# v.betesz(4)
# v.betesz(5)
# print(v)         # [1 4 5
# print(v.meret()) # 3
# print(v.ures())  # False
# x = v.kivesz()
# print(x)         # 5
# print(v)         # [1 4
# v.kivesz()
# v.kivesz()       # most már üres
# x = v.kivesz()
# print(x)         # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)
# Sor adatszerkezet

# A veremhez hasonlóan valósítsa meg a sort is saját osztállyal. Először gondolja át, hogy milyen műveleteket kell egy sornak támogatnia, s írjon ezekre példákat (a fenti kódhoz hasonlóan), majd implementálja a Sor osztályt.

# Az implementációnak (most még) nem muszáj hatékonynak lennie.
    # #elsofeladat
    # a = open("alma.txt", 'r')
    # b = open("uj.txt", 'w')
    # li = a.read()
    # for i in li:
    #     if i not in "?:.,;- \n":
    #         if i == i.upper():
    #             if ord(i) <= ord('X'):
    #                 print(chr(ord(i)+2), file=b, end='')
    #             elif ord(i) >= ord('Y'):
    #                 if i == 'Y':
    #                     print('A', file=b, end='')
    #                 elif i == 'Z':
    #                     print('B', file=b, end='')
    #         else:
    #             if ord(i) <= ord('x'):
    #                 print(chr(ord(i)+2), file=b, end='')
    #             elif ord(i) >= ord('y'):
    #                 if i == 'y':
    #                     print('a', file=b, end='')
    #                 elif i == 'z':
    #                     print('b', file=b, end='')
    #     else:
    #         print(i, file=b, end='')


    # #masodikfeladat
    # a = random.randrange(1, 100)
    # print("Number Guessing Game\n--------------------\nI thought of a number between 1 and 100.")
    # print(f"#debug: the number is {a}")
    
    # myguesses = 0
    # fg = -1
    # while fg != a:
    #     fg = int(input("Your guess> "))
    #     myguesses += 1
    #     if fg > a:
    #         print("my number is smaller")
    #     elif fg < a:
    #         print("my number is bigger")
    #     elif fg == a:
    #         print("Good job! That's it!")
    #         print(f"Number of guesses: {myguesses}")


    # #harmadikfeladat
    # a = input("egyik szo: ")
    # b = input("masik szo: ")
    # lia = []
    # lib = []
    # anagrammma = True
    # for i in a:
    #     if i != "?:.,;- \n":
    #         lia.append(i.lower())
    #     else:
    #         continue
    # for i in b:
    #     if i != "?:.,;- \n": 
    #         lib.append(i.lower())
    #     else:
    #         continue
    # lia = sorted(lia)
    # lib = sorted(lib)
    
    # for i in range(0, len(lia)):
    #     if lia[i] != lib[i]:
    #         anagrammma = False
    # if anagrammma == True:
    #     print("anagramma juhuu!!")
    # else:
    #     print("ez nem anagramma!")
    
    
    # #negyedik feladat
    # bekert = input("nyomtatni valo oldalak: ")
    # bekert += ","
    # vesszopozicio = -1
    # li = []
    # a = ""
    # b = ""
    # c = ""
    
    # for i in range(len(bekert)):
    #     if bekert[i] == ',':
    #         vanbennekotojel = False
    #         for j in range(vesszopozicio + 1, i - 1):
    #             if bekert[j] == '-':
    #                 vanbennekotojel = True
    #                 for g in range(0, ((j - 1) - vesszopozicio)):
    #                     b += (bekert[(vesszopozicio + 1) + g])
        
    #                 for h in range(0, ((i - 1) - j)):
    #                     c += (bekert[(j + 1) + h])

    #                 for k in range(int(b), int(c)+1):
    #                     li.append(str(k))
    #                 b = ""
    #                 c = ""
    #                 break

    #         if vanbennekotojel != True:
    #             for j in range(0, ((i-1) - vesszopozicio)):
    #                 a += (bekert[(vesszopozicio + 1) + j])
    #             li.append(a)
    #             a = ""

    #         vesszopozicio = i
    # print(li)  


    #otodik feladat



    # #hatodik feladat
    # log = [2, 4, 8, 3, 9, 7, 1]
    # sum = 0
    # sum2 = 0
    # for i in range(len(log)-1):
    #     sum += (abs(log[i] - log[i + 1]))
    # print(sum)


    # calc = 2**(1024)
    # szam = str(calc)
    # for i in range(len(szam)-1):
    #     sum2 += (abs(int(szam[i]) - int(szam[i + 1])))
    
    # print(sum2)


if __name__ == "__main__":
    main()