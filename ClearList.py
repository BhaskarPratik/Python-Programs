# Approach 1 : clear() method
# myList = [6, 0, 4, 1]
# print("list before clear : ", myList)
# myList.clear()
# print("list after clear : ", myList)


# Approach 2 : initialize the list with no value
# myList = [6, 0, 4, 1]
# print("list before clear : ", myList)
# myList = []
# print("list after clear :", myList)

# Approach 3 :" *=0 " this method removes all element of the list and make it empty.
# myList = [6, 0, 4, 1]
# print("list before clear:", myList)
# myList *=0  # delete the list
# print("list after clear: ", myList)

# Approach 4 : using del
myList = [6, 0, 4, 1]
print("list before clear: ", myList)
del myList[:] # deletes all the element
print("list after clear : ", myList)
