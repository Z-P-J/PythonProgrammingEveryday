'''
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
'''

num = input("Please enter a number:")
n2 = int("%s%s" %(num, num))
n3 = int("%s%s%s" %(num, num, num))
n4 = int("%s%s%s%s" %(num, num, num, num))
print("%s + %d + %d + %d = %d" %(num, n2, n3 , n4 , (int(num) + n2 + n3 + n4)))
