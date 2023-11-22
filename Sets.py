#SET
"""
Python set
Access set items
Add set items
Remove set items
Loop set
Join set
Set methods
"""

#1.Python Set

"""
Unordered
Unchangeable, but you can remove items and add new items.
The values True and 1 are considered the same value in sets and are treated as duplicates
"""

#set
"""Every time the output changes the order 
cannot be reffered by index"""

Set={"red","blue","green","yellow"}
print(Set)


"""Once a set is created, you cannot change its items, but you can remove items and add new items"""


#Do not allow duplicates
Set={"red","blue","green","yellow","red"}
print("Do not allow dup:", Set)

"The values True and 1 are considered the same value in sets, and are treated as duplicates"

#Get a length of a set
Set={"red","blue","green","yellow","red"}
print(len(Set))

#Set items - Data Types
"""It can of any data types"""

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#A set can contain different data types
set1 = {"apple", "banana","True",4, "cherry"}
print("Different types;",set1)

#type() - set
Set={"red","blue","green","yellow","red"}
print(type(Set))

#Set contructor
"""Double round-brackets"""
Set=set(("red","blue","green","yellow"))
print("Set contructor:",Set)


#2. ACCESS SET ITEMS
"""
1.You cannot access items in a set by referring to an index or a key.

2.But can loop through the set items using a for loop, or ask if a specified 
value is present in a set, by using the in keyword."""

#For Loop
Set={"red","blue","green","yellow","red"}
for x in Set:
    print(x)

# IF
Set={"red","blue","green","yellow","red"}
print("yellow" in Set)
print("pink" in Set)

#Change items
"""Once a set is created, you cannot change its items, but can add new items."""

#3.ADD SET ITEMS
"""To add one item to a set use the add() method."""

Set={"red","blue","green","yellow","red"}
Set.add("pink")
print("Add Item:", Set)

#Add Sets
"""To add items from another set into the current set, use the update() method"""

Set={"red","blue","green","yellow","red"}
Set1={1,2,3,4,5}
Set.update(Set1)
print("Add set:",Set)

#Add Any iterable
"""The object in the update() method does not have to be a set,
 it can be any iterable object (tuples, lists, dictionaries etc.)."""

Set={"red","blue","green","yellow","red"}
Set2=["eyes", "nose", "mouth"]
Set.update(Set2)
print("Add any iterable:",Set)


#4.REMOVES SET ITEMS
"""To remove an item in a set, use the remove(), or the discard() method.
If the item to remove does not exist, remove() will raise an error."""

Set={"red","blue","green","yellow","red"}
Set.remove("blue")
print("Remove-",Set)


"""If the item to remove does not exist, discard() will NOT raise an error"""

Set={"red","blue","green","yellow","red"}
Set.discard("blue")
print("Discard-",Set)

#POP() - Removes a random item.
""" 
1.can also use the pop() method to remove an item, but this method will remove a random item, 
so you cannot be sure what item that gets removed.

2.The return value of the pop() method is the removed item.

3.Sets are unordered, so when using the pop() method, you do not know which item that gets removed."""

Set={"red","blue","green","yellow","red"}
x=Set.pop()
print("pop-",x)
print("Pop-Removes random item:",Set)

#Clear()
Set1={"red","blue","green","yellow","red"}
Set1.clear()
print(Set1)


#Del()
#this will raise an error because the set no longer exists
colors={"red","blue","green","yellow","red"}
#del colors
print(colors)

#5.Loop sets

Set={"red","blue","green","yellow","red"}
for x in Set:
    print(x)


#6.Join sets
"""
1.use the union() method that returns a new set containing all items from both sets, 
or the update() method that inserts all the items from one set into another

2.Both union() and update() will exclude any duplicate items.
"""

Set1={"red","blue","green","yellow","red"}
Set2={1,2,3,4,5}
Set3=Set1.union(Set2)
print("Unioin-",Set3)

Set1={"red","blue","green","yellow","red"}
Set2={1,2,3,4,5}
Set1.update(Set2)
print("Update-",Set1)

#Keep only the duplicates -
#Intersection_update() method

"""The intersection_update() method will keep only the items that are present in both sets."""

Set1={"red","blue","green","yellow","red"}
Set2={1,2,3, "blue", "green",4,5}
Set1.intersection_update(Set2)
print("Intersection_update-",Set1)

#Intersection()
"""The intersection() method will return a new set, that only contains the items that are present in both sets."""

Set1={"red","blue","green","yellow","red"}
Set2={1,2,3, "blue", "green",4,5}
New_Set=Set1.intersection(Set2)
print("Intersection-", New_Set)

#Keep All, But NOT the Duplicates
#symmetric_difference_update() method

"""The symmetric_difference_update() method will keep only the elements that are NOT present in both sets."""

Set1={"red","blue","green","yellow","red"}
Set2={1,2,3, "blue", "green",4,5}
Set1.symmetric_difference_update(Set2)
print("symmetric_difference_update-",Set1)


Set1={"red","blue","green","yellow","red"}
Set2={1,2,3, "blue", "green",4,5}
Set1.symmetric_difference(Set2)
print("symmetric_difference-",Set1)


#exercise
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)

#SET METHODS
"""
add()	                            Adds an element to the set
clear()	                            Removes all the elements from the set
copy()	                            Returns a copy of the set
difference()	                    Returns a set containing the difference between two or more sets
difference_update()	                Removes the items in this set that are also included in another, specified set
discard()	                        Remove the specified item
intersection()	                    Returns a set, that is the intersection of two other sets
intersection_update()	            Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	                    Returns whether two sets have a intersection or not
issubset()	                        Returns whether another set contains this set or not
issuperset()	                    Returns whether this set contains another set or not
pop()	                            Removes an element from the set
remove()                          	Removes the specified element
symmetric_difference()	            Returns a set with the symmetric differences of two sets
symmetric_difference_update()	    inserts the symmetric differences from this set and another
union()	                            Return a set containing the union of sets
update()                   	        Update the set with the union of this set and others
"""