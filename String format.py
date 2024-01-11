# string format()

"""
The format() method allows you to format selected parts of a string.

Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?

To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method:
"""

# Example:

price = 50
x = "The price of the fish is {} dollars"
print(x.format(price))

# You can add parameters inside the curly brackets to specify how to convert the value

# Format the price to be displayed as a number with two decimals

price = 50
x = "The price of the fish is {:.2f} dollars"
print(x.format(price))

#Multiple Values

#If you want to use more values, just add more values to the format() method

txt = "My name is {NAME}, Iam {age} years old".format(NAME = "Priya", age = 31)
print("Multiple values: ", txt)

# Index Numbers

Quantity = 5
Item_no = 100
Price = 1205

myorder = "I bought {0} pices of item number {1} for the price of {2}"
print(myorder.format(Quantity,Item_no,Price))

# Named indexes:

Mycar = "I purchased a {carname}, and the model is {year}."
print(Mycar.format(carname = "Nano", year = "2018"))


