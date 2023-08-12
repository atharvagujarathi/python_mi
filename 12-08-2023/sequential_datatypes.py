# SEQUENCIAL DATATYPES IN PYTHON

# 1]. List:
# - heterogenous = different datatype we can used in single variable
# - ordered = Some are ordered some are not.
# - Indexed
# - mutable
# - duplicate allowed
# []


# Listdemo.py
print("Demonstration of List")
List1 = [10, "Hello", 67.90, True]
print("List", List1)
print(List1[0])

List2 = [11, 78, 90, 11, 45, 78]
print(List2)

List2[1] = 79
print(List2)

List2.append(101)
print(List2)

List2.remove(11)
print(List2)


# 2] Tuple:
# - heterogenous
# - ordered
# - indexed
# - immutable
# - Duplicate allowed
# - ()


Tuple1 = (11, "Hello", 90.89, False)
print("Tuple", Tuple1)
print(type(Tuple1))
print(len(Tuple1))
print(Tuple1[1])

# Tuple1[0] = 12  NA
# print(Tuple1)

# Tuple1.append(67)
# print(Tuple1)

Tuple2 = (11, 89, 62, 11)
print(Tuple2)


# 3]. Set:
# - heterogenous
# - unordered
# - unindexed
# - duplicate invalid
# - mutable
# - {}


Set1 = {True, 11, "hello", 89.90}
print("Set", Set1)
# print(Set1[1])

for value in Set1:
    print(value)

Set2 = {11, 78, 11, 78, 99}
print(Set2)

Set2.add(101)
print(Set2)

Set2.remove(101)
print(Set2)

# print("Enter the value that you want to search in Set:")
# No = int(input())

# for value in Set2:
#     if (No == value):
#         print("Element is present", value)
#         break


# 4]. Dictionary:
# - heterogenous
# - ordered
# - unindexed
# - mutable
# - duplicate invalid
# - {}

# List as Dict.py

BatchName = ["PPA", "python", "LB", "c#"]
BatchFees = [18000, 50, 2000, 10]
for i in range(len(BatchName)):
    print("Batch Name:", BatchName[i])
    print("Batch Fees", BatchFees[i])
    print()


Batches = {"ppa": 18500, "python": 5000, "lb": 40, "cv": 4}
print(Batches)
print(type(Batches), len(Batches))
print(Batches["ppa"])

for value in Batches:
    print(value)


for value in Batches:
    print(value, Batches[value])
