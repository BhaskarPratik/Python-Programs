# Approach 1 : using slicing technique
# myList = [1, 8, 6, 9, 4, 16]
# myListCopy = myList[:]
# print(myListCopy)  # [1, 8, 6, 9, 4, 16]

# Approach 2 : using extend() method
# myList = [1, 8, 6, 9, 4, 16]
# myListCopy = []
# myListCopy.extend(myList)
# print(myListCopy)  # [1, 8, 6, 9, 4, 16]

# Approach 3: Using the list() method
# myList = [1, 8, 6, 9, 4, 16]
# myListCopy = list(myList)
# print(myListCopy)  # [1, 8, 6, 9, 4, 16]

# Approach 4: Using the copy() method
# myList = [1, 8, 6, 9, 4, 16]
# myListCopy = myList.copy()
# print(myListCopy)  # [1, 8, 6, 9, 4, 16]

# Approach 5: Using list compression
myList = [1, 8, 6, 9, 4, 16]
myListCopy = [i for i in myList]
print(myListCopy)