#Define a class called Apple with four instance variables that represent four attributes of an apple.

class Apple():
    def __init__(self, w, c, t, r):
        self.weight = w
        self.color = c
        self.taste = t
        self.rot = r

#Create a circle class with a method called area that calculates and returns its area
#The create a circle object call area on it, and print the result
#Use  Python's pi function in the built in math module

import math

class Circle():
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

testcircle = Circle(5)

print(testcircle.area())

#Create a Triangle class with a method called area that calculates and returns its area, and print the result

class Triangle():
    def __init__(self,base, height):
        self.base = base
        self.height = height
    def area(self):
        return self.base * self.height / 2

test_triangle = Triangle(2, 4)

print(test_triangle.area())









#Create a Hexagon class with a method called calculate_perimeter that calculates and returns its perometer
#Then crate a hexagon object, call calculate_perimeter and print the result
