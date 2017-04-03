#Create Rectangle and Square classes with a method called calculate_perimeter that calculates the perimeter
#of the shapes they represent.
#Create Rectangle and Square objects and call the method on both of them

#Define a method in your Square class called change_size that allows you to pass in a number that increases or
#decreases (if a number is negative) each side of a Square object by that number.
class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_perimeter(self):
        return 2 * self.length + 2 * self.width

class Square():
    def __init__(self, width):
        self.width = width
    def calculate_perimeter(self):
        return self.width * 4
    def change_size(self, change):
        self.change = change
        self.width = self.width + change

a_rectangle = Rectangle(2, 4)
a_square = Square(2)

a_rectangle.calculate_perimeter()
a_square.calculate_perimeter()
a_square.change_size(2)

#Create a class called Shape. Define a method in it called what_am_i that prints "I am a shape" when called.
#Change  your Square and Rectangle classes from the previous challeges to inherit from Shape, create Square and Rectangle
#objects, and call the new method on both of them.


class Shape():
    def i_am(self):
        print("I am a shape" )


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Shape):
    def __init__(self, width):
        self.width = width
    def calculate_perimeter(self):
        return self.width * 4
    def change_size(self, change):
        self.change = change
        self.width = self.width + change

a_rectangle = Rectangle(2, 3)
a_square = Square(2)

a_rectangle.i_am()
a_square.i_am()

#Create a class called Horse and a class called Rider. Use Composition to model a horse that has a rider.

class Rider():
    def __init__(self, name):
        self.name = name


class Horse():
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider

a_rider = Rider("bob")
a_horse = Horse("seabisket", a_rider)

a_horse.rider.name
