


def main():
    li = [n*2 for n in range(0, 10)]
    li2 = ["auto", "metro", "villamos"]
    
    #list comprehension
    li3 = [s.upper()+'!' for s in li2]
    for i in range(0,10): #ez ugyanaz mint a folote levo csak igy bonyibb elv
        li.append(i*2)
    print(li)
    print(li2)
    print(li3)
    nums = '1234567'
    li4 = [z for z in nums]
    print(li4)
    txt = "The quick brown fox jumps over the lazy dog"
    li5 = [len(j) for j in txt.split()]
    print(li5)


if __name__ == "__main__":
    main()