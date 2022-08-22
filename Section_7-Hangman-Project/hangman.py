import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
display = []
lives = 6
# Choose random word from list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
# Loop until user guesses all letters
end_of_game = False

print(f'Pssst, the solution is {chosen_word}.')

# Generate blanks for chosen word
for _ in range(word_length):
    display.append("_")
print(display)


# Display initial hangman
print(stages[lives])
while not end_of_game:

    # Ask user for a letter
    guess = input("Guess a letter: \n").lower()
    # guess_length = len(guess)
    # for position in range(guess_length):
    #     if guess[position] in chosen_word:

    # Check if you've already guessed a letter correctly
    if guess in display:
        print(f"You've already guessed '{guess}'")

    # Check if user chosen letter is in chosen word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess

    # Check if letter is wrong guess then subtract 1 life
    if guess not in chosen_word:
        lives -= 1
        # update hangman image
        print(stages[lives])
        print(f"'{guess}' is not in the word.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if out of lives or if all letters guessed correctly to end game
    if "_" not in display:
        end_of_game = True
        print("Congrats! You win!")
    elif lives == 0:
        end_of_game = True
        print("Out of lives. You lose.")



