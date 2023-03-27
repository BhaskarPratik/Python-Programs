# Method 1: find reverse of string

s = input("Enter string : ")
rev_str = s[::-1]  # reverse string

if s == rev_str:
    print("String is Palindrome")
else:
    print("String is not Palindrome")
