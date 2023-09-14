def main():
    print("Enter first number")
    no1 = int(input())

    print("Enter second number")
    no2 = int(input())

    Ans = 0

    try:
        Ans = no1/no2

    except ZeroDivisionError as zobj:
        print("We can't do zero: ", zobj)

    print("The division is: ", Ans)


if __name__ == "__main__":
    main()
