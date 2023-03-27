myList = [12, 35, 9, 56, 24]
size = len(myList)

# Approach 1 :Temporary variable
# print("List before sorting: ", myList)
# temp = myList[0]
# myList[0] = myList[size - 1]
# myList[size -1] = temp
# print("List after sorting: ", myList)

# Approach 2 :Temporary variable
# print("List before sorting: ", myList)
# myList[0],myList[-1] = myList[-1],myList[0]
# print("List after sorting: ", myList)

# Approach 3 :tuple variable
# print("List before sorting: ", myList)
# get = (myList[-1],myList[0])  # packing
# myList[0],myList[-1] = get  # unpacking
# print("List after sorting: ", myList)

# Approach 4 :* operand
# print("List before sorting: ", myList)
# start,*middle,last = myList
# myList = [last,*middle,start]
# print("List after sorting: ", myList)

# Approach  :* using pop()
print("List before sorting: ", myList)
first = myList.pop(0)
last = myList.pop(-1)

myList.insert(0,last)
myList.append(first)
print("List after sorting: ", myList)