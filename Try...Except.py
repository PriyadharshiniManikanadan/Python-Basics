# Exception Handling

"""
When an error occurs, Python will normally stop and generate an error message.

These exceptions can be handled using the try statement
"""


# try block - The try block lets you test a block of code for errors

# except block - The except block lets you handle the error.

# else -  The else keyword used to define a block of code to be executed if no errors were raised

# finally - The finally block, if specified, will be executed regardless if the try block raises an error or not.

# It ends with error

# a = 10
# b = 0
# try:
#     print("The value is :", a / b)


# how to write a code

"""Since the try block raises an error, the except block will be executed.

Without the try block, the program will crash and raise an error"""

a = 10
b = 0
try:
    print("The value is :", a / b)
except:
    print("The value is not divided by Zero, instead provide some valid number")

# Example 2

try:
    print(x)
except:
    print("x is not defined")  # error handling

# Multiple Exceptions

a = 12
b = 0
try:
    print("The final value is :", a/b  )
except ZeroDivisionError:
    print("The value is not divided by zero")
except NameError:
    print("Invalid value given")
finally:
    print("try except else finally is finished")

# Finally

"""This can be useful to close objects and clean up resources"""

try:
    f = open(abc.txt)
    try:
       f.write("Priya MAnikandan")
    except:
        print("something went wrong wen writing")
    finally:
        f.close()
except:
    print("someting went wrong when closing a flie")

# Raise an exception :

"""
 As a Python developer you can choose to throw an exception if a condition occurs.

To throw (or raise) an exception, use the raise keyword.
"""

x = -1

if x < 0:
    raise Exception("Sorry, no nubers below Zero")


