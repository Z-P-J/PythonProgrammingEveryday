'''
Python has many built-in functions, and if you do not know how to use it, 
you can read document online or find some books. But Python has a built-in 
document function for every built-in functions.
Please write a program to print some Python built-in functions documents, 
such as abs(), int(), input() And add document for your own function
'''
print(abs.__doc__)
print("\n--------------------------------------------------\n")
print(int.__doc__)
print("\n--------------------------------------------------\n")
print(input.__doc__)
print("\n--------------------------------------------------\n")

def say_hello():
    '''
    a simple program to print Hello World in your screen.
    '''
    print("Hello World")

say_hello()
print(say_hello.__doc__)
