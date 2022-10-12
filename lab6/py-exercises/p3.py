'''
Topic 3: List work
'''

print(" === Topic 3: lists! === \n")

# Bringing names list from previous file!
names = ["Aurora", "Cristopher", "Meghan"]

'''
Note how in the previous file we didn't have to declare lengths for a list in Python, we just said - here's a list!
Python uses linked lists, so we don't have to worry about fixed size arrays. This is often super convenient.
For example, I can now easily add a name to my list:
'''

# We can print a list directly in Python :)
print(f"Our original list: {names}")

# The append method adds an item to a list!
names.append("Kevin")

# Let's see what our list looks like now!
print(f"Our list after 'appending' Kevin: {names}")

# We can also easily remove names (sorry Aurora!)
names.remove("Aurora")
print(f"Our list after 'removing' Aurora: {names}")

# We index into a list much the same as we do in C:
print(f"The first name in the list is: {names[0]}")

#We can also do the same for strings as if they were stored as an array of chars in C:
print("The second letter in the first name in our list is: {names[0][1]}")
