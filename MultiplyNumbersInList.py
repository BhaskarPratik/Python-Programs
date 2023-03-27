# Method 1 :Traversal
# myList = [3, 2, 4]
#
# result = 1
# for i in myList:
#     result = result * i
# print(result)

# Method 2 :using numpy.prod() * install numpy package
import numpy
myList = [3, 2, 4]
result = numpy.prod(myList)
print(result)