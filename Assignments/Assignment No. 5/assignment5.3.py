class Arithematic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = float(input("Enter the First Number: "))
        self.Value2 = float(input("Enter the Second Number: "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Substraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        return self.Value1 / self.Value2

def main():
    object1 = Arithematic()

    object1.Accept()
    print("The Addition of two numbers is: ", object1.Addition())
    print("The Substraction of two numbers is: ", object1.Substraction())
    print("The Multiplication of two numbers is: ", object1.Multiplication())
    print("The Division of Two Numbers is: ", object1.Division())

if __name__ == "__main__":
    main()

