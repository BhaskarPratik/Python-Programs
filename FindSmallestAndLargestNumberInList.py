# Method 1 : Sort the list in ascending order and print the first and last element in the list
# myList = [20, 100, 20, 1, 10]
# myList.sort()  # sorting
# print(myList)  # [1, 10, 20, 20, 100]
# print("smallest element is :", myList[0])
# print("largest element is :", myList[-1])

# Method 2 : using min() and max() method
myList = [20, 100, 20, 1, 10]
print("smallest element is : ", min(myList))
print("Largest element is : ", max(myList))
