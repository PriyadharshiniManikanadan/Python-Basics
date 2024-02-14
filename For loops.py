# For loop
"""
1. Looping through a string
2. The break statement
3. The continue statement
4. The range() function
5. Else in for loop
6. Nested loops
7. The pass statement
"""
# PYTHON FOR LOOP

"""
*  A for loop is used for iterating over a sequence 
  (that is either a list, a tuple, a dictionary, a set, or a string)
*  With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc
*  The for loop does not require an indexing variable
  """

#example
colors =["red", "blue", "green", "yellow"]
for x in colors:
    print(x)

#1. Looping through a string
"""Even strings are iterable objects, they contain a sequence of characters"""

for x in "green":
    print(x)

# 2. The break statement

"""With the break statement we can stop the loop before it has looped through all the items"""

colors =["red", "blue", "green", "yellow"]
for x in colors:
    print(x)
    if x == "green":
     break

"""Exit the loop when x is "banana", but this time the break comes before the print"""

colors =["red", "blue", "green", "yellow"]
for x in colors:
    if x == "green":
     break
    print("break -", x)

# 3.The continue statement

colors =["red", "blue", "green", "yellow"]
for x in colors:
    if x == "blue":
        continue
    print("continue -", x)

# 4. The range() function

for x in range(5):
    print(x)

    for x in range(2,6):
        print(x)

        for x in range(5,30,5):
            print(x)

# 5. Else in for loop
"""
  The else keyword in a for loop specifies a block of code to be executed when the loop is finished
 
 """

for x in range(5):
     print(x)
else:
     print("finally finished")

"""The else block will NOT be executed if the loop is stopped by a break statement"""

for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("finish")

# The nested loop

"""A nested loop is a loop inside a loop.

The "inner loop" will be executed one time for each iteration of the "outer loop"""

for x in range(2,11):
    for y in range(1,11):
        print(x, "*", y, "=", x*y)


x = [2,7]
y = [5,9]
i = 0
while i < len(x):
    j = 0
    while j < len(y):
        print(x[i],y[j])
        i += 1
        j += 1

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana","cherry"]

for x in adj:
    for y in fruits:
        print(x,y)

# 6. The passs ststement

"""having an empty for loop like this, would raise an error without the pass statement"""

for x in fruits:
 pass

for x in fruits:
    print(x)
    if x == "banana":
        break

print("="*100)

import itertools

for i in itertools.count():
    print(i)
    if i > 4:
        break

print("="*100)

for i in itertools.count(2):
    print(i)
    if i > 4:
        break

print("="*100)

for i in itertools.count(step=2):
    print(i)
    if i > 5:
        break

print("="*100)

for i in itertools.count(5,-1):
    print(i)
    if i < 5:
        break

# By combining it with zip(), you can create tuples that include a counter

l1 = [1,2,3,4,5]
l2 = ['x','y','z','a','b']

print(list(zip(itertools.count(),l1,l2))) # Tuple result

print(list(enumerate(zip(itertools.count(),l1,l2))))   # Nested Tuple result



