# Polymorphism:

"""
    The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators
 with the same name that can be executed on many objects or classes.
 """""

# Function Polymorphism:

"""An example of a Python function that can be used on different objects is the len() function"""

# String
# returns the number of characters:

print(len("welcome to thwe world"))

# Tuple
#For tuples len() returns the number of items in the tuple

x = ("red","Blue","Green","Yellow")
print(len(x))

# Dictionary
# For dictionaries len() returns the number of key/value pairs in the dictionary

Dic = {"Course" : "Data Science", "Subject" : "Python"}
print(len(Dic))

# Class Polymorphism:
"""
Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move()"""

class car:
    def move(self):
        model = "Mallibu"
        year = "2021"
        print("My new car is :", model, "bought in", year)

class Boat:
    def move(self):
        model = "Nano"
        year = "2018"
        print("My old car is :", model, "bought in", year)

Car1 = car()
Boat1 = Boat()
Car1.move()
Boat1.move()

# for x in(Car1,Boat1):
#     x.move()
#Look at the for loop at the end. Because of polymorphism we can execute the same method for all three classes

# Inheritance in Polymorpism:
"""
    
1. What about classes with child classes with the same name? Can we use polymorphism there?
    
2. Make a parent class called Vehicle, and make Car, Boat, Plane child classes of Vehicle,
    the child classes inherits the Vehicle methods, but can override them"""

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()

# Child classes inherits the properties and methods from the parent class

# In the example above you can see that the Car class is empty, but it inherits brand, model, and move() from Vehicle

# The Boat and Plane classes also inherit brand, model, and move() from Vehicle,
# but they both override the move() method.
# Because of polymorphism we can execute the same method for all classes.