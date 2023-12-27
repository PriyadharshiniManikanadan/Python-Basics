#Regular Expression

"""A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern"""

# RegEx Module

"""
Python has a built-in package called re, 
which can be used to work with Regular Expressions.

Import the re module"""

import re

# RegEx in Python

# When you have imported the re module, you can start using regular expressions

import re
string = "Learning Python"
result = re.findall("Learn",string)
print(result)

# RegEx Functions :

"""The re module offers a set of functions that allows us to search a string for a match:

Function	          Description
findall	      Returns a list containing all matches
search	      Returns a Match object if there is a match anywhere in the string
split	      Returns a list where the string has been split at each match
sub	          Replaces one or many matches with a string
"""

# 1. Findall()

"""The findall() function returns a list containing all matches.

The list contains the matches in the order they are found.

If no matches are found, an empty list is returned"""

import re
txt = "learning python basics"
result = re.findall("sics",txt)
print(result)

import re
txt = "learning python basics"
result = re.findall("abc",txt)
print(result)

# 2. Search()

"""
The search() function searches the string for a match, and returns a Match object if there is a match.

If there is more than one match, only the first occurrence of the match will be returned

If no matches are found, the value None is returned"""

import re
txt1 = "learning python basics"
x = re.search("pyth",txt)
print(x.start())

import re
txt1 = "learning python basics"
x = re.search("pyth",txt)
print(x.span())

import re
txt1 = "learning python basics"
x = re.search("@",txt)
print(x)

# Split()

"""The split() function returns a list where the string has been split at each match

You can control the number of occurrences by specifying the maxsplit parameter"""

import re
txt = "learning python basics, have a great day"
x = re.split(" ",txt)
print(x)

import re
txt = "learning python basics, have a great day"
x = re.split(" ",txt,3)
print(x)

# Sub() function :

"""The sub() function replaces the matches with the text of your choice"""

import re
txt = "learning python basics, have a great day"
x = re.sub("a", "A", txt)
print(x)

import re
txt = "learning python basics, have a great day"
x = re.sub("a", "A", txt, 2)
print(x)

# Match Object :

import re
txt1 = "learning python basics"
x = re.search("pyth",txt)
print(x.start())

import re
txt1 = "learning python basics"
x = re.search("pyth",txt)
print(x.span())

import re
txt1 = "learning python basics"
x = re.search("@",txt)
print(x)