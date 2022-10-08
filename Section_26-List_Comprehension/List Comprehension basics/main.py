# For Loop example
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
# print(new_list)

# Example
# new_list = [new_item for item in list]
# new_item = item to add in new_list
# item = item in the list we are looping through for values
# list = the list that contains item, original items that will be placed in new_list

# List Comprehension replacement for the For Loop
numbers = [1, 2, 3]
# new_list = [n+1 for n in numbers]
# print(new_list)

# List Comprehension for Strings
name = "Angela"
new_list = [letter for letter in name]

# List Comprehension with range()
range_list = [n * 2 for n in range(1, 5)]
# print(range_list)

# Conditional List Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# return names that have less than 5 letters
short_name = [name for name in names if len(name) < 5]
print(short_name)
long_name = [name.upper() for name in names if len(name) > 5]
print(long_name)
