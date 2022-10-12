'''
Topic 8: Files

We often want to work with files outside of our code. How do we do that in Python?
'''

print(" === Topic 8: Files! === \n")

# We generally open files in Python as so:
with open("text.txt") as file:
    # Copy everything from the file into a Python string
    print("Reading a whole file in as one string: ")
    text = file.read()
    print(text, end="\n\n")

# What happens if you change the above to text2.txt?
# What if we wanted each line separately?

with open("text2.txt") as file:
    print("Splitting up lines by using .readlines(): ")
    lines = file.readlines()
    print(lines, end="\n\n")

# How about if we wanted to write our own file?
# This time we need to explicitly provide "w" to write, as it defaults to "r" for read
with open("text3.txt", "w") as file:
    file.write("Here's a new file!")

# with open is great as it automatically closes the file for us. For example, if I try to write again
# here, I will get an error with a helpful error message:

# Uncomment below!
# file.write("Add meeeeee!")

# We can also open and close files more like in C:
file = open("text3.txt", "a")
file.write("\nOh, a second line I see!")
file.close()
# The "a" stands for append, "w" would overwrite what we already had written to the file!