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


def calculator():
    # User chooses first number to calculate with
    num1 = float(input("What's the first number?: "))

    # Show all math operator options
    for operators in math_operators:
        print(operators)
    isCalculating = True

    while isCalculating:
        # User chooses operation
        operation = input("Pick an operation from the line above: ")

        # User chooses second number to calculate with (only number user will update)
        num2 = float(input("What's the next number?: "))

        # Get math function in dictionary
        calculation_function = math_operators[operation]

        # Assign calculation function to variable - answer
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation} {num2} = {answer}")

        # Store previous answer as first number in operation
        num1 = answer

        # Check if user wants to continue
        continue_calc = input(
            f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or 'exit' to Exit: ").lower()

        if continue_calc == 'n':
            # Recursion - calculator() being called within itself
            calculator()
        elif continue_calc == 'exit':
            isCalculating = False


calculator()
# Notes
# Recursion - function that calls itself
# Recursion resets a function and all values within it (A new game!)
