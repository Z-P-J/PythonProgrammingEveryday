'''
Write a program which accepts a sequence of comma separated 4 digit binary numbers 
as its input and then check whether they are divisible by 5 or not. 
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.
'''

s = input("Please enter a sequence of comma separated 4 digit binary numbers:")
items = [x for x in s.split(",")]
results = []
for item in items:
    num = int(item, 2)
    if num % 5 == 0:
        results.append(item)
print(",".join(results))