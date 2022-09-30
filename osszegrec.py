
def sum(li):
    summa = 0
    for i in range(len(li)):
        summa += li[i]
    return summa   



def recsum(li):
    if len(li) == 1:
        return li[0]
    return li[0] + recsum(li[1:])


def main():
    log = [1, 2, 3 , 4]
    print(sum(log))
    print(recsum(log))
    
    
if __name__ == "__main__":
    main()