MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 550,
    "milk": 300,
    "coffee": 300,
}


# Ask user to choose a drink (espresso/latte/cappuccino)
def drink_choice():
    """
    Returns drink based on user choice.
    """
    drink = int(input("What would you like? Enter number for drink (1 - espresso/ 2 - latte/ 3 - cappuccino): "))

    if drink == 1:
        return "espresso"
    elif drink == 2:
        return "latte"
    elif drink == 3:
        return "cappuccino"
    elif drink == 4:
        return "off"
    elif drink == 5:
        return "report"
    else:
        return "Invalid choice"


# Alter to turn off coffee machine


# Print resources inside coffee machine by entering 'report'
def show_report(resource):
    water = resource["water"]
    milk = resource["milk"]
    coffee = resource["coffee"]
    money = resource["money"]
    return f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: ${money}"


# Check if machine has enough resources

# Process money
def process_transaction():
    quarters = int(input("How many quarters: ")) * .25
    dimes = int(input("How many dimes: ")) * .1
    nickels = int(input("How many nickels: ")) * .05
    pennies = int(input("How many pennies: ")) * .01
    total = quarters + dimes + nickels + pennies
    return round(total, 2)


# Check for transaction success
def transaction_is_successful(payment, drink):
    if payment > MENU[drink]["cost"]:
        return True
    else:
        return False


def is_enough_resources(machine, coffee):
    coffee_ingredients = coffee["ingredients"]
    is_enough = True
    if "milk" not in coffee_ingredients.values():
        if machine["water"] < coffee_ingredients["water"]:
            print("Not enough water.")
            is_enough = False
        if machine["coffee"] < coffee_ingredients["coffee"]:
            print("Not enough coffee.")
            is_enough = False
    else:
        if machine["water"] < coffee_ingredients["water"]:
            print("Not enough water.")
            is_enough = False
        if machine["coffee"] < coffee_ingredients["coffee"]:
            print("Not enough coffee.")
            is_enough = False
        if machine["milk"] < coffee_ingredients["milk"]:
            print("Not enough milk.")
            is_enough = False
    return is_enough


# Update resources
def update_resources(machine, coffee):
    coffee_ingredients = coffee["ingredients"]
    water = machine["water"]
    milk = machine["milk"]
    coffee = machine["coffee"]
    money = machine["money"]
    if "milk" not in coffee_ingredients.values():
        water -= coffee_ingredients["water"]
        coffee -= coffee_ingredients["coffee"]
    else:
        water -= coffee_ingredients["water"]
        milk -= coffee_ingredients["milk"]
        coffee -= coffee_ingredients["coffee"]
    print(f"Machine currently has:\nWater: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: ${money}")
    return machine


def coffee_machine():
    isMachineOn = True
    machine_resources = resources
    machine_resources["money"] = 0
    while isMachineOn:
        # GET USER'S DRINK CHOICE
        user_drink = drink_choice()
        # CHECK FOR REPORT OR OFF
        if user_drink == "report":
            resource_report = show_report(machine_resources)
            print(resource_report)
        elif user_drink == "off":
            print("Powering off coffee machine...")
            isMachineOn = False
        else:
            # CHECK FOR MACHINE RESOURCES
            if is_enough_resources(machine_resources, MENU[user_drink]):
                user_payment = process_transaction()
                # CHECK IF USER HAS ENOUGH MONEY
                if transaction_is_successful(user_payment, user_drink):
                    # UPDATE MACHINE RESOURCES
                    machine_resources["money"] += user_payment
                    machine_resources = update_resources(machine_resources, MENU[user_drink])
                    # Produce coffee
                    print(f"Payment successful. Here is your {user_drink}.")
                else:
                    print("Insufficient funds.")
            else:
                print("Not enough")


coffee_machine()
