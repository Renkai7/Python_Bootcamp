print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# Conditional operator
#   check if height is greater than 120
#   '==' operator checks if values are equal; only using a single '=' causes error
if height > 120:
    print("You can ride the roller coaster!")
else:
    print("Sorry! You do not meet the height requirement.")

#   '%' is a modulo operator - divides numbers and gives remainder of division
print(7 % 2)
