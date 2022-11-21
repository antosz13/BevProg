def main():
    while True:
        try:
            szam1 = float(input("1. szam: "))
            szam2 = float(input("2. szam: "))
            result = szam1 / szam2
            print('Az osztas eredmenye: {0:.2f}'.format(result))
            print('-' * 10)
        except ValueError:
            print("Szamot adj meg!")
        except KeyboardInterrupt:
            break
        except ZeroDivisionError:
            print("0val osztas")

#####

if __name__ == "__main__":
    main()