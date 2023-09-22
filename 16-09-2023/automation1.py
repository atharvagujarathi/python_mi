from sys import *


def main():
    print("-------------- Automation Script --------------")

    print("Automation Script Name : ", argv[0])

    if (len(argv) == 2):
        if (argv[1] == "-h" or argv[1] == "-H"):    # Flag for displaying help
            print("This automation script is used to perform addition of two numbers")
            exit()

        # Flag for displaying the usage of script
        elif (argv[1] == "-u" or argv[1] == "-U"):  # Flag for displaying usage
            print("Usage : Name_Of_Script First_Argument Second_Argument")
            print("Example : Demo.py 11 10 67")
            exit()

        else:
            print("There is no such option to handle")
            exit()

    if (len(argv) != 3):
        print("Invalid number of arguments")
        exit()


if __name__ == "__main__":
    main()

# python Automation1.py 11 10
