#STRINGS
 #1.Slicing
 #2.Modify strings
 #3.Concatenate strings
 #4.Format strings
 #5.Escape characters
 #6.String methods


print('hello')
Name='Priya'
print(Name)

#para
Multiline="""Priya  
is 
my
name
"""
print(Multiline)

#strings are Array
print(Name[3]) #each character represents by 1, caled indices starts from 0

#Looping through a string : since it is an array
# it can loop thru the cahracters
for x in 'priya':
    print(x)
for y in "Manikandan":
    print(y)
for Name in "Utsav":
    print(Name)

#String length
sent="My name is  Priyadharshini Manikandan"
print(len(sent))

#use it in "if" statement
sent1="Do yu have cash to buy?"
if "cash" in sent1:
    print("yes, 'cash' is present")
sent2="My life is beautiful with you"
if "beautiful in sent2":
    print("yes, 'beautiful' is present")

#Check string
#keyword - in
print("dharshini" in sent)
print("Main" in sent)

#keyword - Not in
print('utsav' not in sent)
print("Priyadharshini" not in sent)

#NOT IN in IF statement
sent3="Iam a mom of 2 kids"
if "priya" not in sent3:
    print("yes 'priya' is not present")

#1. SLICING
Intro = "hello python"
print(Intro[4:10])

# slice from the start
print(Intro[:8])

# slice to the end
print(Intro[2:])

# Negative slicing
# starts from -1 from backward
print(Intro[-9:-3])

#2.Modify strings
#uppercase
x="   Python is my favourite  "
print(x.upper())
#lowercase
print(x.lower())
#remove whitespace
print(x.strip())

#3.CONCATENATE STRINGS
#Merge two strings
First_name="Priyadharshini"
Last_name="Manikandan"
print(First_name+Last_name)

#add space between two strings
print(First_name+" "+Last_name)

#4.FORMAT STRINGS
#using format() method we can add 2 strings and numbers.
age=30
Line="My name is Priya, and Iam {} years old."
print(Line.format(age))

#multiple values
count=3
toys="Mario"
price=1000
order="I bought {} numbers of {} toys for {} dollars."
purchase="I got my {} new {} toys for {} rupees."
print(purchase.format(count,toys,price))
print(order.format(count,toys,price))

#Index format
ID=12345
Region="NewYork"
Amount=9876
Date="Aug"
Sale="Priya sold an house in {1} Region for {2} dollars on {3},with the ID {0}."
print(Sale.format(ID,Region,Amount,Date))

#5.EXCAPE CHARACTERS
# \ followed by string
Test="My topic name is \"Python\""
print(Test)

Test1="I can\'t able to understand quickly"
print(Test1)

Test2="New \bYork" #backspace
print(Test2)

Test3="New\tYork" #leave a space
print(Test3)

Test4="New\rYork" #return the next string
print(Test4)

Test5="New\nYork" #new line
print(Test5)

Test6="New\fYork" #Form Feed - a page breaking contol character
print(Test6)

#6.STRING METHODS
#built-in methods can use on a strings


sample="manikandan IS MY HUSBAND NAME"
#Converts the 1st character to upper case n others to lower
capitalize=sample.capitalize()
print(capitalize)

# converts all strings to lower case
casefold=sample.casefold()
print(casefold)

#Returns a centered string
sent="Python is interesting"
center=sent.center(50)
print(center)

#Returns the number of times a specified value occurs in a string
x="Hi,how are you Hari?"
count=x.count('H')
print(count)







