import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
options_list = [rock, paper, scissors]

# User and CPU choose rock, paper, scissors
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

if user_input > 2 or user_input < 0:
    print("You typed an invalid number. You lose.")
else:
    user_choice = options_list[user_input]

    # randomise CPU choice
    random_option = random.randint(0, 2)

    cpu_choice = options_list[random_option]

    if user_choice == options_list[0]:
        if cpu_choice == options_list[0]:
            print(f"{user_choice} vs. {cpu_choice} Both rock. TIE!")
        elif cpu_choice == options_list[1]:
            print(f"{user_choice} vs. {cpu_choice} Paper beats rock. You lose.")
        else:
            print(f"{user_choice} vs. {cpu_choice} Rock beats scissors. You win!")

    if user_choice == options_list[1]:
        if cpu_choice == options_list[0]:
            print(f"{user_choice} vs. {cpu_choice} Paper beats rock. You win!")
        elif cpu_choice == options_list[1]:
            print(f"{user_choice} vs. {cpu_choice} Both Paper. TIE!")
        else:
            print(f"{user_choice} vs. {cpu_choice} Rock beats scissors. You lose.")

    if user_choice == options_list[2]:
        if cpu_choice == options_list[0]:
            print(f"{user_choice} vs. {cpu_choice} Rock beats scissors. You lose.")
        elif cpu_choice == options_list[1]:
            print(f"{user_choice} vs. {cpu_choice} Scissors beats paper. You win!")
        else:
            print(f"{user_choice} vs. {cpu_choice} Both scissors. TIE!")
