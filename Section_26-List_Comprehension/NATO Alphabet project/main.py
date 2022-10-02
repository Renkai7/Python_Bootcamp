import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_dict)

user_input = input("Enter a name: ").upper()
nato_name = [nato_dict[letter] for letter in user_input]
print(nato_name)
