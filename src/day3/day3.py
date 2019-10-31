'''
有1、2、3、4个数字，能组成多少个互不相同
且无重复数字的三位数？都是多少？
'''

count = 0
for x in range(1, 5):
    for y in range(1, 5):
        if (x != y) :
            for z in range(1, 5):
                if y != z and x != z:
                    num = 100 * x + 10 * y + z
                    count = count + 1
                    print(num)
                    
print("Total is %d" %count)