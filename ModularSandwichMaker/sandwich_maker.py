
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item, quantity in ingredients.items():
            if self.machine_resources[item] < quantity:
                print(f"Sorry there is not enough {item}")
                return False
        return True

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