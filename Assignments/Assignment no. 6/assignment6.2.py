class BankAccount:

    ROI = 10.5

    def __init__(self, a, b):
        self.name = a
        self.amount = b

    def Display(self):
        print("HI", self.name)
        print("Your Amount is", self.amount)

    def Deposit(self, b):
        ans = 0
        print("you are deposit the amount of rs", b)
        ans = self.amount = self.amount + b
        print("your total deposited rs:", ans)

    def Withdraw(self, b):
        ans = 0
        ans = self.amount = self.amount - b
        print("you withdraw rs", ans)

    def CalculateInterest(self):
        print("your roi is", BankAccount.ROI + 1)


def main():
    value1 = (input("Enter the first value: "))
    value2 = int(input("Enter the second value: "))

    print("the initial rate of interest is", BankAccount.ROI)

    Atharva = BankAccount(value1, value2)

    print("This Operations are performed on Atharva's data")
    Atharva.Display()
    Atharva.Deposit(3000)
    Atharva.Withdraw(1500)
    Atharva.CalculateInterest()

    Amit = BankAccount(value1, value2)

    print("This Operations are performed on Amit's data")
    Amit.Display()
    Amit.Deposit(6000)
    Amit.Withdraw(300)
    Amit.CalculateInterest()


if __name__ == "__main__":
    main()
