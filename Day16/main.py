from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

work = True

while work:
    requirement = input(f"What would you like? {menu.get_items()}: ")
    if requirement == "report":
        coffee_maker.report()
        money_machine.report()
    elif requirement == "off":
        work = False
        print("OFF")
    else:
        order = menu.find_drink(requirement)
        if coffee_maker.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
            coffee_maker.make_coffee(order)
