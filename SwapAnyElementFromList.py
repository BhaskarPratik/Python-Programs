# Approach 1 : simple approach
myList = [23, 65, 19, 90]
# print("List Before swap : ", myList)
# pos1, pos3 = 1, 3
# myList[pos1], myList[pos3] = myList[pos3], myList[pos1]
# print("List after swap: ", myList)

# Approach 2: using list.pop()
# print("List Before swap : ", myList)
# pos1, pos2 = 1, 3
# first_ele = myList.pop(pos1) # 65
# sec_ele = myList.pop(pos2 - 1)  # 23, 19,90
# myList.insert(pos1,sec_ele)
# myList.insert(pos2,first_ele)
# print("List after swap: ", myList)

# Approach 3: using tuple()
print("List Before swap : ", myList)
pos1,pos2 = 1,3
get = (myList[pos1],myList[pos2])
myList[pos2],myList[pos1] =get
print("List after swap: ", myList)