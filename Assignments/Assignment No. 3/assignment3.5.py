def main():

    arr = []

    n = int(input("Enter the value of numbers which user wants: "))

    for i in range(n):
        numbers = int(input("Enter the numbers: "))
        arr.append(numbers)

    print("The user list is: ", arr)

    print(sum(arr))

    if numbers <= 1 and numbers % 2 == 0 and numbers % 3 == 0:
        return False
    
    if numbers <= 3:
        print(sum(arr))
    




if __name__ == "__main__":
    main()


# doubt
