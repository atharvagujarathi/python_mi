class Numbers:

    def __init__(self, a):
        self.value = a

    def chkprime(self):
        if (self.value > 1):
            for i in range(2, (self.value/2)+1):
                if (self.value % i == 0):
                    return False
                break

            else:
                return True

        else:
            return False

    def chkperfect():
        pass

    def sumfactors():
        pass

    def factors():
        pass


def main():
    value = input("Enter the Number: ")


if __name__ == "__main__":
    main()
