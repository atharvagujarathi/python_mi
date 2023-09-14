class bookStore:
    noOfBooks = 0

    def __init__(self, a, b):
        print("Inside the Instance method")
        self.Name = a
        self.Author = b
        print("The Name is: ", self.Name)
        print("The Author is: ", self.Author)

    def Display(self):
        bookStore.noOfBooks = bookStore.noOfBooks + 1
        print("The Number of books are: ", bookStore.noOfBooks)


def main():
    value1 = input("Enter the First Value: ")
    value2 = input("Enter the Second Value: ")

    print("Initially the number of books are: ", bookStore.noOfBooks)

    obj1 = bookStore(value1, value2)
    obj1.Display()

    obj2 = bookStore(value1, value2)
    obj2.Display()


if __name__ == "__main__":
    main()
