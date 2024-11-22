import random

arr = []
target = 5

for i in range(0,10):
    arr.append(random.randint(0,10))
print(arr)




for i  in range(len(arr)):
    if arr[i] == target:
        print("Target is at index: ", i)
    else:
        print("Target is not at index: ", i)
