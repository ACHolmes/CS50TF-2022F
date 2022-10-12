'''
Part 2: Loops & range function
'''

print(" === PART 2 === \n")

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

