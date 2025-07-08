class MenuItem:
    def __init__(self, name, ingredients, cost):
        self.name = name
        self.ingredients = ingredients
        self.cost = cost

class Menu:
    def __init__(self):
        self.items = {
            "espresso": MenuItem("espresso", {"water": 50, "coffee": 18}, 1.5),
            "americano": MenuItem("americano", {"water": 150, "coffee": 18}, 2.0),
            "latte": MenuItem("latte", {"water": 50, "coffee": 18, "milk": 150}, 2.5),
            "cappuccino": MenuItem("cappuccino", {"water": 50, "coffee": 18, "milk": 100}, 2.5),
            "flat_white": MenuItem("flat_white", {"water": 50, "coffee": 18, "milk": 120}, 2.7),
            "macchiato": MenuItem("macchiato", {"water": 50, "coffee": 18, "milk": 20}, 2.2),
            "cafe_au_lait": MenuItem("cafe_au_lait", {"water": 100, "coffee": 18, "milk": 100}, 2.4),
            "cold_brew": MenuItem("cold_brew", {"coffee": 20, "water": 200}, 2.8),
            "frappuccino": MenuItem("frappuccino", {"coffee": 18, "milk": 100, "water": 50}, 3.0)
        }

    def get_items(self):
        return list(self.items.keys())

    def find_drink(self, name):
        return self.items.get(name)

class CoffeeMaker:
    def __init__(self):
        self.resources = {"water": 1000, "milk": 500, "coffee": 300}

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        for ingredient, amount in drink.ingredients.items():
            if self.resources.get(ingredient, 0) < amount:
                print(f"Sorry, there is not enough {ingredient}.")
                return False
        return True

    def make_coffee(self, drink):
        for ingredient, amount in drink.ingredients.items():
            self.resources[ingredient] -= amount
        print(f"Here is your {drink.name}. Enjoy!")

class MoneyMachine:
    COIN_VALUES = {"quarters": 0.25, "dimes": 0.10, "nickels": 0.05, "pennies": 0.01}

    def __init__(self):
        self.money = 0.0

    def report(self):
        print(f"Money: ${self.money}")

    def process_coins(self):
        print("Please insert coins.")
        total = 0
        for coin, value in self.COIN_VALUES.items():
            count = int(input(f"How many {coin}?: "))
            total += count * value
        return round(total, 2)

    def make_payment(self, cost):
        amount_received = self.process_coins()
        if amount_received >= cost:
            change = round(amount_received - cost, 2)
            if change > 0:
                print(f"Here is your change: ${change}")
            self.money += cost
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False

# ----------- Main Program -----------
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
print("Welcome to the OOP Cafe!")

while is_on:
    options = "/".join(menu.get_items())
    choice = input(f"What would you like? ({options}): ").lower()
    
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice in menu.get_items():
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    else:
        print("Invalid choice. Please try again.")
