def DisplayW():
    i = 1
    while (i < 6):
        print(i, end=" ")
        i += 1


def DisplayF():
    for i in range(1, 6):
        print(i, end=" ")


def main():
    DisplayF()
    DisplayW()


if __name__ == "__main__":
    main()
