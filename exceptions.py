def main():
    try:
        d1 = int(input("Num1: "))
        d2 = int(input("Num2: "))
        print(d1/d2)
    except ZeroDivisionError:
        print("Nullaval nem osztunk")
    except (KeyboardInterrupt,FileNotFoundError):
        print("Ha nem megy hat nem megy")
    except:
        pass
    print("Vege")

if __name__ == "__main__":
    main()