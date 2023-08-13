def fun(no):
    sum = 0

    for i in range(100000):
        sum = sum + (no*no)
    return sum


def main():
    print("Demonstartion of serial execution using single core.")

    Result = []
    for no in range(1000):
        Result.append(fun(no))


if __name__ == "__main__":
    main()
