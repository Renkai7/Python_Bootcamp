from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# SHOW MENU
show_menu = menu.get_items()

isMachineOn = True
while isMachineOn:
    # Ask user to choose drink
    user_choice = input(f"What would you like? ({show_menu}): ").lower()

    if user_choice == "report":
        # SHOW REPORT
        coffee_maker.report()
        money_machine.report()
    elif user_choice == "off":
        isMachineOn = False
        print("Shutting down coffee machine.")
    else:
        # Assign drink to user
        user_drink = menu.find_drink(user_choice)
        if user_drink is not None:
            # CHECK MACHINE RESOURCES
            if coffee_maker.is_resource_sufficient(user_drink):
                if money_machine.make_payment(user_drink.cost):
                    coffee_maker.make_coffee(user_drink)

