# to use random Module you must import it
import random
import my_module

# randint() gives numbers between 1 and 10
random_integer = random.randint(1, 10)
print(random_integer)

# multiply by 5 to get decimal numbers between 0 and 5
random_float = random.random() * 5
print(random_float)

# recreate of love score calculator
love_score = random.randint(1, 100)
print(f"love score: {love_score}")

# Using Modules
#   Use our personally created module - my_module
# print(my_module.pi)

# Notes
# - modules are split up pieces of code (think different people working on different parts of a car
# - random.random() only gives decimal numbers less than 1
