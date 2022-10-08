from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website == "" or username == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please fill in all fields.")
    else:
        is_saving = messagebox.askokcancel(title=website,
                                           message=f"These are the details entered: \nUsername: {username} \n"
                                                   f"Password: {password} \nWould you like to save?")
        if is_saving:
            with open("password.txt", mode="w") as file:
                file.write(f"{website} | {username} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# Website entry
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

# Email/Username label
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

# Email/Username entry
username_entry = Entry(width=35)
username_entry.insert(0, "ren531@email.com")
username_entry.grid(column=1, row=2, columnspan=2)

# Password label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Password entry
password_entry = Entry(width=21, show="*")
password_entry.grid(column=1, row=3)

# Generate password button
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

# Add button
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
