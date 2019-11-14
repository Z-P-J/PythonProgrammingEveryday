'''
Write a program that accepts sequence of lines as input and prints the lines after 
making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
'''
s = input("Please input a string:")
arr = []
for c in s:
    arr.append(c.upper())
print("".join(arr))