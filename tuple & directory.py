def main():
    
    kartya = [1, "Aladár", 4.5]
    id, nev, jegy = kartya
    print(kartya)
    print(id, nev, jegy)
    
    #dictionary
    myDict = {
        "anna" : 4.5,
        "bela" : 2,
        "cecilia" : 1
    }
    print(myDict["bela"])
    print(myDict.keys())
    print(myDict.values())
    print(myDict.items()) #keyvaluepaireket ad vissza
    print(len(myDict))



if __name__ == "__main__":
    main()