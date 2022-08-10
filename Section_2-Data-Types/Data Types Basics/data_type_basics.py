# DATA TYPES

# String
#   Subscripting - pulling character out of a string
print("Hello"[0])
#   Using [-1] you can pull the last character in a string
print("Hello"[-1])

# Integer - whole numbers(numbers without decimals)
print(123 + 345)

# Float - Numbers using decimal places
print(3.14141)

# Boolean - True or False values
truth = True
deceit = False

# TYPE ERROR, TYPE CHECKING and TYPE CONVERSION
#   type() gives the type of data something is
num_char = 4
print(type(num_char))

#   Convert int into str
new_num_char = str(num_char)
print("Your number is " + new_num_char + ". How lucky!")

# MATH OPERATORS
#   '**' raises number to power of a number
print(2 ** 3)
#   round() will round numbers
print(round(8 / 3))
#   round(num, x) allows you to round number by decimal place of choice
# this rounds to 2 decimal places
print(round(8 / 3, 2))
#   '//' operator gets whole number without converting into int
print(8 // 3)
#   '+=, -=, *=, /=' manipulate previous value

# F STRING
#   f string allows you to add values into a string
score = 1
height = 1.8
isWinning = True
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")

print(type(8 // 2))

# Note
# - You can't combine string with int without conversions
# - When using '/' divide operator the results will always be float
