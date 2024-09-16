### Data ###
recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item, quantity in ingredients.items():
            if self.machine_resources[item] < quantity:
                print(f"Sorry there is not enough {item}")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        largedollars = int(input("How many large dollars?: "))
        halfdollars = int(input("How many half dollars?: "))
        quarters = int(input("How many quarters?: "))
        nickels = int(input("How many nickels?: "))

        total = largedollars * 1.00 + halfdollars * 0.50 + quarters * 0.25 + nickels * 0.05
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = coins - cost
            if change > 0:
                print(f"Here is ${change} in change.")
            return True
        else:
            print(f"Sorry there is not enough money! Money refunded.")
            return False


    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item, quantity in order_ingredients.items():
            self.machine_resources[item] -= quantity
        print(f"{sandwich_size} sandwich is ready for you. Bon appetit! ")


    def report(self):
        """Function that will create a report of all ingredients"""
        print(f"Bread: {self.machine_resources['bread']} slice(s) left.")
        print(f"Ham: {self.machine_resources['ham']} slice(s) left.")
        print(f"Cheese: {self.machine_resources['cheese']} ounces left.")

### Make an instance of SandwichMachine class and write the rest of the codes ###

machine = SandwichMachine(resources)

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
                coins_inserted = machine.process_coins()
                if machine.transaction_result(coins_inserted, sandwich["cost"]):
                    machine.make_sandwich(choice, sandwich["ingredients"])
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()