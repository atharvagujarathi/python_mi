# create a module named as arithematic which contains 4 functions ass Add() for addition
# sub() for substraction, mul() for multiplication and div() for division. All functions accepts two parameters as number and
# perform the operation. Write a program which call all the functions from Arithematic module by accepting the parameters from user.

x = int(input("Enter the first value: "))
y = int(input("Enter the second value: "))


def Sum(x, y):
    print("The addition of given numbers is: ", x+y)


def Sub(x, y):
    print("The substraction of given numbers is: ", x-y)


def Mul(x, y):
    print("The multiplication of given numbers id: ", x*y)


def Div(x, y):
    print("The division of given numbers is: ", int(x/y))


Sum(x, y)
Sub(x, y)
Mul(x, y)
Div(x, y)
