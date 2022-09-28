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


# Function with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


greet_with("Jack Bauer", "Nowhere")

# Keyword Arguments
greet_with(name="Angela", location="London")

# Notes
# Parameter vs. Argument
# Parameter: the name of the data inside the function parenthesis (ex. "name" in def greet_with_name(name))
# Argument: the value of the data used in function (ex. "Angela" in greet_with_name("Angela"))
