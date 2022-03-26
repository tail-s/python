from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 객체 생성
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What owould you like? ({options}) : ")
    if choice == "off":
        is_on = False

    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    elif choice in options:
        drink = menu.find_drink(choice)
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        is_enough_successful = money_machine.make_payment(drink.cost)

        if is_enough_successful and is_enough_ingredients:
            coffee_maker.make_coffee(drink)
        # if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
        #         coffee_maker.make_coffee(drink)

    else:
        print("Please, Check your order again.") # 어렵다 어려워