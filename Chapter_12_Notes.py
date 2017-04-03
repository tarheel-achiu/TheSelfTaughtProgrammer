"""
Functional programming:
Functional programing does not use the global state and therefore avoids side effects.
State is stored in functions.
Functions receive an input and release an output. Sometimes to another function.
All data variables exists within the function and do not effect data varibales in other functions.
"""


"""
Object oriented programing:
State is stored in objects.
Classes define a set of objects that can interact with each other. Similar objects with similar attributes.
Every object is an instance of a class.
Class is a compound statement with a header and suites.
Class names start with a capital letter and in camelCase.
As suite can be a simple statement or a compund statement called a method.
Methods have the same syntax as functions except for two differences:
You must define a method as a suite in a class, and it has accept at least one parameter.
Always name the first parameter of a method self
"""

class [Name]:
    [suites]

class CoolName:
    def __init__(self):
        print("Created!")

"""
You use self to define an instance variable. A variable that belongs to an object.
If you create multiple objects, they can all have diferent instance variable values
"""

self.[variable_name] = [variable_value]

"""
You normally define instance variables inside of a special method called __int__ (initialize)
Orange example:
"""

class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created!")

"Any method surrounded by double underscores like " __init__ "is called a magic method, used for special purposes"

"""
You create a new Orange object with the same syntax you use to call a function.
You do not have to pass self parameter.
Creating a new object is called instantiating a class.
"""

[class_name] ([parameters])

orange1 = Orange(10, "dark orange")

"""
Once you have created an object you can get the value of instance variables with the syntax:
"""
[object_name].[variable_name]

print(orange1.weight)
print(orange1.color)

"""
To change the value of an instance variable with the following syntax:
"""

[object_name].[variable_name] = [new_value]

orange1.weight = 100
orange1.color = "light orange"

"""
Creating more attributes for object and methods to model them
"""

class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")
    def rot(self, days, temp):
        self.mold = days * temp

orange_1 = Orange(6, "light orange")
print(orange_1.mold)
orange_1.rot(10,98)
print(orange_1.mold)

"You can define multiple methods in a class"
