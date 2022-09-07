from game_data import data
from art import vs, logo
import random


# Get random user from list
# user1 = random.choice(data)
# user2 = random.choice(data)

# print(user1["name"])
# print(user2)

# Compare user followers
# comparison_list = {}
# comparison_list[user1["name"]] = user1["follower_count"]
# comparison_list[user2["name"]] = user2["follower_count"]

# print(comparison_list)
# Get list of dictionaries
def get_dictionary_list():
    dictionary_list = []
    for entry in data:
        dictionary_list.append(entry)
    return dictionary_list


def get_user_data(user):
    user_name = user['name']
    user_description = user['description']
    user_country = user['country']
    return f"{user_name}, a {user_description}, from {user_country}"


def get_follower_count(user):
    user_followers = user['follower_count']
    return user_followers


def find_highest_count(dictionary_name):
    """
    Find user with the highest follower count and returns name of user
    """
    highest_followers = max(dictionary_name, key=dictionary_name.get)
    return highest_followers


def game():
    user_list = get_dictionary_list()
    chance = 1
    answer = ""
    score = 0
    # print(user_list)
    user_1 = random.choice(user_list)
    user_2 = random.choice(user_list)

    print(logo)
    while chance != 0:
        # Loop until user 1 and user 2 have different values
        while user_1['name'] == user_2['name']:
            user_2 = random.choice(user_list)
        user_1_followers = get_follower_count(user_1)
        user_2_followers = get_follower_count(user_2)
        print(f"Compare A: {get_user_data(user_1)} \n "
              f"{vs} \n "
              f"Compare B: {get_user_data(user_2)}")

        # TODO: Make account account at position B become the next account at position A

        comparison_list = []
        comparison_list = {user_1["name"]: user_1_followers, user_2["name"]: user_2_followers}
        highest_count = find_highest_count(comparison_list)
        print(highest_count)

        # Assign A or B to user with the highest count
        if highest_count == user_1['name']:
            answer = "a"
        elif highest_count == user_2['name']:
            answer = "b"

        # Ask user for a guess
        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Check if user answer is correct
        if user_choice == answer:
            score += 1
            print("Correct!\n")
            user_1 = random.choice(user_list)
            user_2 = random.choice(user_list)
        else:
            print("Incorrect.")
            chance -= 1

    print(f"Final score: {score}")


game()

# Steps
# 1 - Show 2 random dictionaries
#
