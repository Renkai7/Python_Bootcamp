print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# Conditional operator
#   check if height is greater than 120
#   '==' operator checks if values are equal; only using a single '=' causes error
# if height > 120:
#     print("You can ride the roller coaster!")
# else:
#     print("Sorry! You do not meet the height requirement.")

#   '%' is a modulo operator - divides numbers and gives remainder of division
print(7 % 2)

# Nested if / else statement
if height > 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry! You do not meet the height requirement.")
