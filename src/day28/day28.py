'''
Define a class with a generator which can iterate the numbers, which are 
divisible by 7, between a given range 0 and n.
'''

from generator import Generator

generator = Generator(100)
for i in generator.generateNum():
    print("%d\n" %i)