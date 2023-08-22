class Arithematic:
    def __init__(self, a, b):
        print("Inside constructor")
        self.no1 = a
        self.no2 = b

    def addition(self):
        ans = 0
        ans = self.no1 + self.no2
        return ans

    def substraction(self):
        ans = 0
        ans = self.no1 - self.no2
        return ans


def main():
    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))

    obj1 = Arithematic(value1, value2)

    ret = obj1.addition()
    print(ret)

    ret = obj1.substraction()
    print(ret)

    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))

    obj2 = Arithematic(value1, value2)

    ret = obj2.addition()
    print(ret)

    ret = obj2.substraction()
    print(ret)


if __name__ == "__main__":
    main()
