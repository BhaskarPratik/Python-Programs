# Approach 1 :Using Loop

# myList = [1, 6, 3, 5, 4]
#
# ele = 100
# flag = 0
#
# for i in myList:
#     if i == ele:
#         print("Element found")
#         flag = 1
#         break
# if flag == 0 :
#     print("Element not found")

# Approach 2 :Using in operator

myList = [1, 6, 3, 5, 4]
ele = 200
if ele in myList:
    print("Element found")
else:
    print("Element not found")