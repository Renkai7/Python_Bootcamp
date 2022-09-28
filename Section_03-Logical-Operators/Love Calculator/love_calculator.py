# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
pair_name = name1.lower() + name2.lower()
letter_t = pair_name.count("t")
letter_r = pair_name.count("r")
letter_u = pair_name.count("u")
letter_e = pair_name.count("e")

letter_l = pair_name.count("l")
letter_o = pair_name.count("o")
letter_v = pair_name.count("v")

true_total = letter_t + letter_r + letter_u + letter_e
love_total = letter_l + letter_o + letter_v + letter_e

true_love = int(str(true_total) + str(love_total))

if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif 40 < true_love < 50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")

