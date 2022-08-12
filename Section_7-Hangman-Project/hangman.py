import random

word_list = ["aardvark", "baboon", "camel"]
display = []
# Choose random word from list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(f'Pssst, the solution is {chosen_word}.')

# Generate blanks for chosen word
for _ in range(word_length):
    display.append("_")
print(display)

# Ask user for a letter
guess = input("Guess a letter: \n").lower()

# Check if user chosen letter is in chosen word
for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = guess
        print(position)
print(display)



