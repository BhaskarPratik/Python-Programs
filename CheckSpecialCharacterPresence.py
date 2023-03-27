import re

str1 = "welcome@@2To%%python**Programming@!!^%%%@$"
str2 = "Welcome to python"
regex = re.compile('[@~!@#$%^&*()_+]')

if regex.search(str1) is None:
    print("No special character present in string")
else:
    print("Special character present in string")
