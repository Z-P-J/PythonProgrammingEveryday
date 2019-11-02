'''
将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
'''
import math
def fun(num):
    # print("num=%d" %num)
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            # print("i1=%d" %i)
            return str(i) + "*" + fun(num // i)
    # print("i2=%d" %num)
    return str(num)


num = int(input("请输入一个正整数："))
result = fun(num)
numStr = str(num)
if result == numStr:
    print(numStr + "=1*" + numStr)
else:
    print(numStr + "=" + result)
