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
# if height > 120:
#     print("You can ride the roller coaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry! You do not meet the height requirement.")


# Multiple if statements
bill = 0

# if height > 120:
#     print("You can ride the roller coaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")
#
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         bill += 3
#
#     print(f"The bill total is ${bill}.")
# else:
#     print("Sorry! You do not meet the height requirement.")

# Logical Operators
if height > 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"The bill total is ${bill}.")
else:
    print("Sorry! You do not meet the height requirement.")