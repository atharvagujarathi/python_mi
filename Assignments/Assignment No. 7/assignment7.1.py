import threading


def even_numbers():
    even = []
    count = 0
    num = 2  # because even numbers are starting from 2

    while count < 10:
        even.append(num)
        num += 2
        count += 1

    print(even)


def odd_numbers():
    odd = []
    count = 1

    while len(odd) < 10:
        odd.append(count)
        count += 2

    print(odd)


def main():
    print("This is the multithreading program")

    no = 5
    en = threading.Thread(target=even_numbers, args=(no,))
    on = threading.Thread(target=odd_numbers, args=(no,))

    en.start()
    on.start()

    en.join()
    on.join()


if __name__ == "__main__":
    main()
