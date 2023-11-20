#TUPLES
"""
1.Python Tuple
2.Access tuples
3.Update tuples
4.Unpack tuples
5.Loop tuples
6.Join tuples
7.Tuples Methods
"""

#1. Python Tuples

#Multiple item in single variable
#round brackets
#ordered
#unchangable
#Allow duplicates
#one of the 4 built in functions

print(Tuple)
#Allow Duplicate
Tuple1=("red","blue","green","red","blue","yellow")
print(Tuple1)

#Tuple length
Tuple1=("red","blue","green","red","blue","yellow")
print(len(Tuple1))

#Create Tuple with one item
"""To create a tuple with only one item, you have to add a comma after the item
otherwise Python will not recognize it as a tuple."""

Tuple2=("red",)
print(type(Tuple2))

#Tuple item - Data Types
"""String, 
   int 
   boolean data types"""

#Type()
fruits=("apple","mango","banana","orange")
print(type(fruits))

#Type() constructor

"""It is also possible to use the tuple() constructor to make a tuple.
   Using the tuple() method to make a tuple:"""

fruits=tuple(("apple","mango","banana","orange"))
print(type(fruits))

#2.Access Tuples

fruits=("apple","mango","banana","orange")
print("Tuple Index:", fruits[2])

fruits=("apple","mango","banana","orange")
print("Negative index: ",fruits[-1])

fruits=("apple","mango","banana","orange")
print("range:", fruits[2:4])

fruits=("apple","mango","banana","orange")
print("range of negative index:", fruits[:-2])

#check if item is exist:

fruits=("apple","mango","banana","orange")
if "banana" in fruits:
    print("yes, banana is present")

#3. Update Tuples
"""Once a tuple is created, you cannot change its values. 
Tuples are unchangeable, or immutable as it also is called.

But there is a WORKAROUND. You can convert the tuple into a list,
 change the list, and convert the list back into a tuple."""

#change tuple values:

fruits=("apple","mango","banana","orange")
Y=list(fruits)
Y[2]="kiwi"
fruits=tuple(Y)
print(fruits)

#'example'
colours=("red","blue","green","yellow")
change=list(colours)
change[2]="purple"
colours=tuple(change)
print(colours)

#Add items:
#(i) Convert into List an

fruits=("apple","mango","banana","orange")
Y=list(fruits)
Y.append("avacado") #append() method
fruits=tuple(Y)
print("Add: ",fruits)

#(ii) Add Tuple to Tuple:
fruits=("apple","mango","banana","orange")
Y=("kiwi",)
fruits += Y
print("Add Tuple to Tuple:", fruits)

#Remove Tuple
fruits=("apple","mango","banana","orange")
y=list(fruits)
y.remove("mango")
fruits=tuple(y)
print(fruits)

#Delete tuples
# fruits=("apple","mango","banana","orange")
# del fruits
# print(fruits)

#Unpack Tuple
#Extract the values back into variables. This is called "unpacking":

fruits=("apple","mango","banana","orange")
(red,green,yellow,orange)=fruits
print(red)
print(green)
print(yellow)
print(orange)


# Using Asterisk*
"""If the number of variables is less than the number of values, 
you can add an * to the variable name and 
the values will be assigned to the variable as a list:"""

fruits=("apple","mango","banana","orange")
(red,green,*yellow)=fruits
print(red)
print(green)
print(yellow)


"""If the asterisk is added to another variable name than the last,
Python will assign values to the variable until the number of values 
left matches the number of variables left."""

fruits=("apple","mango","banana","orange")
(red,*green,orange)=fruits
print(red)
print(green)
print(orange)

#4. Loop Tuples
# Loop Through a Tuple

fruits=("apple","mango","banana","orange")
for x in fruits:
    print(x)

#Loop through the Index number

fruits=("apple","mango","banana","orange")
for x in range(len(fruits)):
    print(fruits[x])
    print(x)

#While loop
fruits=("apple","mango","banana","orange")
x=0
while x < len(fruits): #0<4
    print(fruits[x])
    x+=1 #x=x+1


#Join Tuples
#using + operator
fruits=("mango","banana","apple")
vegs=("carrot","beetroot","potato")
tuples = fruits + vegs
print(tuples)

#Multiply Tuples
#multiply the content of tuples
colors=("red","green","blue")
multiply = colors * 2
print(multiply)

#Methods 2
"""
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
"""

