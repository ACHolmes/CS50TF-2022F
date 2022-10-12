
''' 
Part 4: Slicing and string work

We can slice up strings into smaller parts!
The syntax for this is similar to a range, where this time we have:
variable[start:end:step]
'''

print(" === PART 4 === \n")

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
