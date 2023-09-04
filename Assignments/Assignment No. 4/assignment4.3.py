from functools import reduce

def checkSeventy(x):
    if x >= 70 and x <= 90:
        return True
    
def increaseTen(y):
    return y + 10

def product(a, b):
    return a * b



def main():
    
    arr = []

    n = int(input("Enter the value which user wants into the list: "))

    for i in range(n):
        numbers = int(input("Enter the numbers: "))
        arr.append(numbers)

    print("The user list is: ", arr)    
    
    stepOneFilter = list(filter(checkSeventy, arr))
    print("The Filter value is: ", stepOneFilter)

    stepTwoMap = list(map(increaseTen, stepOneFilter))
    print("The Map value is: ", stepTwoMap)

    stepThreeReduce = int(reduce(product, stepTwoMap))
    print("The Reduce value is:", stepThreeReduce)




if __name__ == "__main__":
    main()