def addition(no1, no2):
    ans = 0
    ans = no1 + no2
    return ans


def substraction(no1, no2):
    ans = 0
    ans = no1 - no2
    return ans


def main():
    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))

    ret = addition(value1, value2)
    print("Addition is: ", ret)

    ret = substraction(value1, value2)
    print("Substraction is: ", ret)


if __name__ == "__main__":
    main()
