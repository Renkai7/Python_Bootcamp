from game_data import data
from art import vs
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
def get_user_data():
    dictionary_list = []
    for entry in data:
        dictionary_list.append(entry)
    return dictionary_list


def find_highest_count(dictionary_name):
    """
    Find user with the highest follower count and returns name of user
    """
    highest_followers = max(dictionary_name, key=dictionary_name.get)
    return highest_followers


def game():
    user_list = get_user_data()
    chance = 1
    answer = ""
    score = 0
    # print(user_list)
    user1 = random.choice(user_list)
    user2 = random.choice(user_list)

    while chance != 0:

        while user1['name'] == user2['name']:
            user2 = random.choice(user_list)
        print(f"1: {user1['name']}, {user1['description']} \n {vs} \n 2: {user2['name']}, {user2['description']}")
        comparison_list = []
        comparison_list = {user1["name"]: user1["follower_count"], user2["name"]: user2["follower_count"]}
        highest_count = find_highest_count(comparison_list)
        print(highest_count)
        if highest_count == user1['name']:
            answer = "a"
        elif highest_count == user2['name']:
            answer = "b"

        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        if user_choice == answer:
            score += 1
            print("Correct!")
            user1 = random.choice(user_list)
            user2 = random.choice(user_list)
        else:
            print("Incorrect.")
            print(f"Final score: {score}")
            chance -= 1


game()

# Steps
# 1 - Show 2 random dictionaries
#
