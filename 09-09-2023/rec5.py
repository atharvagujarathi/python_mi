# If I want to access the global variable in function we have to used "global" variable for this.

i = 0


def Display():
    global i
    print("Inside Display", i)
    i += 1
    Display()


def main():
    Display()


if __name__ == "__main__":
    main()
