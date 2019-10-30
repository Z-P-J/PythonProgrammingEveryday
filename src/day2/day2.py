'''
打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，
其各位数字立方和等于该数本身。例如：153是一个“水仙花数”，
因为153=1的三次方＋5的三次方＋3的三次方
'''

# 方法1
for x in range(1, 10):
    for y in range(10):
        for z in range(10):
            num = x * x * x + y * y * y + z * z * z
            if num == (100 * x + 10 * y + z):
                print(num)


# 方法2
for num in range(100, 1000):
    # 注意！！！！！
    # 对于Python2来说，如果两个操作数都是整数，那么结果将向下取整
    # 对于Python3来说，不管操作数有没有浮点数，都是浮点数除法
    # 在Python3环境下，整除用//符号
    x = num // 100
    y = (num - 100 * x) // 10
    z = num % 10
    if (x ** 3 + y ** 3 + z ** 3) == num:
        print(num)