class demo:
    def __init__(self, a, b):
        print("Inside Constructor")
        self.no1 = a
        self.no2 = b

    def fun(self):
        # ans = 0
        ans = self.no1 + self.no2
        return ans
    
    def gun(self):
        # ans = 0
        ans = self.no1 - self.no2
        return ans
    

def main():
    value1 = int(input("Enter the first number: "))
    value2 = int(input("Enter the second number: "))

    obj1 = demo(value1, value2)

    firstOutput = obj1.fun()
    print(firstOutput)

    secondOutput = obj1.gun()
    print(secondOutput)

    value1 = int(input("Enter the first number: "))
    value2 = int(input("Enter the second number: "))

    obj2 = demo(value1, value2)

    firstOutput = obj2.fun()
    print(firstOutput)

    secondOutput = obj2.gun()
    print(secondOutput)


if __name__ == "__main__":
    main()
