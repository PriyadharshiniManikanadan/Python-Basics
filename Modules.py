# PYTHON MODULES

"""
Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application """

# Create a Module

"""To create a module just save the code you want in a file with the file extension .py"""

#def greeting(name):
   # print("Hello, " + name)


# Use a Module
"""To create a module just save the code you want in a file with the file extension .py

  When using a function from a module, use the syntax: module_name.function_name"""

 # import Modules
 # Modules.greeting("Priya")


# Variables  in Modules :
"""The module can contain functions, as already described, but also variables of all types
 (arrays, dictionaries, objects etc)"""

person1 = {
  "name": "John",
  "age": 36,
  "Gender" : "Female"
}

import Modules
a = Modules.person1["name"]
print(a)

# Naming a module
"""You can name the module file whatever you like, but it must have the file extension .py"""

import Modules as Module
a = Module.person1["age"]
print(a)

# Built in Modules:

"""There are several built-in modules in Python, which you can import whenever you like."""

# Examples - platform module

import platform
x = platform.system()
print(x)

# Using the dir() function:

"""
1. There is a built-in function to list all the function names (or variable names) in a module. 
2. The dir() function can be used on all modules, also the ones you create yourself"""

import platform
x = dir(platform)
print(x)

# Import from Module

"""You can choose to import only parts from a module, by using the from keyword"""

def Modules(name):
  print("My name is : " + name)

Person1 = {"name" : "Priya", "age" : 31, "Gender" : "Female"}

from Modules import person1
print(person1["Gender"])

"""When importing using the from keyword, do not use the module name when referring to elements in the module. 
Example: person1["age"], not mymodule.person1["age"]"""