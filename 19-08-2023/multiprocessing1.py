# If we want to execute the multiple processs simultaneously then its called multiprocessing.
# os loves to create multiple threads as compare to multiple processes.
import multiprocessing
import os


def fun(number):
    print('parent process of fun:', os.getppid())
    print
