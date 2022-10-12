'''
Part 3: List work
'''

print(" === PART 3 === \n")

# Bringing names list from previous file!
names = ["Aurora", "Cristopher", "Meghan"]

'''
Note how in the previous file we didn't have to declare lengths for a list in Python, we just said - here's a list!
Python uses linked lists, so we don't have to worry about fixed size arrays. This is often super convenient.
For example, I can now easily add a name to my list:
'''

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
