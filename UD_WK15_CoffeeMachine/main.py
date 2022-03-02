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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resources_sufficient(order_ingredient):
    """Returns True when the orders can be made, False when the ingredients are insufficient."""
    for items in order_ingredient:
        if order_ingredient[items] >= resources[items]:
            print(f"Sorry, there is no enough {items}.")
            return False
    return True


def insert_coins():
    """Returns the total calculated from the coins inserted."""
    print("Please inserts coins:")
    total = int(input("How many quarters:"))*0.25
    total += int(input("How many dimes:"))*0.1
    total += int(input("How many nickles:"))*0.05
    total += int(input("How many pennies:"))*0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, False if the payment is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change: ${change}.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, the payment is insufficient. Payment has been refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for items in order_ingredients:
        resources[items] -= order_ingredients[items]
    print(f"Here is your {drink_name}☕")


is_on = True
while is_on:
    choice = input("What would you like?(espresso/latte/cappuccino:)")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water :{resources['water']} ml")

        print(f"Milk : {resources['milk']} ml")

        print(f"Coffee : {resources['coffee']} g")

        print(f"Money : ${profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink['ingredients']):
            payment = insert_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])










