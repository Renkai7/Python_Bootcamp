from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()

# --creating new text for a label
my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button
def button_clicked():
    # Gets input inside Entry component (text box)
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry (text box)
input = Entry(width=10)
input.pack()
# input.get()

window.mainloop()

# Notes
# *args: creates tuple for inputs in function
# pack() places tkinter components on screen
# command in Button() is an event listener
