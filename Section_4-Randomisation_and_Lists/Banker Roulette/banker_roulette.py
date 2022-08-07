import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
name_list_length = len(names)
random_num = random.randint(0, name_list_length - 1)
winner = names[random_num]

print(f"{winner} is going to buy the meal today!")

# Extra
# Gives same result buy with less code
person_to_pay = random.choice(names)
print(f"{person_to_pay} is going to buy the meal today!")
