# Python Functions
"""
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result
"""

"""
1. Creating a function
2. Calling a function
3. Arguments
4. Parameters or Arguments
5. Number of arguments
6. Arbitrary Arguments, *args
7. Keyword Arguments
8. Arbitrary Keyword Arguments, **kwargs
9. Default Parameter Value
10. Passing a List as an Argument
11. Return values
12. The pass statement
13. Recursion
"""

# CREATING A FUNCTION

"""In Python a function is defined using the def keyword"""

def myfunc():
    print("Hello Priya")

# CALLING A FUNCTION
"""To call a function, use the function name followed by parenthesis"""

def myfunc():
    print("Hello Priya")
myfunc()

# ARGUMENTS
"""
1. Information can be passed into functions as arguments
2. Arguments are often shortened to args in Python documentations
3. Arguments are specified after the function name, inside the parentheses
4. Can add as many arguments as you want, just separate them with a comma.
"""

def myfunc(fname):
    print(fname + " Manikandan")

myfunc("Priya")
myfunc("Utsav")
myfunc("Inbav")

# PARAMETERS OR ARGUMENTS ?
"""The terms parameter and argument can be used for the same thing 
 - Information that are passed into a function"""

"""
1. A parameter is the variable listed inside the parentheses in the function definition.
2. An argument is the value that is sent to the function when it is called."""

# NUMBER OF ARGUMENTS

"""A function must be called with the correct number of arguments. Meaning that, if your function expects 2 arguments, 
you have to call the function with 2 arguments, not more, and not less."""

# Expects 2 arguments and Get 2 arguments
#If you try to call the function with 1 or 3 arguments, you will get an error

def myfunc(fname,lname):
    print(fname + " " + lname)
myfunc("Priya", "Manikandan")

# ARBITRARY ARGUMENTS - *args
"""
1. If you do not know how many arguments that will be passed into your function, 
   add a * before the parameter name in the function definition.

2. This way the function will receive a tuple of arguments, and can access the items accordingly"""

def myfamily(*kids):
    print("The youngest in my family is " + kids[3])
myfamily("Mani", "Priya", "Utsav", "Inbav")

# KEYWORD ARGUMENTS - *kwargs
"""
You can also send arguments with the key = value syntax.

This way the order of the arguments does not matter

The phrase Keyword Arguments are often shortened to kwargs in Python documentations.
"""

def myfamily(child3, child2, child1):
  print("The youngest child is " + child3)

myfamily(child1 = "Utsav", child2 = "Deeku", child3 = "Inbav")


# ARBITRARY KEYWORD ARGUMENTS - **kwargs

"""
   If you do not know how many keyword arguments that will be passed into your function, 
   add two asterisk: ** before the parameter name in the function definition.

   This way the function will receive a dictionary of arguments, and can access the items accordingly 
"""

def myfamily(**kid):
  print("His last name is " + kid["lname"])

myfamily(fname = "Utsav", lname = "Manikandan")

# DEFAULT PARAMETER VALUE
"""If we call the function without argument, it uses the default value"""

def my_func(lang = "Tamil"):
    print("I speak" + " " + lang)

my_func("English")
my_func() # default value is automatically taken if there is no argument written

# PASSING A LIST AS AN ARGUMENT
"""
    You can send any data types of argument to a function (string, number, list, dictionary etc.)
    and it will be treated as the same data type inside the function.

Example:  If you send a List as an argument, it will still be a List when it reaches the function
"""

def myfunction(food):
    for x in food:
        print(x)
fruits = {"apple","banana","mango"}
vegs= {"carrot","raddish","beetroot"}
myfunction(fruits)
myfunction(vegs)

"""
 You made a function called my_function() which in this case takes in the input of food shown by the parentheses brackets. 
 my_function(food)

 So whenever you want to call my_function() later down the line, you will be required to give it an input.
 
The input in this case can be any iterable things. 
(strings, lists, tuples, sets, dictionaries, etc)
 
Iterables are anything that you can loop over.
 
 So in a sense, food means fruits.
 
 And x "turns" into each iterable value, first as apple then prints itself,
  then turns into banana and prints itself, etc."""

# RETURN VALUE
"""To let a function return a value, use the return statement"""

def myfunc(num):
     return num * 5
print(myfunc(2))
print(myfunc(10))

# THE PASS STATEMENT
"""
 Function definitions cannot be empty, but if a function definition is with no content,
 put in the pass statement to avoid getting an error.
 """
def mypassstatement():
    pass

# RECURNSION

""" 
1. Recursion means a defined function can call itself 

2. Recursion is a common mathematical and programming concept It means that a function calls itself. 
   This has the benefit of meaning that you can loop through data to reach a result
   
3. The developer should be very careful with recursion as it can be quite easy to slip into writing 
   a function which never terminates, or one that uses excess amounts of memory or processor power.
   
4. Recursion can be a very efficient and mathematically-elegant 
   approach to programming.
   
5. In this example, 'recurse()' is a function that we have defined to call itself ("recurse").

6. We use the k variable as the data, which decrements (-1) every time we recurse. 
   The recursion ends when the condition is not greater than 0 (i.e. when it is 0)
    
   """

def my_recursion(int):
    if (int > 1):
        result = int + my_recursion(int - 1)
        print(result)
    else:
        result = 0
    return result
print("Recursion numbers")
my_recursion(5)