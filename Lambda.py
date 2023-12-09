# LAMBDA FUNCTION

"""
A lambda function is a small Anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

SYNTAX
Variable = lambda arguments : expression

"""

math = lambda y : 10 + y
print(math(10))
# or
ans=math(10)
print(ans)

x = lambda a , b , c : a * b * c
print(x(5,6,5))

# Why Use Lambda Functions?
"""

**** Use lambda functions when an anonymous function is required for a short period of time ****

1. The power of lambda is better shown when you use them as an anonymous function inside another function.

2. Say you have a function definition that takes one parameter, 
and that parameter will be multiplied with an unknown number,

3. Use that function definition to make a function that always doubles the number you send in
"""
# example for doubles

def myfunc(n):
    return lambda a : a * n
doubles = myfunc(2)
print(doubles(11))

# Example for triples

def mytrial(x):
    return lambda y : y * x
triples = mytrial(3)
print(triples(11))

# Example foe both doubles and triples

def myfunc(n):
    return lambda a : a * n
doubles = myfunc(2)
triples = mytrial(3)
print(doubles(11))
print(triples(11))


