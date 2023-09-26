from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
#coffee_machine.report()
coffee_menu = Menu()
money_machine = MoneyMachine()
print(coffee_menu.get_items())

operate = True
while operate:
    coffee_choice = input("Please choose a coffee drink from menu: ")

    my_coffee = coffee_menu.find_drink(coffee_choice)
    if my_coffee == None:
        continue

    if not coffee_machine.is_resource_sufficient(my_coffee):
        continue

    if money_machine.make_payment(my_coffee.cost):
        coffee_machine.make_coffee(my_coffee)
    coffee_machine.report()
    money_machine.report()