# Assignment 2: Modular Sandwich Maker
# Katrina Wilson, kwils178@uncc.edu
# Reorganized and refined code from my original Assignment 1

import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()
machine = sandwich_maker_instance

def main():
    while True:
        choice = input("What would you like? (small/medium/large/off/report): ")
        if choice == "off":
            print("Turning off the machine...")
            break
        elif choice == "report":
            machine.report()
        elif choice in ["small", "medium", "large"]:
            sandwich = recipes[choice]
            if machine.check_resources(sandwich["ingredients"]):
                print("Please insert coins.")
                coins_inserted = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins_inserted, sandwich["cost"]):
                    machine.make_sandwich(choice, sandwich["ingredients"])
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()