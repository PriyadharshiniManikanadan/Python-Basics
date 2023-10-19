#DATA TYPES
x="colours" #text type - str
print(x)
print(type(x))

#NUMERIC TYPE
x=3               #int,
print(x)
print(type(x))
y=7.6          #float,
print(y)
print(type(y))
z=5j            #comp
print(z)
print(type(z))

#sequence type
x=["red","blue","green","yellow"]  #list,
print(type(x))
X=("red","blue","green","yellow") #tuple
print(type(X))
x=range(4) #range
print(x)
print(type(x))

#MAPPING TYPE - dict
x={"name":"utsav","age":7}
print(x)
print(type(x))

#SET TYPE -
x={"red","blue","green"}  #set(mutable),
print(x)
print(type(x))
x=frozenset({"red","blue","green"}) #frozenset(immutable)
print(x)
print(type(x))

#BOOLEAN TYPE - bool (T/F should be in capital)
x=False
print(x)
print(type(x))

#BYTE TYPE
x=b"priya" #bytes
print(x)
print(type(x))
x=bytearray(4) #bytearray
print(x)
print(type(x))
x=memoryview(bytes(5)) #memoryview(byte)
print(x)
print(type(x))

#NONE TYPE
x=None
print(x)
print(type(x))
