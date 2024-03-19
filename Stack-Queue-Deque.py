#Stack
""" Stack works on the principle of “Last-in, first-out”.
Also, the inbuilt functions in Python make the code short and simple.
To add an item to the top of the list, i.e., to push an item,
we use append() function and to pop out an element we use pop() function.
These functions work quiet efficiently and fast in end operations."""

# Python code to demonstrate Implementing
# stack using list
x = ["Amar", "Akbar", "Anthony"]
x.append("Ram")
x.append("Iqbal")
print("Stack:\n",x)
#
# Removes the last item
print(x.pop())
#
print(x)
#
#Removes the last item
print(x.pop())
#
print(x)

print("==================================================================")

#Queue :

"""works on the principle of “First-in, first-out”. 
 Below is list implementation of queue. 
 We use pop(0) to remove the first item from a list."""

# Python code to demonstrate Implementing
# Queue using list
y = ["Amar", "Akbar", "Anthony"]
y.append("Ram")
y.append("Iqbal")
print("Queue:\n",y)

# Removes the first item
print(y.pop(0))

print(y)

# Removes the first item
print(y.pop(0))

print(y)

print("==================================================================")

# Deque

"""In case of stack, list implementation works fine and provides both append() and pop() in O(1) time. 
When we use deque implementation, we get same time complexity."""


# Python code to demonstrate Implementing
# Stack using deque
from collections import deque
queue = deque(["Ram", "Tarun", "Asif", "John"])
print(queue)
queue.append("Akbar")
print(queue)
queue.append("Birbal")
print(queue)
print(queue.pop())
print(queue.pop())
print(queue)


"""But when it comes to queue, the above list implementation is not efficient. 
In queue when pop() is made from the beginning of the list which is slow. 
This occurs due to the properties of list, which is fast at the end operations but slow at the beginning operations, 
as all other elements have to be shifted one by one.
So, we prefer the use of dequeue over list, 
which was specially designed to have fast appends and pops from both the front and back end. """


from collections import deque

queue = deque(["Ram", "Tarun", "Asif", "John"])
print(queue)
queue.append("Akbar")
print(queue)
queue.append("Birbal")
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)

