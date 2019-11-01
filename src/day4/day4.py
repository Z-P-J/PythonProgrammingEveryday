'''
编写一个函数判断一个数是否是奇数，
并判断101-200之间有多少个素数，
并输出所有素数
'''
import math
def isPrimeNum(num):
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            return False
    return True

count = 0
for num in range(101, 201):
    if isPrimeNum(num):
        print(num)
        count = count + 1
print("The total num is %d" %count)