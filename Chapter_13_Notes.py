"""
The Four Pillars of Object-Oriented Programming
Encapsulation
Abstraction
Polymorphism
Inheritance
"""

"""
Encapsulation: refers to two concepts:

Objects group variables (states) and methods (for altering state or doing calculation that use state)
in a single unit - the object

A class's internal data is hiden from the client (code outside the class), so it cannot be accessed outside the class.
"""

class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n


data_one = Data()
data_one.nums[0] = 100
print(data_one.nums)

data_two = Data()
data_two.change_data(0, 100)
print(data_two.nums)

"""
private variables and private methods adress issue where objects can access the code that implements the various
methods, but the client cannot
Python does not have private variables
In Python, if you have a variable or method the caller should not access, you preceed the name with an underscore
Python programmers know if it starts with an underscore, they shouldn't use it
but still are able to at their own risk
"""

class PublicPrivateExample:
    def __init__(self):
        self.publc = "Safe"
        self._unsafe = "Unsafe"

    def public_method(self):
        #client can use this
        pass

    def_unsafe_method(self):
        #clients shouldn't use
        pass


"""
Abtraction: is the process of "taking away or removing characteristics from something in order to reduce it to a
set of essential characteristics

You use abtraction in OOP when you model objects using classes and omit unnecessary details.
"""

"""
Polymorphism: the ability (in programming) to present the same interface for different underlying forms (data types)
An interface is a function or a method
"""

print("Hello World") #string
print(200) #int
print(200.1) #float

"""
The built in function 'type' returns the data type of the object
"""

type("Hello World") #string
type(200) #int
type(200.1) #float

"""
Inheritance in programming is similar to genetic inheritance
When you create a class, it can inherit methods and variables from another class.
Parent class and Child class.
"""

class Shape():
    def __init__(self, w, l):
        self.width = w
        self.length = l
    def print_size(self):
        print("""{} by {}
              """.format(self.width,
                         self.length))

my_shape = Shape(20, 25)
my_shape.print_size()

"""
pass the parent class to the child class as a parameter
"""

class Square(Shape):
    pass

a_square = Square(20, 20)
a_square.print_size()

"""
You can override parent methods in the child class using the same method name and add new methods
"""

class Shape():
    def __init__(self, w, l):
        self.width = w
        self.length = l
    def print_size(self):
        print("""{} by {}
              """.format(self.width,
                         self.length))
class Square(Shape):
    def area(self):
        return self.width * self.length
    def print_size(self):
        print("""I am {} by {}
              """.format(self.width,
                         self.length))
a_square = Square(2, 4)
a_square.print_size()

"""
Composition models the "has a" relationship
Passing a class as the parameter of another class
"""

class Dog():
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person():
    def __init__(self, name):
        self.name = name

mick = Person("Mick Jagger")
stan = Dog("Stanley", "Bulldog", mick)

print(stan.owner.name)
