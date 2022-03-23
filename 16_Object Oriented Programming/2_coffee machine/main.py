from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    select_menu = input("What would you like? (espresso/latte/cappuccino/) : ")
    print(select_menu)
    if select_menu == "off":
        pass
    elif select_menu == "report":
        CoffeeMaker().report()
    else:
        return select_menu

main()