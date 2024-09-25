#we use classes to define new types, to model real concepts e.g. shopping cart
# A class defines the blueprint/template for creating objects
'''
simple types in python
Numbers
Strings
Booleans
---
complex types in python
Lists
Dictionaries
'''
#capitalize class name(Pascal naming convention)
# (don't use underscores to name, instead capitalize 1st letter of every word)
class Point:
    #some methods:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


#object is an instance of a class
#objects are the actual instances based on that blueprint
#to create an object we type the name of the class and parenthesis
point1 = Point()
point1.draw()
#objects can have attributes
point1.x = 10
point1.y = 20
print(point1.x)

#another object
point2 = Point()
point2.x = 1
print(point2.x)
