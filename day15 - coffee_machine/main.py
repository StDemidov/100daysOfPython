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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def get_money():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return round(quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01, 2)


def report_resources(cash):
    measure = "ml"
    for ingredient in resources:
        if ingredient == "coffee":
            measure = "g"
        print(f"{ingredient}: {resources[ingredient]}{measure}")
    print(f"Money: ${cash}")


def check_ingredients(coffee):
    for ingr in MENU[coffee]["ingredients"]:
        if resources[ingr] < MENU[coffee]["ingredients"][ingr]:
            print(f"Sorry, there is no enough {ingr}.")
            return False
    return True


def prepare_coffee(coffee, money, cash):
    money += MENU[coffee]['cost']
    print(f"Here is ${round(cash - MENU[coffee]['cost'], 2)} in change.")
    print(f"Here is your {coffee}. Enjoy!")
    for ingr in MENU[coffee]["ingredients"]:
        resources[ingr] -= MENU[coffee]["ingredients"][ingr]
    return money


user_answer = ""
money = 0

while user_answer != "off":
    cash = 0
    user_answer = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_answer == 'report':
        report_resources(money)
    elif user_answer != "off":
        if check_ingredients(user_answer) == True:
            cash = get_money()
            if cash < MENU[user_answer]['cost']:
                print("Sorry that's not enough money. Money refunded")
            money =  prepare_coffee(user_answer, money, cash)
