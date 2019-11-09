'''
Write a program which accepts a sequence of comma-separated numbers from console and 
generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
元组与列表的区别：元组中的元素不能修改
'''
str = input("Please input a sequence of comma-separated numbers:")
list = str.split(",")
t = tuple(list)
print(list)
print(t)