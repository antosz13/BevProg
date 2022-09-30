
def both_ends(stri):
    if len(stri) < 2:
        return ''
    return (stri[0:2] + stri[-1:])

def main():
    txt = "hello world"
    print(len(txt))
    print(txt[3])
    print(txt[1:8])
    print(txt.upper())
    print(txt.capitalize())
    print(txt.title())
    print("               hello          ".strip())
    print(txt.replace("llo", "nlo"))
    print("1;2;3;4;5".split(sep=';'))
    print(txt.rfind('o'))
    print(txt.join("henlo"))
    
    print(both_ends("edba"))


if __name__ == "__main__":
    main()