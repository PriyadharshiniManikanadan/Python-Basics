#BOOLEAN VALUES
#an expression is True or False.
print(10>9)
print(6>9)

#message
x=10
y=20
if x>y:
    print("Yes!, x is greater than y")
else:
    print("No!, x ix not greater than y")

#True statement
print(bool("priya"))
print(bool(5))
bool(["apple", "cherry", "banana"])

#False statement
print(bool())
print(bool(None))
print(bool({}))
print(bool([]))
print(bool(0))
print(bool(""))
print(bool(False))

#Functions can return a boolean
def myfunc():
    return True
print(myfunc())

#Execute code based on a boolean answer of a function
def mycode():
    return True
if mycode():
    print("YES!")
else:
    print("NO!")

#Built-in Function
#isinstance() returns the boolean value
x=200
print(isinstance(x,float))

y=65.76
print(isinstance(y,float))

z="priya"
print(isinstance(z,str))



