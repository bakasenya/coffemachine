MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 30000,
    "milk": 20000,
    "coffee": 10000,
}

money_earned = 0

def print_report():
    """ Prints the current resource status and money earned. """
    global money_earned
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    
    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money_earned:.2f}"

def process_coins():
    """Processes coins and returns the total."""
    quarters = 0.25
    dimes = 0.10
    nickels = 0.05
    pennies = 0.01

    user_quarters = int(input("How many quarters?: "))
    user_dimes = int(input("How many dimes?: "))
    user_nickels = int(input("How many nickels?: "))
    user_pennies = int(input("How many pennies?: "))

    total = (user_quarters * quarters) + (user_dimes * dimes) + (user_nickels * nickels) + (user_pennies * pennies)
    return total

def sufficient_resources(drink):
    """ Checks if there are enough resources to make the selected drink. """
    if drink in MENU:
        for item , amount in MENU[drink]["ingredients"].items():
            if resources.get(item, 0) < amount:
                print(f"Sorry there isn't enough {item}")
                return False
        print("Please insert Coins.")
        payment = process_coins()
        drink_cost = MENU[drink]["cost"]
        if payment >= drink_cost:
            change = round(payment - drink_cost, 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        print("Enter a valid response.")
        return False

def update_report(drink):
    """ Deducts the ingredients used from resources and updates money earned. """
    global money_earned
    for item, amount in MENU[drink]["ingredients"].items():
        resources[item] -= amount
    money_earned += MENU[drink]["cost"]
    print(f"Here is your {drink} ☕. Enjoy!")
    return resources

def make_coffee():
    global money_earned
    is_on = True

    while is_on:
        user_input = input("What would you like to have? (espresso/latte/cappuccino): ").lower()
        if user_input == "off":
            print("Turning off the coffee machine. Goodbye!")
            break
        elif user_input == "report":
            print(print_report())
        elif user_input in MENU:
            if sufficient_resources(user_input):
                update_report(user_input)
        else:
            print("Invalid input. Please choose a valid option.")
        

make_coffee()



