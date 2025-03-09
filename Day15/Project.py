# Coffee Machine

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

money = 0.0

work = True

def report():
    for key in resources:
        if key == "water":
            print(f"Water : {resources[key]}ml")
        elif key == "milk":
            print(f"Milk : {resources[key]}ml")
        elif key == "coffee":
            print(f"Coffee : {resources[key]}ml")
    print(f"Money: ${money}")

def sufficient(order):
    for key in MENU[order]["ingredients"]:
        if MENU[order]["ingredients"][key] > resources[key]:
            print(f"Sorry there is not enough {key}.")
            return False
    return True

def coin(order):
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    sum = round(quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01, 2)
    order_cost = MENU[order]["cost"]
    if sum < order_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif sum > order_cost:
        change = round(sum - order_cost, 2)
        print(f"Here is ${change} in  change")
    return True
        
def make(order):
    for key in MENU[order]["ingredients"]:
        resources[key] -= MENU[order]["ingredients"][key]
    print(f"Here is your {order}. Enjoy!")
    return MENU[order]["cost"]

while work:
    requirement = input("What would you like? (espresso/latte/cappuccino): ")
    if requirement == "report":
        report()
    elif requirement == "off":
        work = False
        print("OFF")
    elif requirement == "espresso" or requirement == "latte" or requirement == "cappuccino":
        if sufficient(requirement) and coin(requirement):
            money += make(requirement)
        else:
            work = False
    

