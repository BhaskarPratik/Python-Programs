# Method 1 :
# myList = [10, 20, 49, 95, 4]
# myList.sort()
# print(myList)  # [4, 10, 20, 49, 95]
# print("First Largest Number :", myList[-1])
# print("Second Largest Number :", myList[-2])

# Method 2 :
myList = [10, 20, 49, 95, 4]
new_list = set(myList)
new_list.remove(max(new_list))
print(new_list)

print(" Second Largest Number is :",max(new_list))