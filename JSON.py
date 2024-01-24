
# PYTHON JSON
"""
JSON is a syntax for storing and exchanging data.

JSON is text, written with JavaScript object notation
"""

# Json in Python:

"""Python has a built-in package called json, which can be used to work with JSON data."""
import json

# Parse JSON - Convert from JSON to Python

import json
x =  '{ "name":"John", "age":30, "city":"New York"}'         # some JSON
y = json.loads(x)                                            # parse x:
print(y["age"])                                              # the result is a Python dictionary:

#  Convert from Python to Json

import json
x = ["red","blue","green"]       # python dic
y = json.dumps(x)                # convert from pyton to json
print(y)                         # result as json string

# You can convert Python objects of the following types, into JSON strings:

#Convert Python objects into JSON strings, and print the values:

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# dict  -  Object
# list  -  array
# tuple - array
# string  - str
# int - number
# float - number
# True - true
# False - false
# None  - null

# Format the Result :

import json

x = {"name": "John","age": 30,"married": True,"divorced": False,"children": ("Ann","Billy"),"pets": None,
  "cars": [{"model": "BMW 230", "mpg": 27.5},{"model": "Ford Edge", "mpg": 24.1}]}

print(json.dumps(x))


#  Format the result:

"""
 The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.

The json.dumps() method has parameters to make it easier to read the result:

Use the indent parameter to define the numbers of indents:"""



x = {"name": "John","age": 30,"married": True,"divorced": False,"children": ("Ann","Billy"),"pets": None,
  "cars": [{"model": "BMW 230", "mpg": 27.5},{"model": "Ford Edge", "mpg": 24.1}]}

print(json.dumps(x, indent = 5 ))

# You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate
# each object, and a colon and a space to separate keys from values

# Use the separators parameter to change the default separator:

#x = {"name": "John","age": 30,"married": True,"divorced": False,"children": ("Ann","Billy"),"pets": None,
 # "cars": [{"model": "BMW 230", "mpg": 27.5},{"model": "Ford Edge", "mpg": 24.1}]}

#print(json.dumps(x, indent = 4, seperators = (".","=")))

# Order the result:

"""
The json.dumps() method has parameters to order the keys in the result:

Use the sort_keys parameter to specify if the result should be sorted or not"""


# Example :

x = {"name": "John","age": 30,"married": True,"divorced": False,"children": ("Ann","Billy"),"pets": None,
  "cars": [{"model": "BMW 230", "mpg": 27.5},{"model": "Ford Edge", "mpg": 24.1}]}

print(json.dumps(x, indent=4, sort_keys=True))