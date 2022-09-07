from game_data import data
import random

# Get random user from list
user1 = random.choice(data)
user2 = random.choice(data)

# print(user1["name"])
# print(user2)

# Compare user followers
comparison_list = {}
comparison_list[user1["name"]] = user1["follower_count"]
comparison_list[user2["name"]] = user2["follower_count"]

print(comparison_list)


#
# print(f"{comparison_list}")

# user1_follower = user1["follower_count"]
# max_follow = max(comparison_list[0]["follower_count"], comparison_list[1]["follower_count"])

def find_highest_count(list):
    """
    Find user with the highest follower count and returns name of user
    """
    highest_followers = max(list, key=list.get)
    return highest_followers


def game():
    answer = find_highest_count(comparison_list)
    print(answer)

# Steps
# 1 - Show 2 random dictionaries
#
