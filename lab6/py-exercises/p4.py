
''' 
Topic 4: Slicing and string work

We can slice up strings into smaller parts!
The syntax for this is similar to a range, where this time we have:
variable[start:end:step]
'''

print(" === Topic 4: Strings & slices! === \n")

example = "Slice me!"

# Printing our example text. Note here that + performs string concatentation (the joining of two strings)!
# This is another way of combining things to print in Python
print("Our example string is: " + example)

#Let's get just the word slice:
print(f"Slicing just the first word: {example[0:5:1]}")

# Remember in Python we can have optional arguments, so we can shorten this to just:
print(f"Slicing just the first word, simpler: {example[:5]}")

# It assumes whatever is after the first colon is the end, and anything after a second colon is the step!
# Let's be a bit more creative:
print(f"Slicing the second word: {example[6:9]}")
print(f"Reversing our string: {example[::-1]}")

# Why doesn't the following work? (it will print nothing)
# print(example[1:5:-1])

print(f"Some weird slice: {example[8:3:-2]}")
# Which e is this printing?

# There are a whole bunch of other string methods you could use, for example:
confused = example.replace("!", "?")
print(f"A confused slice: {confused}")

split = example.split()
print(f"Splitting by spaces: {split}")
