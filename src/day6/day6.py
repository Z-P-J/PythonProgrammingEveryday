'''
输入一行字符，分别统计出其中
英文字母、空格、数字和其它字符的个数。
'''
str = input("Please input a string:")

alphas = 0
spaces = 0
nums = 0
others = 0
for c in str:
    if c.isalpha():
        alphas += 1
    elif c.isspace():
        spaces += 1
    elif c.isnumeric():
        nums += 1
    else:
        others += 1

print("string = %s." %str)
print("The number of alphas is %d." %alphas)
print("The number of spaces is %d." %spaces)
print("The number of nums is %d." %nums)
print("The number of others is %d." %others)