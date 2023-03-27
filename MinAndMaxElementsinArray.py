arr = [41, 24, 33, 48, 15]

# find max element no of element in array
max = arr[0]
n = len(arr)

for i in range(1, n):
    if arr[i] > max:
        max = arr[i]
print("Maximum no of array is:", max)


# minimum no of element in array

min = arr[0]
n = len(arr)
for i in range(1,n):
    if arr[i] < min:
        min: arr[i]

print("Minimum value of array is:", min)