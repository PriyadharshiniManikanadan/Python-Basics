#Python Conditions and If statements
"""
Python supports the usual logical conditions from mathematics

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.
"""

#exapmple

a = 1
b = 5
if a < b:
    print("a is less than b")
else:
    print("False")

a = 5
b = 5
if a < b:
        print("a is less than b")
else:
        print("False")

# INDENTATION

a = 5
b = 10
if b > a:
 print("b is greater than a") # you will get an error

a = 5
b = 10
if b > a:
 print("b is greater than a") # you will get an error

 # Elif Statement

 """The elif keyword is : if the previous conditions were not true, then try this condition"."""

 a = 5
 b = 10
 if  a > b:
     print("a is less than b")
 elif a < b:
      print("Elif statement -", "a is less than b")


#Else Statement
"""The else keyword catches anything which isn't caught by the preceding conditions."""

a = 10
b = 10
if a > b:
    print ("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("Else statement -", "a is equal to b")

# Short hand if statement
"""If you have only one statement to execute, you can put it on the same line as the if statement."""

a = 10
b = 20
if a < b: print("shorthandif - ", "a is lesser than b")

#Short hand if...else statement
"""If you have only one statement to execute, one for if, and one for else, you can put it all on the same line"""

a = 10
b = 20
print("A") if a < b else print("B") #This technique is known as Ternary Operators, or Conditional Expressions.

#Can also have multiple else statements on the same line

a = 100
b = 200
print("A") if a > b else print("B") if a == b else print("C")

# AND operators
"""The and keyword is a logical operator, and is used to combine conditional statements"""
a = 10
b = 20
c = 30
if a < b and c > a:
    print("both condition is True")

# OR
"""The or keyword is a logical operator, and is used to combine conditional statements"""
a = 10
b = 20
c = 30
if a > b or c > a:
    print("At least one of the condition is true")

# NOT
"""The not keyword is a logical operator, and is used to reverse the result of the conditional statement"""
a = 10
b = 20
if not a > b:
    print("a is not greater than b")

# NESTED IF
"""You can have if statements inside if statements, this is called nested if statements"""

a = 50

if a > 40:
    print("a is above 10")
    if a < 10:
        print("a is also above 20")
    else:
        print("a is not above 10")

# PASS STATEMENT
"""
if statements cannot be empty, 
but if you for some reason have an if statement with no content, 
put in the pass statement to avoid getting an error
"""

A = 10
B = 15
if A > B:
 pass






