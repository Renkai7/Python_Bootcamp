# Functions with Outputs

def format_name(f_name, l_name):
    """
    Take a first and last name and format it to return the title case version of the name.
     
    """
    # Can have multiple returns in function

    # Return if conditions are met
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."

    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"


formatted_string = format_name("mIchaEl", "sPENcEr")
# print(formatted_string)
print(format_name(input("What is your first name? "), input("What is your last name? ")))
