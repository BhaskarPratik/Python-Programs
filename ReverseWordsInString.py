str = "welcome to python programming "
words = str.split(' ')
print(words)  # ['welcome', 'to', 'python', 'programming']
words = words[-1::-1]
print(words)  # ['', 'programming', 'python', 'to', 'welcome']
outptstr = ' '.join(words)
print(outptstr)
