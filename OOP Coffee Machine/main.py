from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
money = MoneyMachine()
menu = Menu()
items = {
    "espresso": [MenuItem("espresso", 50, 0, 18, 1.5), 1.5],
    "latte": [MenuItem("latte", 200, 150, 24, 2.5), 2.5],
    "cappuccino": [MenuItem("cappuccino", 250, 100, 24, 3.0), 3.0]
}
on = True

while on:
    choice = input(f"What would you like? {menu.get_items()}: ").lower()
    if choice == "off":
        on = False
    elif choice == "report":
        coffee.report()
        money.report()
    elif menu.find_drink(choice):
        if coffee.is_resource_sufficient(items[choice][0]):
            money.make_payment(items[choice][1])
            coffee.make_coffee(items[choice][0])
