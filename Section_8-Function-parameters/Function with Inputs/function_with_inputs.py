# Regular Function
def greet():
    print("Hello Angela!")
    print("Welcome to the program Jack Bauer.")
    print("Shall we begin?")


# greet()


# Function that allows for input
def greet_with_name(name):
    print(f"Hello {name}!")
    print(f"Welcome to the program {name}.")


greet_with_name("Angela")

# Notes
# Parameter vs. Argument
# Parameter: the name of the data inside the function parenthesis (ex. "name" in def greet_with_name(name))
# Argument: the value of the data used in function (ex. "Angela" in greet_with_name("Angela"))
