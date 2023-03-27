# The find() methods finds the first occurrence of the specified value
# The find() method returns -1 if the value is not found

str = "Welcome to python programming"
sub_str = "python"
print(str.find(sub_str))  # 11
if str.find(sub_str) == -1:
    print("Not Found")
else:
    print("Found")
