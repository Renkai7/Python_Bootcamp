# Using this lets you give variable name to file and close file for you without file.close()
# Read from file
with open("Output/my_file.txt") as file:
    contents = file.read()
    print(contents)

# file = open("my_file.txt")
# file.close()

# Write to file
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")

# Write to file that doesn't exist yet
# with open("new_file.txt", mode="w") as file:
#     file.write("New text.")

# Relative and Absolute File Path example


# Notes
# Use file.close() because it will use PC resources
# To write to file you must use mode="w"
# mode="w" (write) will overwrite previous text in file with new text
# mode="a" (append) will add new text to file without overwriting
# If you write using (mode="w") to a file that doesn't exist then it will be created automatically

