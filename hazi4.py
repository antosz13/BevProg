#caesar kodolas
def caesar(text):
    decode = ""
    for i in text:
        decode += chr(ord(i) - 3)
    return decode


#bizonyos karakterek
def fgv(text, chars):
    txtback = ""
    for i in text:
        for j in chars:
            if i == j:
                txtback += i
    return txtback            


#beszurofgv
string = "Az egy bogre"
def beszurofgv(word1, word2):
    x = string.replace(word1, (word2 + ' ' + word1))
    return x    


#binaris konverter
def bindec(num):  
    print((num % 2), end = '')
    if num == 0:
        return print("vege")
    return bindec(num//2)
    



def main():
    print(caesar("kwwsv=22|rxwx1eh2gTz7z<Zj[fT"))
    print(fgv("almaazjo", "mj8232"))
    print(beszurofgv("bogre", "piros"))
    print(bindec(156))
    
    
if __name__ == "__main__":
    main()