from array import *

# arr = array('i', [-1,2,3,4,5])

# print(arr)
# print(arr.buffer_info())


# for i in arr:
#     print(i)
 
# for pnt in range(4):
#     print(pnt, arr[pnt])   

# arr.reverse()
# print(arr)

# arr.append(6)
# print(arr)

# arr.append(6)
# print(arr)

# arr.remove(6)
# print(arr)

# arr = array('i', [])
# x = int(input("Enter the length of the array: "))
# print("Enter %d elements"%x)
# for i in range(x):
#     n = int(input())
#     arr.append(n)
# print(arr)

#Removing duplicates in  array arr
# i = 0
# while i < x -1:
#     j = i + 1
#     while j < x:
#         if arr[i] == arr[j]:
#             arr.pop(j)
#             x -= 1
#         else:
#             j += 1
#     i += 1
# print(arr)


arr = []
for _ in range(6):
    arr.append(list(map(int, input('Enter number;').split())))

maxSum = -100
for i in range(4):
    for j in range(4):
        sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        if sum > maxSum:
            maxSum = sum

print(maxSum)