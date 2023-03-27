# Method 1 : using loop
# myList = [15,6,10,8,16,10,85,10,75,15,56,85]
# x = 15
# count = 0
#
# for ele in myList:
#     if ele == x:
#         count = count + 1
# print("{} has occurred {} times ".format(x,count))

# Method 2 : using count()
# myList = [15,6,10,8,16,10,85,10,75,15,56,85]
# x = 15
# print("{} is occurred {} times".format(x,myList.count(x)))

# Method 3 : using counter()
from collections import Counter

myList = [15, 6, 10, 8, 16, 10, 85, 10, 75, 15, 56, 85]
x = 15
dic = Counter(myList)  # {15:2,6:1,10:3.....}
print("{} is occurred {} times".format(x,dic[x]))
