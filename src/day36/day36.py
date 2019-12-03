'''
Define a function that can receive two integral numbers in string form and 
compute their sum and then print it in console.
'''

def sum(str1, str2):
    return int(str1) + int(str2)

print("3 + 4 = %d" %(sum("3", "4")))