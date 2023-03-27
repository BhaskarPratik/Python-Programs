#  Method 1 : using for loop with range()
myList = [5, 10, 15, 20]
total = 0

for i in range(0, len(myList)):
    total = total + myList[i]
print("sum of all elements in given list: ", total)

#  Method 2 : using sum() method
# myList = [5,10,15,20]
# total = sum(myList)
# print("Sum of myList is : ",total)
