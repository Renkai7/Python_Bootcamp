fruits = ["Apple", "Peach", "Pear"]
# For loop
#   takes list of 'fruits' and assigns variable: fruit to each item in list
#   fruit value for each pass: 1st pass- fruit = Apple, 2nd pass- fruit = Peach, etc.
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

# Range()
#   range() generate a range of numbers
#   range() doesn't include the last number in the range
# for number in range(1, 11):
#     print(number)

#   you can add a step count for range() by adding a third number
# for number in range(1, 11, 3):
#     print(number)

#   Add all numbers from 1 to 100
total = 0
for number in range(1, 101):
    total += number
print(total)

# Notes
#  - rule of thumb: use singular word for items in a list (ex. fruit for fruits list)
