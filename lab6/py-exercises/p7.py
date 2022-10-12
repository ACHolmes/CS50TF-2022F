'''
Topic 7: main function and command line arguments

It might have seemed weird to leave behind our trusty main function and 
the (hopefully now less) cryptic int main(void). While Python can do without a main
function, we often use one anyway, although with even more bizarre syntax
'''

# We have to import the sys library to get command line arguments. 
# There is no such thing as argc in Python, instead we use argc = len(sys.argv)
import sys

# Even with a main funciton, we can still write code outside of it that will be run
print(" === Topic 7: main function and cmd-line args! === \n")

def main():
    print("Hello, world!")
    if len(sys.argv) > 1:
        print(f"The first argument provided to the function was: {sys.argv[1]}")
    # To return 0, we use sys.exit:
    sys.exit(0)

print("Where should this appear?")

# Don't worry about how this works - you're welcome to Google if interested
# Otherwise probably best to treat this as an int main(void) scenario again.
# We only have a week on Python, so maybe worth just accepting this one as is :)
if __name__ == "__main__":
    main()

print("Did you find this? How come it never prints?")