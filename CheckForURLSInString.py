import re

str1 = "I am a bloger at https://www.pavantestingtools.com/"
str2 = "I am a bloger at https://www.pavantestingtools.com/ and present at https://www.pavanonlinetrainings.com/"

url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str2)
print(url)
