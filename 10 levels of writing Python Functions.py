# Basic Function

def func():
    print("Hello Python")
func()
print("===========================================")

# Fuctions with parameters

def data(name):
    print("My name is " + name)
data("Priya")
print("===========================================")

# Return values

def add(a,b):
    return a + b
print(add(5,5))
print(add(5,10))
print("===========================================")

# Default parameters

def greet(name="Python"):
    print(f"hello, {name}!")
greet()
print("===========================================")

# Docstring

def add(a,b):
    return a + b
add(1,2)

def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2
square(2)
print("===========================================")

# Scope Variable

global_var = 10

def my_fun():
    local_var = 5
    print(global_var + local_var)
my_fun()

print("===========================================")

# Recursion

def function(A):
    if (A>0):
        result = A + function(A - 1)
        print(result)
    else:
        result = 0
    return result
print("Recursion Numbers")
function(6)

print("===========================================")

# Lambda Functions
x = lambda a : 10 + a
print("Lambda:",x(5))

print("===========================================")
y = lambda a,b,c : a*b*c
print(y(5,2,4))

print("===========================================")







