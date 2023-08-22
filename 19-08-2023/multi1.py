import multiprocessing
import os


def task1(value):
    print("Executing the first task...")
    print("PID of running process for task1 is: ", os.getpid())
    for i in range(value):
        print("Task1 :", i)

        # logic


def task2(value):
    print("Executing the second task...")
    print("PID of running process for task2 is: ", os.getpid())
    for i in range(value):
        print("Task2 :", i)

        # logic


def main():
    print("Demonstration of Multiprocessing...")
    print("PID of running process is: ", os.getpid())

    no = 500
    no2 = 800
    p1 = multiprocessing.Process(target=task1, args=(no,))
    p2 = multiprocessing.Process(target=task2, args=(no2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == "__main__":
    main()
