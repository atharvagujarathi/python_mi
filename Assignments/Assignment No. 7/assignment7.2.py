import threading
import os


def even_factors(a):
    evensum = 0

    for i in range(1, a+1):
        if a % i == 0 and i % 2 == 0:
            evensum += 1
    print(evensum)


def odd_factors(b):
    oddsum = 0

    for i in range(1, b+1):
        if b % i == 0 and i % 2 != 0:
            oddsum += 1
    print(oddsum)


def main():
    value1 = int(input("Enter the Even Factor Value: "))
    value2 = int(input("Enter the Odd factor value: "))

    # no = 5
    es = threading.Thread(target=even_factors, args=(value1,))
    oos = threading.Thread(target=odd_factors, args=(value2,))

    es.start()
    oos.start()

    es.join()
    oos.join()


if __name__ == "__main__":
    main()
