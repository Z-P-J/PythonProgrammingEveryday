'''
Write a program which can map() to make a list whose elements are square of 
elements in [1,2,3,4,5,6,7,8,9,10].
'''
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# map()函数：
# Python 2.x 返回列表。
# Python 3.x 返回迭代器。
m = map(lambda x : x ** 2, l)
print([x for x in m])