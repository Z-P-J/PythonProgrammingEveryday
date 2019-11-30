'''
Define a class, which have a class parameter and have a same instance parameter
'''

class Person:

    name = "Person"

    def __init__(self, name = None):
        super().__init__()
        self.name = name

person1 = Person("zpj")
print("%s name is %s" %(Person.name, person1.name))

person2 = Person()
person2.name = "zpj"
print("%s name is %s" %(Person.name, person2.name))