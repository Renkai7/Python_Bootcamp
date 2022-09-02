# Calculator

# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


# Dictionary for Functions
math_operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# User chooses first number to calculate with
num1 = int(input("What's the first number?: "))

# Show all math operator options
for operators in math_operators:
    print(operators)

# User chooses operation
operation = input("Pick an operation from the line above: ")

# User chooses second number to calculate with
num2 = int(input("What's the second number?: "))

# Get math function in dictionary
calculation_function = math_operators[operation]

# Assign chosen function to variable - answer
answer = calculation_function(num1, num2)

print(f"{num1} {operation} {num2} = {answer}")


