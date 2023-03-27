myList = ["geeks", "for", "geeks","geeks","geeks"]
word = "geeks"
n = 3
count = 0

for i in range(0,len(myList)-1):
    if myList[i] == word:
        count = count + 1
        if count == n:
            del myList[i]

print(myList)
