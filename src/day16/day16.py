'''
Write a program that accepts a comma separated sequence of words as input and 
prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
'''

inputStr = input("Please input some strings")
strList = inputStr.split(",")
strList.sort()
print(",".join(strList))

# 参考答案
# items = [ x for x in input().split(',') ]
# items.sort()
# print(','.join(items))

