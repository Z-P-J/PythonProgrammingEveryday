'''
一个数如果恰好等于它的因子之和，这个数就称为“完数”。
例如6=1＋2＋3.编程找出1000以内的所有完数。
'''

import math

for num in range(1, 1001):
    temp = 0
    for i in range(1,  num // 2 + 1):
        if num % i == 0:
            temp += i
    if temp == num:
        print("%d" %num)
