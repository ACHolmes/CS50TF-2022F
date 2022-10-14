'''
Topic 9: Dictionaries

Python has some more built-in data structures that can be helpful (as you will see in the PSET).
One of these is a dictionary. Dictionaries store key-value pairs, and are implemented using hash tables (under the hood)
to allow for O(1) access and amortized (don't worry about what this means) O(1) insertions. 
'''

print(" === Topic 9: Dictionaries! === \n")

# We use {} to denote dictionaries in Python
dictionary = {}

'''
Part 1: Inserting into a dictionary

To insert into a dictionary, we use the following syntax:
dictionary[key] = value

Note that if that key already has a value, this updates the value in the dictionary
Let's create a dictionary that stores a TF's lab times.
'''

dictionary["Andrew"] = "Fri 4:30pm"
dictionary["Kenny"] = "Wed 3:00pm"

print("Our first dictionary: ")
print(dictionary)

# However, this week I have a midterm right before my lab, so let's update my lab time:

dictionary["Andrew"] = "Fri 4:45pm"

print("\nUpdated time for Andrew's lab this week: ")
print(dictionary)

'''
Part 2: Retrieving items from a dictionary

To retrieve information from a dictionary, if we are sure the key exists, we can
simply find it using the value of dictionary[key].

However, if we aren't sure whether a key exists in the dictionary, this may cause errors.
'''

# Using '' rather than  "" to avoid messing up the string - the two are generally equivalent
# in Python, but I generally use "" in case I have apostrophes in my string like "who's"
print("\nAccessing data from a dictionary: ")
print(f"Andrew's lab time this week is {dictionary['Andrew']}")

# Try uncommenting the following line. What happens?
# print(f"Phyllis' lab time this week is {dictionary['Phyllis']}")
# Phyllis doesn't have a lab as Head TF, some of you will attend her section instead!

# To do this safely, we can use the .get method for dictionaries, the first argument is they
# key to search for, the second argument is what is returned in case it can't find the key
print(f"Phyllis' lab time this week is {dictionary.get('Phylis', 'non-existent')}")