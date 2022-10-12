''' 
Exercises to get used to Python!

Multi-line comments can be done using the triple apostrophes like this!

Single-line comments require a #

Note in codespaces (and VSCode), you can use the shortcut
CTRL + /  (Or CMD if on Mac I believe) to write a single line comment
in any language.
'''

'''
Part 1: Using print
'''

print("\n === PART 1 === \n")

# To print, we can just use the print function as such:
print("Hello world!")

# by default, print adds a newline character for us. To avoid this, we use the end paramter:
print("Hello, ", end ="")

# We can print a variable by just writing print(variable):
name = "Andrew"
print(name)

# We can return to a more C-like syntax instead as such:
print(f"{name}")


'''
Part 2: Loops & range function
'''

print("\n === PART 2 === \n")

# To write a for loop, we use the following syntax:
for i in range(3):
    print(f"Iteration {i}")
# Note: indentations matter in Python! Being at the same level of indentation
# is equivalent to being within the same set of {} in C.

# Above we used the range function. Essentially what it does is generate a list (array) for us
# which we can see if we explicitly treat it as a list:
print(list(range(3)))

'''
Range syntax:

range takens up to 3 arguments: 
range(start, end, step)
If only 1 is provided, it defaults to start = 0, step = 1
If only 2 are provided, it deaults to step = 1
Try think about what the following will look like

range1 = range(1, 3, 2)
range2 = range(5, 0, -1)
range3 = range(1, 6, 2)

Which values are inclusive or exclusive? 
Once you've thought about these, take them outside the comments and use the syntax above to print them, e.g.
print(list(range1))

'''

# Returning to our previous loop:
for i in range(3):
    print(f"Iteration {i}")

# we see this 'for' loop sets i to each value in the list at each iteration. This means we can shorten
# some things we would do in C. For example, let's imagine printing a list of names:
print("Printing lists is easy in Python!")
print("--- FOR LOOP VERSION ---")
names = ["Aurora", "Cristopher", "Meghan"]
for name in names:
    print(name)


# An example for a while loop:
print("--- WHILE LOOP VERSION ---")
i = 0
while i < len(names):
    print(names[i])
    i+= 1


'''
Note how we didn't have to declare lengths or do anything for a list in Python, we just said - here's a list!
Python uses linked lists, so we don't have to worry about fixed size arrays. This is often super convenient.
For example, I can now easily add a name to my list:
'''

'''
Part 3: List work
'''

print("\n === PART 3 === \n")

# We can print a list directly in Python :)
print(names)

# The append method adds an item to a list!
names.append("Kevin")

# Let's see what our list looks like now!
print(names)

# We can also easily remove names (sorry Aurora!)
names.remove("Aurora")
print(names)

# We index into a list much the same as we do in C:
print(names[0])

#We can also do the same for strings as if they were stored as an array of chars in C:
print(names[0][1])
# Prints 'r', the second letter in Cristopher :)

''' 
Part 4: Slicing and string work

We can slice up strings into smaller parts!
The syntax for this is similar to a range, where this time we have:
variable[start:end:step]
'''

print("\n === PART 4 === \n")

example = "Slice me!"
#Let's get just the word slice:
print(example[0:5:1])

# Remember in Python we can have optional arguments, so we can shorten this to just:
print(example[:5])

# It assumes whatever is after the first colon is the end, and anything after a second colon is the step!
# Let's be a bit more creative:
print(example[6:9])
print(example[::-1])

# Why doesn't the following work? (it will print nothing)
print(example[1:5:-1])

print(example[8:3:-2])
# Which e is this printing?

# There are a whole bunch of other string methods you could use, for example:
confused = example.replace("!", "?")
print(confused)



'''
Part ?: VSCode tricks

Adding a few bonus tricks in case you like learning keyboard shortcuts. 
If people like these I can share more!

1) Highlighting several lines and hitting TAB indents each line. hitting SHIFT + TAB de-indents the lines

2) Highlighting a word and hitting F2 (Or FN + F2) will rename a variable/function in ALL locations. Try it on this badly named variable:
'''

print("\n === PART ? === \n")

this_is_a_bad_variable_name = 0

print(this_is_a_bad_variable_name + 1)

'''
3) Similarly, highlighting a word and hitting CTRL + SHIFT + L will select all occurences of a string.
   Try using it to rename names to something like lab_names :)
'''