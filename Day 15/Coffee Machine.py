from pygments.lexers import ml

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

def is_resource_sufficient(ordered_ingredients):
    for items in ordered_ingredients:
        if ordered_ingredients[items] > resources[items]:
            print(f'Sorry there is not enough {items}.')
            return False
    return True

def process_coins():
    print("Please enter coins")
    total = int(input('How many quarters?: '))*0.25
    total += int(input('How many dimes?: '))*0.1
    total += int(input('How many nickels?: '))*0.05
    total += int(input('How many pennies?: '))*0.01
    return total

def is_transaction_successful(money_inserted,drink_cost):
    if money_inserted >= drink_cost:
        change = round(money_inserted - drink_cost,2)
        print(f"Here is your ${change}")
        return True
    else:
        print("Sorry that's not enough money, Money refunded.")
        return False

def make_coffee(name, ordered_ingredients):
    for items in ordered_ingredients:
        resources[items] -= ordered_ingredients[items]
    print(f"Here is your {name}coffee.")

machine_off = False

while not machine_off:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'off':
        machine_off = True
    elif choice == 'report':
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
    else:
        drink_name = MENU[choice]
        if is_resource_sufficient(drink_name['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink_name['cost']):
                make_coffee(choice, drink_name['ingredients'])
