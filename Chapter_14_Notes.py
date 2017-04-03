"""
Class variables vs instance variables:
Instance variables belong to individual objects.
Class variables belong to the object that Python creates for each class definition.

You define class variables like regular variables but you must define them inside of a class.
You can access them with class objects, and with an object created with a class object.
You access them the same way you access instance variables: preceeding the variable name with self.
Class variables allow you to share data between all of the instances of a class without relying on global variables.
"""

class Rectangle():
    recs = []

    def __init__(self, w, l):
        self.width = w
        self.length = l
        self.recs.append((self.width, self.length))

    def print_size(self):
        print("{} by {}".format(self.width, self.length))

r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r2 = Rectangle(100, 200)

print(Rectangle.recs)

"""
Magic Methods:

Every class in Python inherits from a parent class called Object.
Python utilizes the methods inherited from Object in different situtations - like when you print an object:
You can override the magic Methods

"""
class AlwaysPostive:
    def __init__(self,number):
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n)

x = AlwaysPostive(-20)
y = AlwaysPostive(10)

print(x + y)

"""
'is' keyword is used to evaluate whether two objects are the same object
"""

class Person:
    def __init__(self):
        self.name = 'Bob'

bob = Person()
same_bob = bob
print(bob is same_bob)

another_bob = Person()
print(bob is another_bob)

"""
Can also use keyword 'is' to check if a variable is a value
"""

x = 10
if x is None:
    print("x is None :( ")
else:
    print("x is not None")

x = None
if x is None:
    print("x is None :( ")
else:
    print("x is not None")

"""
object.__repr__(self)
Called by the repr() built-in function and by string conversions (reverse quotes) to compute the “official” string representation of an object.
 If at all possible, this should look like a valid Python expression that could be used to recreate an object with the same
 value (given an appropriate environment). If this is not possible, a string of the form <...some useful description...> should be returned.
 The return value must be a string object. If a class defines __repr__() but not __str__(), then __repr__() is also used when
 an “informal” string representation of instances of that class is required.

This is typically used for debugging, so it is important that the representation is information-rich and unambiguous.
"""

"""
object.__str__(self)
Called by the str() built-in function and by the print statement to compute the “informal” string representation of an object.
This differs from __repr__() in that it does not have to be a valid Python expression: a more convenient or concise representation
may be used instead. The return value must be a string object.
"""

"""

"""
