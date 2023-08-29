import re


def main():
    arr = []

    n = int(input("Enter the value of numbers which user wants: "))

    for i in range(n):
        numbers = int(input("Enter the numbers: "))
        arr.append(numbers)

    print("the user list is: ", arr)
    searchNumber = int(input("Enter the number to fimd the freqency: "))

    fre = arr.count(searchNumber)
    print("The frequency of the ", searchNumber, " is ", fre)


if __name__ == "__main__":
    main()
