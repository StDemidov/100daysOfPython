from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

user_answer = "on"

money_coffee_machine = MoneyMachine()
coffee_machine = CoffeeMaker()
COFFEE_MENU = Menu()

while user_answer != "off":
    user_answer = input(f"What would you like? ({COFFEE_MENU.get_items()}): ").lower()
    if user_answer == 'report':
        coffee_machine.report()
        money_coffee_machine.report()
    elif user_answer != 'off':
        coffee = COFFEE_MENU.find_drink(user_answer)
        if coffee_machine.is_resource_sufficient(coffee) and money_coffee_machine.make_payment(coffee.cost):
            coffee_machine.make_coffee(coffee)

