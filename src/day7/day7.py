'''
求s=a+aa+aaa+aaaa+aa...a的值，
其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，
几个数相加有键盘控制。
'''
num = int(input("Input num:"))
n = int(input("Input n:"))
tempNum = num
tempStr = ""
total = 0
for i in range(n):
    total += tempNum
    tempStr += str(tempNum)
    if i < n -1:
        tempNum = num * (10 ** (i + 1)) + tempNum
        tempStr += " + "
    else:
        print(tempStr + " = %d" %total)
    