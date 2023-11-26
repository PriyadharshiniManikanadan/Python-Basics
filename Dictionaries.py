
"""Choosing the right type for a particular data set could mean retention of meaning,
and, it could mean an increase in efficiency or security"""

#Dictionaries
"""
Python dictionaries
Access items
Change items
Add items
Remove items
Loop dictionaries
Copy dictionaries
Nested dictionaries
Dictionaries methods
"""

#1.PYTHON DICTIONARIES
"""
1. Dictionaries are used to store data values.
2. A dictionary is a collection which is ordered, changeable and do not allow duplicates.
3. As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
4. Dictionaries are written with curly brackets, and have keys and values.
"""

#Dictionary

biodata={"Name":"Priya",
         "Gender":"Female",
         "Age": 31}
print(biodata)

#DICTIONARY ITEMS
"""A dictionary is a collection which is ordered, changeable and do not allow duplicates."""

biodata={"Name":"Priya",
         "Gender":"Female",
         "Age": 31}
print("Name -", biodata["Name"])

#Ordered & changable
"""
Dictionaries are defined order, and that order will not change.
Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.

Dictionaries are changeable means we can change, add or remove items after the dictionary has been created.
"""

 #Duplicates are not allowed

biodata={"Name":"Priya",
         "Gender":"Female",
         "Age": 31,
         "Gender":"F"}
print("No duplicates allowed -",biodata)

#Dictionary Length

print(len(biodata))

#Dictionary Items - Data Types

"The values in dictionary items can be of any data type - String, int, boolean, and list"

biodata={"Name":"Priya",
         "Gender":"Female",
         "Age": 31,
         "Gender":"F",
         "Data":True,
         "skin": ["brown", "white", "dark"]
         }
print(biodata)


#type()  -  dict

print(type(biodata))

#Dictionary contructor()
"""It is also possible to use the dict() constructor to make a dictionary."""

biodata=dict(Name = "Priya", Gender = "Female", Age = 31)
print("Dictionary constructor -",biodata)

#1.ACCESS ITEMS

"""
1. You can access the items of a dictionary by referring to its key name, inside square brackets.

2. There is also a method called "get()" that will give you the same result.
"""

biodata={"Name":"Priya",
         "Gender":"Female",
         "Age": 31,
         "Gender":"F",
         "Data":True,
         "skin": ["brown", "white", "dark"]
         }
x=biodata["Data"]
print("Access by index -",x)

#get () method

X = biodata.get("Gender")
print("get method -",X)

#Get keys - Key() method - to get all key names

biodata={"Name":"Priya",
         "Gender":"Female",
         "Age": 31,
         "Gender":"F",
         "Data":True,
         "skin": ["brown", "white", "dark"]
         }

x = biodata.keys()
print(x) # before the change

biodata["DOB"]=(9,"Aug",1992)
print(biodata)
print(x) # after the change

# Get values - value() method to get all the values of the dictionaries

y=biodata.values()
print(y) # before the chnage

biodata["Name"]= "Priyadharshini"
print(y) # after the change

# Get Items - items() method to get all items in the dictionaries
#Get a list of the key:value pairs

z=biodata.items()
print(z)

#Add a new item to the original dictionary, and see that the items list gets updated as well:

biodata["Country"] = "India"
print(biodata) #after the change

#Check if key exist

biodata={"Name":"Priya",
             "Gender":"Female",
             "DOB": (9, 'Aug', 1992),
             "Age": 31,
             "Gender":"F",
             "Data":True,
             "skin": ["brown", "white", "dark"],
             "Country": "India"
             }
if "Name" in biodata:
    print("yes it is present")

if "Age" in biodata:
    print("yes it is present")

#To check
print("To check-",biodata)

#2. CHANGE ITEMS
"""You can change the value of a specific item by referring to its key name"""

biodata["Country"]="USA"
print("Changing the values-",biodata)

#Update Dictionary
"""
1. The update() method will update the dictionary with the items from the given argument.

2. The argument must be a dictionary, or an iterable object with key:value pairs.
"""
biodata={"Name":"Priya",
         "Gender":"Female",
         "DOB": (9, 'Aug', 1992),
         "Age": 31,
         "Gender":"F",
         "Data":True,
         "skin": ["brown", "white", "dark"],
         "Country": "India"
         }
biodata.update({"skin": "dusky"})
print("Update() method-",biodata)

#3. ADD ITEMS
"""Adding an item to the dictionary is done by using a new index key and assigning a value to it"""

biodata["State"] = "Tamil Nadu"
print(biodata)

#Update dictionary
"""
1.The update() method will update the dictionary with the items from a given argument. 
2.If the item does not exist, the item will be added.
3.The argument must be a dictionary, or an iterable object with key:value pairs.
"""

X=biodata.update({"State":"TamilNadu"})
print(biodata)

#4.Remove items
 #"""pop(), popitem() del, clea(),"""

#pop() - The pop() method removes the item with the specified key name

biodata={"Name":"Priya",
         "Gender":"Female",
         "DOB": (9, 'Aug', 1992),
         "Age": 31,
         "Gender":"F",
         "Data":True,
         "skin": ["brown", "white", "dark"],
         "Country": "India"
         }

biodata.pop("Data")
print("pop() method-",biodata)

#popitem() - The popitem() method removes the last inserted item
# (in versions before 3.7, a random item is removed instead)

biodata.popitem()
print("popitem()-",biodata)

#del - The del keyword removes the item with the specified key name

del biodata["skin"]
print(biodata)

#The del keyword can also delete the dictionary completely
#this will cause an error because "thisdict" no longer exists.
#del biodata
#print(biodata)

 #clear() - The clear() method empties the dictionary

#biodata.clear()
#print("Clear() method - ", biodata)

#5.LOOP DICTIONARIES

biodata={"Name":"Priya",
         "Gender":"Female",
         "DOB": (9, 'Aug', 1992),
         "Age": 31,
         "Gender":"F",
         "Data":True,
         "skin": ["brown", "white", "dark"],
         "Country": "India"
         }

#keys - 2 different methods to get the keys through for loop
for x in biodata:
    print("Keys -",x)

for x in biodata.keys():
    print("Keys -",x)

# Values - 2 different methods to get the values through for loop
for X in biodata:
    print("Values -",biodata[X])

for X in biodata.values():
    print("Values -",X)

#Items - 2 different methods to get the values through for loop
for x,y in biodata.items():
    print(x,y)

#6.COPY DICTIONARIES

biodata={"Name":"Priya",
         "Gender":"Female",
         "DOB": (9, 'Aug', 1992),
         "Age": 31,
         "Gender":"F",
         "Data":True,
         "skin": ["brown", "white", "dark"],
         "Country": "India"
         }
priya_data=biodata.copy() # copy() method
print("copy() method -", priya_data)

priya_data=dict(biodata) # dict() method
print("dict() method -",priya_data)

#7. NESTED DICTIONARIES
"""A dictionary can contain dictionaries, this is called nested dictionaries."""

Exams = {
    "Trimester1" : {"June to August"},
    "Trimester2" : {"September to December"},
    "Trimester3" : {"January to March"}
}
print(Exams)

"""Or, if you want to add three dictionaries into a new dictionary"""

Trimester1 = {"June" : "August"}
Trimester2 = {"September" : "December"}
Trimester3 = {"January" : "March"}

My_Exams={"Trimester1" : Trimester1, "Trimester2" : Trimester2, "Trimester3" : Trimester3}
print(My_Exams)


#Example  2

myfamily= {
    "child1" : {"name" : "Utsav", "year" : 2016},
    "child2" : {"name" : "Inbav", "year" : 2022}
}
print("myfamily -",myfamily)

child1={"name" : "Utsav", "year" : 2016},
child2={"name" : "Inbav", "year" : 2022}

myfamily = {"child1" : child1,
              "child2" : child2 }
print("My_children -", myfamily)

#Access Items in Nested Dictionaries
"""To access items from a nested dictionary, you use the name of the dictionaries, 
    starting with the outer dictionary"""

myfamily={
    "child1" : {"name" : "Utsav", "year" : 2016},
    "child2" : {"name" : "Inbav", "year" : 2022}
}
print("Access items - ",myfamily["child1"]["name"])
print("Access items - ",myfamily["child2"]["name"])

#DICTIONARIES METHODS

"""
clear()     	Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()       	Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary
"""
#fronkeys()
x=("A", "B", "C")
y=("Alphabet")
method=dict.fromkeys(x,y)
print(method)