'''
Use a list comprehension to square each odd number in a list. The list is input 
by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
'''
s = input("please enter some numbers:")
nums = [int(x) for x in s.split(",")]
list = []
for num in nums:
    if num % 2 != 0:
        list.append(str(num))
print(','.join(list))
