def lnko(a, b):
    while a != b:
        if a > b:
            a -= b
        elif a < b:
            b -= a
    return a

def lnkorec(a, b):
    if a > b:
        return lnko(a-n, b)
    elif a < b:
        return lnko(b-a, a)
    blablabla




def main():
    print(lnko(18, 4))
    



if __name__ == "__main__":
    main()