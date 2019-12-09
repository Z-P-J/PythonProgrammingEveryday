'''
Define a function which can generate a list where the values are square of 
numbers between 1 and 20 (both included). Then the function needs to print 
the first 5 elements in the list.
'''

def printDict():
    d = list()
    for i in range(1, 21):
        d.append(i ** 2)
    print(d[:5])

printDict()