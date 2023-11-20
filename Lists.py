#List
"""
1.Python List
2.Access list items
3.Change list items
4.Add list items
5.Remove list items
6.Loop lists
7.List comprehension
8.Sort lists
9.Copy lists
10.Join lists
11.List Methods
"""
#  1.Python Lists
#4 built in data types = list,set,tuple,dict
# Lists are created using square brackets
#List items are ordered, changeable, and allow duplicate values.


#Ordered
"""There are some LIST METHODS that will change the order, but in general: 
 the order of the items will not change."""

# Changeable
"""The list is changeable, meaning that we can change, add, 
and remove items in a list after it has been created."""

#Allow duplicates
"""Since lists are indexed, lists can have items with the same value"""
mycolors = ["red", "blue", "green", "red", "yellow"]
print(mycolors)

#List length -
colors=["red","blue"]
print(len(colors))

#List items
"""List items can be of any data type"""
colors=["red","blue"]
count=[1,2]
state=["true","false"]
print(colors,count,state)

"""List items can contain any data type"""
list=["true","priya",2,]
print(list)

#type() - to find the data type of a list
colors=["red","blue"]
count={1,2}
state=("true","false")
print(type(colors))
print(type(count))
print(type(state))

#List() construct - double brackets
"""It is also possible to use the list() constructor 
   when creating a new list"""
# mycolors = list(("red","blue","green","yellow"))
# print(mycolors)

#Python collections- Arrays
"""
List              Tuple          Set            Dic
1.ordered         ordered        unordered      ordered  
2.changable       unchangable    unchangable    changable
3.allow dupl      allow dupl     No dupl        No dupl"""

#   2.Access Lists Items
"""Can access them by referring to the index number
 The first item has index 0."""

mycolors = ["red", "blue", "green", "red", "yellow"]
print(mycolors[2])

#Negative indexing
#starts from the end as -1 ,-2,-3....
mycolors = ["red", "blue", "green", "red", "yellow"]
print(mycolors[-1])
print(mycolors[:4]) # range of index
print(mycolors[:-2]) #range of negative index
print(mycolors[-3:])

#Check "if" item exixts
mycolors = ["red", "blue", "green", "red", "yellow"]
if "grey" in mycolors:
    print("yes, it is present")
else:
    print("No,it is not present")

if "blue" in mycolors:
        print("yes, it is present")
else:
        print("No,it is not present")

#  3.Change list items
"""To change the value of a specific item, 
   refer to the index number"""

mycolors = ["red", "blue", "green", "red", "yellow"]
mycolors[2]="grey" #change 1 item value
print(mycolors)

mycolors[2:5]="grey","orange","pink" #change the range of item values
print(mycolors)

#Insert() method
"""To insert a new list item, without replacing 
any of the existing values, we can use the insert() method."""
fruits=["apple","mango","orange"]
fruits.insert(1,"avacado")
print(fruits)

#Add item list - append() method
"""To add an item to the end of the list, 
   use the append() method"""
fruits=['apple', 'avacado', 'mango', 'orange']
fruits.append("pomo")
print(fruits)

#Extend() List
"""To append elements from
   another list to the current list, use the extend() method"""
fruits=['apple', 'avacado', 'mango', 'orange']
mycolors = ["red", "blue", "green", "red", "yellow"]
fruits.extend(mycolors)
print(fruits)

#Add any Iterable - any data type in a list
"""The extend() method does not have to append lists, 
you can add any iterable object (tuples, sets, dictionaries etc.)"""
list=["priya",30,"Manikandan",34.5,"true"]
Tuple=("priya","mani")
set={"couple"}
list.extend(Tuple)
print(list)
list.extend(set)
print(list)

#   4.Remove items from the lists
fruits=['apple', 'avacado', 'mango', 'orange']
fruits.remove("avacado") #The remove() method removes the specified item
print(fruits)

#The pop() method removes the specified index
"""If you do not specify the index, the pop() method removes the last item."""
fruits.pop(2)
print(fruits)

fruits.pop()
print(fruits)

#del keyword
"""The del keyword also removes the specified index
   The del keyword can also delete the list completely."""
alpha=["a","b","c"]
del alpha[1]
print(alpha)

#del alpha
#print(alpha) ##this will cause an error because you have succsesfully deleted

#Clear() method
"""The list still remains, but it has no content"""
Names=["Priya","Mani","Utsav","Inbav"]
Names.clear()
print(Names)

#Loop lists
"""You can loop through the list items by using a "for" loop
   Print all items in the list, one by one"""

colors=["red","blue","green","yellow"]
for x in colors:
    print(x)

for Parts in "cpu": #values are given directly
    print(Parts)

#Loops through the index num
"""You can also loop through the list items by referring to their index number.
Use the range() and len() functions to create a suitable iterable"""

colors=["red","blue","green","yellow"]
for result in range(len(colors)):
    print(result)

for numbers in range(5,100,10): #5-start, 100-end, 10 - intervels
    print(numbers)
else:
    print("Number stops here")

#While Loop
"""Use the len() function to determine the length of the list, 
   then start at 0 and loop your way through the list items by 
   referring to their indexes.
 Remember to increase the index by 1 after each iteration"""

# While Loop
Names=["Priya","Mani","Utsav","Inbav"]
x=0
while x < len(Names):
    print(Names[x])
    x+=1

#Example 1
x=0
while x < 10:
    print("inside loop")
    x+=2
else:
    print("outside loop")

#Example 2
count=0
while count < 5:
    print (count, "is less than ")
    count += 1
else:
    print(count, "is not less than 5")

#Looping Using List Comprehension
"""List Comprehension offers the shortest syntax 
   for looping through lists:
  1. Based on a list of fruits, you want a new list, containing only 
     the fruits with the letter "a" in the name.
  2. Without list comprehension you will have to write 
     a for statement with a conditional test inside"""

colors=["red","blue","green","yellow"]
newcolors=[]

for x in colors:
    if "b" in x:
        newcolors.append(x)
        print(newcolors)

#List comprhension: what will be the single line syntax

colors=["red","blue","green","yellow"]
new_colors=[x for x in colors if "y" in x]
print(new_colors)


#With list comprehension you can do all that with only one line of code:
fruits=["apple","mango","guava"]

#fruit = [expression for item in iterable if condition == True]

#Condition
#The condition is like a filter that only accepts the items that valuate to True

fruit=[x for x in fruits if "guava" != x]
print(fruit)

fruit=[x for x in fruits if "g" in x]
print(fruit)

#The condition is optional and can be omitted:
fruit=[x for x in fruits]
print(fruit)

#Iterable
#The iterable can be any iterable object, like a list, tuple, set etc.

Numbers=[x for x in range(10)]
print(Numbers)

Numbers=[x for x in range(10,20) if x <= 15]
print(Numbers)

#Expression
"""The expression is the current item in the iteration, 
   but it is also the outcome, 
   which you can manipulate before it ends up like a list item in the new list"""

list=["name","age","dob"]
newlist=[x.upper() for x in list]
print("The expression used here is upper case: ", newlist)

newlist=[x.upper() for x in list if "d" in x]
print(newlist)

#You can set the outcome to whatever you like:
#Set all values in the new list to 'hi':

colors=["red","blue","green","yellow"]
new=["priya" for x in colors]
print(new)

"""The expression can also contain conditions, not like a filter, 
but as a way to manipulate the outcome:"""

"""colors=["red","blue","green","yellow"]
newline=[x if x != "blue" else "pink" if x in colors]
print(newline)"""

#SORT LISTS
#Sort list Alphanumerically
colors=["red","blue","green","yellow"]
colors.sort() #from a-z in acsending order
print(colors)

#Sort Numerically
numbers=[50,40,20,30,10]
numbers.sort() # in acsending order
print(numbers)

#Sort Descending
"""To sort descending, use the keyword argument reverse = True"""
numbers=[50,40,20,30,10]
numbers.sort(reverse=True)
print(numbers)

colors=["red","blue","green","yellow"]
colors.sort(reverse=True)
print(colors)

#Customize sort function
"""
1.You can also customize your own function by using 
   the keyword argument "key = function".
   
2.The function will return a number that will
   be used to sort the list (the lowest number first)
   
3.It's sorting your original values from 
  smallest to largest AFTER going through your key
  
4."abs" is supposed to return the distance of a number from 0
  """

def mysort(n):
    return abs(n-10)
numbers=[10,30,20,50,40]
numbers.sort(key=mysort)
print(numbers)


# function to return the second element of the
# two elements passed as the parameter
def sortSecond(val):
    return val[1]

# list1 to demonstrate the use of sorting
# using  second key

list1 = [(1, 2), (3, 3), (1, 1)]

# sorts the array in ascending according to
# second element
list1.sort(key=sortSecond)
print(list1)

# sorts the array in descending according to
# second element
list1.sort(key=sortSecond, reverse=True)
print(list1)

#Example1

def sortSecond(val):
    return val[1]
list1 = [(1, 2), (3, 3), (1, 1)]
list1.sort(key=sortSecond)
print(list1)
list1.sort(key=sortSecond, reverse=True)
print(list1)

#Example 2

def mysort(num): # num is parameter, mysort is function
    return num[0]
list1=[(1,4),(3,5),(2,3)]
list1.sort(key=mysort)
print(list1)
list1=[(1,4),(3,5),(2,3)]
list1.sort(key=mysort,reverse=True)
print(list1)

#Case Sensitive Sort
"""By default the sort() method is case sensitive, 
resulting in all capital letters being sorted before lower case letters"""

Fruits=["apple","Banana","mango","Kiwi"]
Fruits.sort()
print(Fruits)

"""Luckily we can use built-in functions 
as key functions when sorting a list."""

Fruits=["apple","Banana","mango","Kiwi"]
Fruits.sort(key=str.lower)  # will be in default ascending order
# case-insensitive sort function can be used using key function (str.upper)
print(Fruits)

#Reverse Order
# It will just reverse the order of the list.
colors=["Red","blue","Green","yellow"]
colors.reverse()
print(colors)

#Copy Lists
"""
1. You cannot copy a list simply by typing list2 = list1,
   because: list2 will only be a reference to list1
   and changes made in list1 will automatically also be made in list2.

2. There are ways to make a copy, one way is to use the built-in List method copy()"""

lang=["python","c","java"]
new_lang=lang.copy()
print(new_lang)

#lang1=["python","sql","java"]
# new_lang1=list(lang1)
# print(new_lang1)


#Join list
#use + operater is the easiest way to join the lists.
alpha=["a","j","k","i","j"]
num=[1,2,3,4,5]
join=alpha+num
print(join)


#Append()

"""Another way to join two lists is by appending all the items 
from list2 into list1, ONE BY ONE"""

alpha=["a","j","k"]
num=[1,2,3,]
for x in num:
    alpha.append(x)
    print(alpha)

#Extend()

"""you can use the "extend()" method, which purpose is 
to add elements from one list to another list"""

list1=["a","b","c"]
list2=["d","e","f",]
list1.extend(list2)
print(list1)

list1=[1,2,3,7,6,6,7,8,9,10]
x=list1.count(6)
print(x)


#LIST METHODS
"""
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
"""