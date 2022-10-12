'''
Topic 6: Functions

So far we have only used standard Python functions, or functions imported from
other libraries. How do we define our own functions? In Python, function definitions are written
using the def keyword. We use the syntax

def name(input1, input2, ...):
    # logic here
    return result

Let's do some examples
'''

print(" === Topic 6: functions! === \n")

print(" -- Part 1: basic functions -- ")
# A function that adds 1
def add_1(x):
    return x + 1

print(f"2 + 1 = {add_1(2)}")

# A function thats finds x + y
def add(x, y):
    return x + y

x = 4
y = 5
print(f"{x} + {y} = {add(x, y)}")

# A function that prints "Hello, world!"
def hello():
    print("Hello, world!")

hello()

# A function that computes the nth Fibonacci number (note: example of recursion in Python, same as C)
def fib(n):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)

# Using our 'end' parameter again for practice:
print("Some Fibonacci terms: ", end ="")
print(fib(5), fib(6), fib(7))

'''
This seems great, it's much easier to define a function in Python! However, this function
definition at the moment has some problems, for example, what happens when we run the following?
'''

print("\n -- Part 2: Functions & types -- ")
print("Question 1: What happens when we try to add 1 to a string?")
# Uncomment me and try running the program!
# print(f"Adding 1 to t: {add_1('t')}")

'''
We can specify what types we want as inputs for our functions just the same as we could in C, although we
aren't required to do so:
'''

def add_ints(x: int, y: int) -> int:
    return x + y

print(f"4 + 5 using add function with typing: {add_ints(4, 5)}")

'''
What happens if we try adding an int and a string again?
First try:
    print(add_ints(5, "a"))
Then try:
    print(add_ints("a", 5))

What errors do we get? What do you think they mean?
'''

# Uncomment each one separately and try running the program:
# print(add_ints(5, "a"))

# print(add_ints("a", 5))


'''
Now let's try adding two strings using our two add functions:
What happens in each case?
'''
result = add("a", "b")
print(f"Printing add(\"a\", \"b\"): {result}") 

int_result = add_ints("a", "b")
print(f"Printing add_ints(\"a\", \"b\"): {int_result}") 

'''
Perhaps surprisingly, they both print "ab"!
It turns out that even if we do specify which type we want, 
Python DOES NOT ENFORCE THOSE TYPES. I can actually pass two floats into either function
if I wanted to, and Python would allow it! Here's an implementation that enforces the types as C would.
'''

print("\n -- Part 3: Type checking (bonus) -- ")

def add_ints_safe(x, y):
    if not(isinstance(x, int) and isinstance(y, int)):
        raise TypeError("Must provide two integer arguments")
    return x + y

print(f"Safe add function, 4 + 5 = {add_ints_safe(4, 5)}")
print("Safe add function should report our error if we try adding a + 5:\n")
print(add_ints_safe("a", 5))