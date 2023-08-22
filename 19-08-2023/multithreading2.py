import threading


def fun(number):
    for i in range(number):
        print(i)


def gun(number):
    for i in range(number):
        print(i)


if __name__ == "__main__":

    number = 5
    thread1 = threading.Thread(target=fun, args=(number,))
    thread2 = threading.Thread(target=gun, args=(number,))


# will execute both as parallel
    thread1.start()
    thread2.start()

    # join thread back to the parent process which is this
    thread1.join()
    thread2.join()
