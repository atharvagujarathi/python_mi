import threading
import os

def even():
    # This function is used to accept the list from user for even numbers
    print("for thread 1", os.getpid())
    even_number_list = []
    value1 = int(input("Enter the list for Evenlist: "))

    for i in range(value1):
        numbers = int(input("Enter the numbers: "))
        even_number_list.append(numbers)
    print("This is the user list to get the output of evenlist numbers",even_number_list)

    even_number_list_new = []
    for num in even_number_list:
        if num % 2 == 0:
            even_number_list_new.append(num)
    print("The even list number list is: ",even_number_list_new)     
    print("The sum of number in the even number list is: ", sum(even_number_list_new))   


def odd():
    print("for thread 2", os.getpid())
    # This function is used to accept the list from user for odd numbers
    odd_number_list = []
    value2 = int(input("Enter the list for Oddlist: "))

    for i in range(value2):
        numbers = int(input("Enter the numbers: "))
        odd_number_list.append(numbers)
    print("This is the user list to get the output of oddlist numbers",odd_number_list)

    odd_number_list_new = []
    for numm in odd_number_list:
        if numm % 2 == 1:
            odd_number_list_new.append(numm)
    print("The odd list number list is: ",odd_number_list_new)   
    print("The sum of number in the odd number list is: ", sum(odd_number_list_new))   


def main():

    eventhread = threading.Thread(target=even)
    oddthread = threading.Thread(target=odd)     

    eventhread.start()
    eventhread.join()

    oddthread.start()
    oddthread.join()

if __name__ == "__main__":
    main()
