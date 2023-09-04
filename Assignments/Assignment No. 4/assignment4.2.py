def main():
    multiplication = lambda x, y: x * y

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = multiplication(a, b)
    print("The multiplication of ", a, "&", b, "is", result)

if __name__ == "__main__":
    main()