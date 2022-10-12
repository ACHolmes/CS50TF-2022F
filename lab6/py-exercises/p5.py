'''
Topic 5: Importing libraries

Where in C we used include to use code from header files, in Python we use the import keyword.

We can import an entire library or just a function from a library
'''

print(" === Topic 5: libraries! === \n")

# random library gives us access to random numbers :)
import random
from cs50 import get_int

while(True):
    roll = get_int("Pick a number (1 - 6): ")
    if roll > 0 and roll <= 6:
        break

opponent = random.randint(1, 6)
print(f"Your pick: {roll}, opponent's roll: {opponent}")
if roll == opponent:
    print("You won!")
else:
    print("You lost :(")


''' 
What do you notice about this code? Python doesn't have a do-while loop explicitly,
but I have given you the implementation of a do-while loop above. How does it work?

We've also shown a few more syntactical differences (and similiarities):
 -- C --      -- Python --
    &&             and
    ||             or
    ==             ==
'''