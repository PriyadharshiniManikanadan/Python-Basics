#OPERATERS
#1.Arithmetic
#2.Assignment
#3.Comparison
#4.Logical
#5.Identity
#6.Membership
#7.Bitwise

#Arithmatic
X=5
Y=2
print(X+Y) #add
print(X-Y) #sub
print(X*Y) #multiply
print(X/Y) #division
print(X**Y) #to the power of
print(X//Y) #floor division
print(X%Y) #remainder

#ASSIGNMENT
x=10
x+=5
print(x)
x-=4
print(x)
x*=2
print(x)
x/=3
print(x)
x%=2
print(x)
x//=1
print(x)
x=5
x**=10
print(x)
x=10
x&=5
print(x)
x|=10
print(x)
x^=40
print(x)

#COMPARISON T/F
a=10
b=7
print(a==b) #equal
print(a!=b) #not equal
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#LOGICAL
A=20
B=10
print(A>5 and B<5)
print(A>10 or B<3)
print(not(A>10 and B>5))

#Identity
#is
#is not
a={"red","blue"}
b={"red","blue"}
c=a
print(a is b)
print(c is a)
print(c is not b)
print(a != b)

"""to demonstrate the difference betweeen "is not" and "!=": 
this comparison returns False because x is equal to y"""

#MEMBERSHIP
#in
#not in
x="Red is a primary color"
print('primary' in x)
## returns True because a sequence with the value "primary" is there
print("colour" not in x)
## returns True because a sequence with the value "colour" is not there

#BITWISE
"""AND &        OR |           XOR  ^          NOT ~      >> RIGHT SHIFT
0 & 0 = 0       0 | 0 = 0      0 ^ 0 = 0       ~0 = 1     << LEFT SHIFT
0 & 1 = 0       0 | 1 = 1      0 ^ 1 = 1       ~1 = 0
1 & 0 = 0       1 | 0 = 1      1 ^ 0 = 1
1 & 1 = 1       1 | 1 = 1      1 ^ 1 = 0"""

print(6&3)
print(8|4)
print(5^8)
print(~2)
print(6 >> 2)
print (5<<2)

#OPERATER PRECEDENCE
print(100 + 5 * 3)

"""
Multiplication has higher precedence than addition, and needs to be 
evaluated first.
The calculation above reads 100 + 15 = 115
"""







