arr = []
n = int(input("Enter the numbers which user wants in list: "))

for i in range(n):
    numbers = int(input("Enter the numbers: "))
    arr.append(numbers)

print("the list is, ", arr)
print("The sum of the numers into the list is: ", sum(arr))
