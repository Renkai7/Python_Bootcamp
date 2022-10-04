from tkinter import *


def convert_miles():
    miles = int(miles_input.get())
    kilometer = miles * 1.609
    kilometer_output.config(text=kilometer)


# Setup Window
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Miles section
miles_label = Label(text="Miles")
miles_input = Entry()
# --miles section positioning
miles_label.grid(column=2, row=0)
miles_input.grid(column=1, row=0)

# Kilometer section
is_equal_to_text = Label(text="is equal to")
kilometer_label = Label(text="Km")
kilometer_output = Label(text="0")
# --kilometer section positioning
is_equal_to_text.grid(column=0, row=1)
kilometer_label.grid(column=2, row=1)
kilometer_output.grid(column=1, row=1)

# Calculate button
calculate_btn = Button(text="Calculate", command=convert_miles)
# --button positioning
calculate_btn.grid(column=1, row=2)

window.mainloop()
