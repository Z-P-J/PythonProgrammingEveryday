'''
Write a program that accepts a sentence and calculate the number of upper case 
letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''

s = input("Please enter a sentence:")
uppers = 0
lowers = 0
for c in s:
    if c.isupper():
        uppers += 1
    elif c.islower():
        lowers += 1
print("uppers = %d, lowers = %d" %(uppers, lowers))