
def recsum(li):
    summa = 0
    for i in range(len(li)):
        summa += li[i]
    return summa   

def main():
    log = [1, 2, 3 , 4]
    print(recsum(log))
    
    
if __name__ == "__main__":
    main()