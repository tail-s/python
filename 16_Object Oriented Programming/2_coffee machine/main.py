from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    select_menu = input(f"What would you like? ({Menu().get_items()}) : ")
    print(select_menu)

    if select_menu in Menu().get_items():
        CoffeeMaker().is_resource_sufficient(Menu().find_drink(select_menu))
        pass

    elif select_menu == "report":
        CoffeeMaker().report()
        MoneyMachine().report()

    elif select_menu == "off":
        pass

    else:
        print("Please, Check your order again.")

main()