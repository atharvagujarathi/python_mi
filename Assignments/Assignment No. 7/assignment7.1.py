import threading
import os


def even_numbers():
    print("Function 1: ", os.getpid(), "Thread ID is: ", threading.get_ident())
    even = []
    count = 0
    num = 2  # because even numbers are starting from 2

    while count < 10:
        even.append(num)
        num += 2
        count += 1

    print(even)


def odd_numbers():
    print("Function 2: ", os.getpid(), "Thread ID is: ", threading.get_ident())
    odd = []
    count = 1

    while len(odd) < 10:
        odd.append(count)
        count += 2

    print(odd)


def main():
    print("This is the multithreading program")

    en = threading.Thread(target=even_numbers)
    on = threading.Thread(target=odd_numbers)

    en.start()
    on.start()

    en.join()
    on.join()


if __name__ == "__main__":
    main()
