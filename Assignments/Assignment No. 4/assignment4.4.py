from functools import reduce
def checkEven(x):
    if x % 2 == 0:
        return True
    
def square(y):
    return y ** 2

def summation(a, b):
    return a + b 


def main():
    arr = []

    n = int(input("Enter the value of numbers which user wants into the list: "))

    for i in range(n):
        numbers = int(input("Enter the numbers"))
        arr.append(numbers)

    print("The user list is", arr)    


    stepOneFilter = list(filter(checkEven, arr))
    print("The filter value is: ", stepOneFilter)

    stepTwoMap = list(map(square, stepOneFilter))
    print("The mapo value is: ", stepTwoMap)

    stepThreeReduce = int(reduce(summation, stepTwoMap))
    print("The reduce value is: ", stepThreeReduce)

if __name__ == "__main__":
    main()