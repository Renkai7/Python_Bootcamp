from tkinter import *


def button_clicked():
    # Gets input inside Entry component (text box)
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# --creating new text for a label
my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)
new_button = Button(text="Shiny Button")
new_button.grid(column=2, row=0)

# Entry (text box)
input = Entry(width=10)
# input.pack()
# input.get()
input.grid(column=3, row=2)


window.mainloop()

# Notes
# *args: creates tuple for inputs in function
# pack() places tkinter components on screen
# place() uses x, y to place components
# grid() uses a grid system to place components
# command in Button() is an event listener
