# write a program which accept and display below pattern
# input = 5
#  * * * * *
#  * * * * *
#  * * * * *
#  * * * * *
#  * * * * *

x = int(input("Enter the number: "))

for i in range(x):
    for j in range(x):
        print("* ", end="")
    print()
