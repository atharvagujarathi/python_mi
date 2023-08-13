import multiprocessing


def square(no):
    return no * no

# pool means it collects the data and then divide it in all cores.


def main():
    Arr = [10, 20, 30, 40]
    Result = []
    p = multiprocessing.Pool()
    Result = p.map(square, Arr)
    p.close()
    p.join()

    print(Result)


if __name__ == "__main__":
    main()
