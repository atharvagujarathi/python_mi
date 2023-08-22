# for example - Chinese...

from functools import reduce


def checkEven(no):
    return (no % 2 == 0)


def increase(no):
    return no+2


def Summation(a, b):
    return a+b


def main():
    data = []

    print("Enter number of elements: ")
    n = int(input())

    print("Enter the elements: ")
    for i in range(n):
        value = int(input())
        data.append(value)

    output = list(filter(checkEven, data))
    print(output)

    output1 = list(map(increase, output))
    print(output1)

    output2 = int(reduce(Summation, output1))
    print(output2)


if __name__ == "__main__":
    main()
