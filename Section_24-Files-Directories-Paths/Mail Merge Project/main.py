with open("Input/Names/invited_names.txt") as invites:
    names_list = invites.readlines()

with open("Input/Letters/starting_letter.txt") as start_letter:
    letter_template = start_letter.read()

for name in names_list:
    name = name.strip()
    with open(f"Output/ReadyToSend/{name}_invite.txt", mode="w") as invite_letter:
        invite_letter.write(letter_template.replace("[name]", name))
