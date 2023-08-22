# for example - Chinese...

from functools import reduce


def checkEven(no):
    if (no % 2 == 0):
        return True
    else:
        return False


def increase(no):
    return no+2


def Summation(a, b):
    return a+b


def main():
    data = [5, 4, 9, 8, 13, 17, 12, 18]
    print(data)

    output = list(filter(checkEven, data))
    print(output)

    output1 = list(map(increase, output))
    print(output1)

    output2 = int(reduce(Summation, output1))
    print(output2)


if __name__ == "__main__":
    main()
