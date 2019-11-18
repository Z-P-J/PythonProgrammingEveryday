'''
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''
s = input("Please enter a sentence:")
letters = 0
digits = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isdigit():
        digits += 1
print("LETTERS %d\nDIGITS %d" %(letters, digits))