# While Loops
 """
 break statement
 continue statement
 else statement
 """

"""1. With the while loop we can execute a set of statements as long as a condition is true.
2. Remember to increment i, or else the loop will continue forever."""

#Example

i = 0
while i <= 5:
    print(i)
    i += 1

i = 0
while i <= 5:
    i += 1
    print(i)

# The Break Statement
""" With the break statement we can stop the loop even if the while condition is true """

i = 1
while i <= 5:
    print("break", i)
    if i == 3:
      break
    i += 1

# The Continue Statement
"""With the continue statement we can stop the current iteration, and continue with the next"""

i = 1
while i < 6:
    i += 1 # i = i + 1
    if i == 3:
        continue
    print("continue", i)

# The Else statement
"""With the else statement we can run a block of code once when the condition no longer is true"""

i = 2
while i >= 10:
    print(i)
    i += 1
else:
    print("i is no greater than 10")


