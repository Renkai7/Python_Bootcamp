alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(message, shift_amount):
    cipher_text = ""
    for letter in message:
        index = alphabet.index(letter)
        # restarts position based on remainder from larger number
        new_position = (index + shift_amount) % len(alphabet)
        cipher_text += alphabet[new_position]

    print(f"This encoded text is {cipher_text}")


def decrypt(message, shift_amount):
    cipher_text = ""
    for letter in message:
        index = alphabet.index(letter)
        new_position = index - shift_amount % len(alphabet)
        cipher_text += alphabet[new_position]

    print(f"This encoded text is {cipher_text}")


# encrypt(message=text, shift_amount=shift)
decrypt(message=text, shift_amount=shift)
