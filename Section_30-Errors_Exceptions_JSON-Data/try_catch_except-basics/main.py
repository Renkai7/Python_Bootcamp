# FileNotFound
# --except is too broad
# try:
#     file = open("a_file.txt")
# except:
#     file = open("a_file.txt", "w")

# --except with more information
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()

# Using 'raise'
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that I made up")

# Use 'raise' to check for extreme values
height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)


# Notes
# [finally] will run no matter what
