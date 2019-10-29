'''
一球从100米高度自由落下，每次落地后反跳回原高度的一半；
再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
'''

print("Hello World!")

total = 0.0
temp = 100.0
for i in range(10):
    # 落地
    total = total + temp
    # 反弹
    temp = temp / 2
    if i == 9:
        print("total = %f\n" % total)
        print("temp = %f\n" %temp)
    total = total + temp