arr = []

n = int(input("Enter the value of numbers which user wants in the list: "))

for i in range(n):
    numbers = int(input("Enter the numbers: "))
    arr.append(numbers)

print("The user list is: ", arr)

sortedArrayList = sorted(arr)
print("The sorted list is: ", sortedArrayList)
print("The minimum number in the sorted list is", sortedArrayList[0])
