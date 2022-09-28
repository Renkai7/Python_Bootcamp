from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(logo)
isCipherOn = True


def caesar(message, shift_amount, code_type):
    cipher_text = ""
    for letter in message:
        if letter in alphabet:
            index = alphabet.index(letter)
            if code_type == "encode":
                # restarts position based on remainder from larger number
                new_position = (index + shift_amount) % len(alphabet)
            else:
                # Goes in reverse order for list when numbers are negative
                new_position = index - shift_amount % len(alphabet)

            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter

    print(f"This {code_type}d text is {cipher_text}\n")


while isCipherOn:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(message=text, shift_amount=shift, code_type=direction)

    continue_cipher = input("Would you like to continue using the cipher? 'yes' or 'no'\n").lower()

    if continue_cipher == 'no':
        isCipherOn = False
        print("Goodbye!")
