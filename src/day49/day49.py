'''
Write a program which can filter even numbers in a list by using filter function. 
The list is: [1,2,3,4,5,6,7,8,9,10].
'''

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
关于filter()方法, python3和python2有一点不同
Python2.x 中返回的是过滤后的列表, 而 Python3 中返回到是一个 filter 类。
filter 类实现了 __iter__ 和 __next__ 方法, 可以看成是一个迭代器, 有惰性运算的特性, 
相对 Python2.x 提升了性能, 可以节约内存。
'''
evenNums = filter(lambda x : x % 2 == 0, l)
# Python3环境下输出结果：<filter object at 0x0000022EC66BB128>， Python2环境下输出结果：[2, 4, 6, 8, 10]
# print(evenNums)
print([num for num in evenNums])