'''
Write a program which will find all such numbers which 
are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in 
a comma-separated sequence on a single line.
'''
arr = []
for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        # 注: 下面用到的join函数是字符串操作函数，所以列表arr必须是字符串列表
        arr.append(str(num))
# join(): 将序列中的元素以指定的字符连接生成一个新的字符串。
print(','.join(arr))
