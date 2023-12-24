# Pyhton Math :

"""
Python has a set of built-in math functions, including an extensive math module,
that allows you to perform mathematical tasks on numbers.
"""

# Built-in Math Functions :

"""The min() and max() functions can be used to find the lowest or highest value in an iterable"""

x = min(5,10,15)
y = max(5,10,15)
print(x)
print(y)


# The abs() function returns the absolute (positive) value of the specified number:

X = abs(-8.5)
print(X)

# The pow(x, y) function returns the value of x to the power of y (xy).

Y = pow(5,3) # 5*5*5
print(Y)

# The Math Module :

"""
Python has also a built-in module called math, which extends the list of mathematical functions.

To use it, you must import the math module

When you have imported the math module, you can start using methods and constants of the module

The math.sqrt() method for example, returns the square root of a number"""

import math
x = math.sqrt(3)
print(x)

""" 
The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() 
method rounds a number downwards to its nearest integer, and returns the result
"""

import math
X = math.ceil(1.5)
print(X)

import math
X = math.floor(1.5)
print(X)

""" The math.pi constant, returns the value of PI (3.14...)"""

import math
Y = math.pi
print(Y)




