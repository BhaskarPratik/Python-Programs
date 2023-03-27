# Method 1 : using for loop
# str = "welcome"
# counter = 0
# for i in str:
#     counter = counter + 1
# print("Length of string : ", counter)

# Method 2 : using while loop and slicing
# str = "welcome"
# counter = 0
# while str[counter:]:
#     counter = counter + 1
# print("Length of string : ", counter)

# Method 3 : using built-in function len()
# str = "welcome"
# print("Length of string : ", len(str))

# Method 4 : using join and count
str = "welcome to python"
randrom_str = "X"
print(randrom_str.join(str))  # wXeXlXcXoXmXe
print(randrom_str.join(str).count(randrom_str)) # 6
print(randrom_str.join(str).count(randrom_str)+ 1)
