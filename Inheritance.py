# INHERITANCE

"""
1. Inheritance allows us to define a class that inherits all the methods and properties from another class.

2. Parent class is the class being inherited from, also called base class.

3. Child class is the class that inherits from another class, also called derived clasS
"""

# Create a Parent Calss

"""Any class can be a parent class, so the syntax is the same as creating any other class"""

# Parent class:
# Create a class named Person, with firstname and lastname properties, and a printname method


class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

P1 = Person("Priya", "Manikandan")
P1.printname()

# Create a Child class:
# Create a class named Student, which will inherit the properties and methods from the Person class

class student(Person):  #  Use the pass keyword when you do not want to add any other properties or methods to the class.
    pass

# Use the Student class to create an object, and then execute the printname method

P2 = student("Utsav", "Manikandan")
P2.printname()

# Add the __init__() Function

"""we have created a child class that inherits the properties and methods from its parent.

Now, We want to add the __init__() function to the child class (instead of the pass keyword)"""


"""
1. The __init__() function is called automatically every time the class is being used to create a new object

2. When you add the __init__() function, the child class will no longer inherit the parent's __init__() function

3. To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:"""

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# The child's __init__() function overrides the inheritance of the parent's __init__() function.
#To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

# Example

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self,fname,lname)


x = Student("Inbav", "Ravimanya")
x.printname()

# Super() Function :

"""By using the super() function, you do not have to use the name of the parent element,
   it will automatically inherit the methods and properties from its parent."""

class Home:
    def __init__(self):
        print("Iam from parent init function")
    def func1(self):
        print("Iam from fun1")

class Office(Home):
    def __init__(self):
        super().__init__()
        print("Iam from child init function")
    def func2(self):
        print("Iam from fun2")

object1 = Office()
object1.func1()
object1.func2()

# ADD PROPERTIES

class Person:
    def __init__(self,fname,lname):
     self.fname = fname
     self.lname = lname

    def printname(self):
        print(self.fname , self.lname)

class student(Person):
    def __init__(self,fname,lname,year):
     super().__init__(fname,lname)
     self.year = year

x = student("Priya","Manikandan",2019)
print(x.year)

# ADD METHODS:

"""If you add a method in the child class with the same name as a function in the parent class, 
the inheritance of the parent method will be overridden."""

class Person:
    def __init__(self,fname,lname):
     self.fname = fname
     self.lname = lname

    def printname(self):
        print(self.fname , self.lname)

class student(Person):
    def __init__(self,fname,lname,year):
     super().__init__(fname,lname)
     self.year = year

    def Welcome(self):
        print("welcome", self.fname,self.lname, "of the class", self.year)

y = student("Priya", "Manikandan", 2019)
y.Welcome()

