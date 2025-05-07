coffee_machine = {
    "menu": {
        "espresso": { 
            "ingredients": {
                "water": 50,
                "coffee": 18
            },
            "cost": 1.5
        },
        "americano": {
            "ingredients": {
                "water": 150,
                "coffee": 18
            },
            "cost": 2.0
        },
        "latte": {
            "ingredients": {
                "water": 50,
                "coffee": 18,
                "milk": 150
            },
            "cost": 2.5
        },
        "cappuccino": {
            "ingredients": {
                "water": 50,
                "coffee": 18,
                "milk": 100
            },
            "cost": 2.5
        },
        "flat_white": {
            "ingredients": {
                "water": 50,
                "coffee": 18,
                "milk": 120
            },
            "cost": 2.7
        },
        "macchiato": {
            "ingredients": {
                "water": 50,
                "coffee": 18,
                "milk": 20
            },
            "cost": 2.2
        },
        "cafe_au_lait": {
            "ingredients": {
                "water": 100,
                "coffee": 18,
                "milk": 100
            },
            "cost": 2.4
        },
        "cold_brew": {
            "ingredients": {
                "coffee": 20,
                "water": 200
            },
            "cost": 2.8
        },
        "frappuccino": {
            "ingredients": {
                "coffee": 18,
                "milk": 100,
                "water": 50
            },
            "cost": 3.0
        }
    },
    "resources": {
        "water": 1000,   # in milliliters
        "milk": 500,     # in milliliters
        "coffee": 300    # in grams
    }
}
bank = 0.0
menu_items = coffee_machine["menu"].keys()
print("Welcome to the Cafe")
def process_coins():
    """Returns the total amount of money inserted."""
    print("Please insert coins.")
    quarters = int(input("How many quarters ($0.25)?: "))  
    dimes = int(input("How many dimes ($0.10)?: "))        
    nickels = int(input("How many nickels ($0.05)?: "))    
    pennies = int(input("How many pennies ($0.01)?: "))    
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return round(total, 2)
is_on = True
def process_coins():
    """Returns the total amount of money inserted."""
    print("Please insert coins.")
    quarters = int(input("How many quarters ($0.25)?: "))  # 25 cents
    dimes = int(input("How many dimes ($0.10)?: "))        # 10 cents
    nickels = int(input("How many nickels ($0.05)?: "))    # 5 cents
    pennies = int(input("How many pennies ($0.01)?: "))    # 1 cent
    acc_quarters = quarters * 0.25
    acc_dimes = dimes * 0.10
    acc_nickels = nickels * 0.05
    acc_pennies = pennies * 0.01
    total = acc_quarters + acc_dimes + acc_nickels + acc_pennies
    return round(total, 2)
while is_on:
    choice = input("What would you like? (1)espresso/2)americano/3)latte/4)cappuccino/5)flat_white/6)macchiato/7)cafe_au_lait/8)cold_brew/9)frappuccino): ").lower()
    
    # Create variables for resources
    water = coffee_machine['resources']['water']
    milk = coffee_machine['resources']['milk']
    coffee = coffee_machine['resources']['coffee']

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${bank}")
    elif choice in coffee_machine["menu"]:
        drink = coffee_machine["menu"][choice]
        if all(coffee_machine["resources"].get(ingredient, 0) >= amount for ingredient, amount in drink["ingredients"].items()):
            print(f"The cost of {choice} is ${drink['cost']}")
            money_received = process_coins()
            if money_received >= drink["cost"]:
                change = round(money_received - drink["cost"])
                for ingredient, amount in drink["ingredients"].items():
                    coffee_machine["resources"][ingredient] -= amount
                print(f"Here is your {choice}. Enjoy!")
                print(f"Cost: ${drink['cost']}")
                if change > 0:
                    print(f"Here is your change: ${money_received - drink['cost']}")
                bank += drink["cost"]
            else:
                print("Sorry, that's not enough money. Money refunded.")
        else:
            print("Sorry, there is not enough resources.")
    else:
        print("Invalid choice. Please try again.")
