'''
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
'''

numStr = input("Please input the value of X and Y:")
print(numStr.split(","))
nums = numStr.split(",")
X = int(nums[0])
Y = int(nums[1])
array = []
for i in range(X):
    newArr = []
    array.append(newArr)
    for j in range(Y):
        newArr.append(i * j)
print(array)

# 参考答案：
# input_str = input()
# dimensions = [int(x) for x in input_str.split(',')]
# rowNum = dimensions[0]
# colNum = dimensions[1]
# multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

# for row in range(rowNum):
#     for col in range(colNum):
#         multilist[row][col]= row*col
    
# print(multilist)