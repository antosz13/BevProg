def main():
    
    log1 = [1, 3, 54, 5124423, 54321]
    log2 = [74, 3, 1, 54, 412424312, 568765989, 8765]

    for i in log1:
        for j in log2:
            if i == j:
                print(i)
        

if __name__ == "__main__":
    main()