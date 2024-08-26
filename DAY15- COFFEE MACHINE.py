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
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money":0
}
run_again=True
def check_resources(MENU,resources):
    if customer_choice=='espresso':
        if MENU['espresso']['ingredients']['water']<=resources['water'] and MENU['espresso']['ingredients']['coffee']<=resources['coffee']:
            return True
        else:
            return False
    elif customer_choice=='latte':
        if MENU['latte']['ingredients']['water']<=resources['water'] and MENU['latte']['ingredients']['coffee']<=resources['coffee'] and MENU['latte']['ingredients']['milk']<=resources['milk']:
            return True
        else:
            return False
    elif customer_choice=='cappuccino':
        if MENU['cappuccino']['ingredients']['water']<=resources['water'] and MENU['cappuccino']['ingredients']['coffee']<=resources['coffee'] and MENU['cappuccino']['ingredients']['milk']<=resources['milk']:
            return True
        else:
            return False

def resource_shortage(MENU,resources):
    if customer_choice=='espresso':
        if MENU['espresso']['ingredients']['water'] > resources['water']:
            return'water'
        if MENU['espresso']['ingredients']['coffee'] > resources['coffee']:
            return 'coffee'
    elif customer_choice=='latte':
        if MENU['latte']['ingredients']['water']>resources['water']:
            return 'water'
        if MENU['latte']['ingredients']['coffee']>resources['coffee']:
            return 'coffee'
        if MENU['latte']['ingredients']['milk']>resources['milk']:
            return 'milk'
    elif customer_choice=='cappuccino':
        if MENU['cappuccino']['ingredients']['water']>resources['water']:
            return 'water'
        if MENU['cappuccino']['ingredients']['coffee']>resources['coffee']:
            return 'coffee'
        if MENU['cappuccino']['ingredients']['milk']>resources['milk']:
            return 'milk'

def deduct_resources(MENU,resources):
    if customer_choice=='espresso':
        resources['water']=resources['water']-MENU['espresso']['ingredients']['water']
        resources['coffee']=resources['coffee']-MENU['espresso']['ingredients']['coffee']
    elif customer_choice=='latte':
        resources['water'] = resources['water'] - MENU['latte']['ingredients']['water']
        resources['coffee']=resources['coffee']-MENU['latte']['ingredients']['coffee']
        resources['milk']=resources['milk']-MENU['latte']['ingredients']['milk']
    elif customer_choice=='cappuccino':
        resources['water'] = resources['water'] - MENU['cappuccino']['ingredients']['water']
        resources['coffee'] = resources['coffee'] - MENU['cappuccino']['ingredients']['coffee']
        resources['milk'] = resources['milk'] - MENU['cappuccino']['ingredients']['milk']

while run_again==True:
    customer_choice=input("what would you like? (espresso/latte/cappuccino) : ").lower()
    if customer_choice=='off':
        break
    elif customer_choice=='report':
        water=resources['water']
        milk=resources['milk']
        coffee=resources['coffee']
        money=resources['money']
        print(f"water : {water}ml\nmilk : {milk}ml\ncoffee : {coffee}g\nmoney : ${money}")
    elif customer_choice=='latte' or 'espresso' or 'cappuccino':
        output=check_resources(MENU,resources)
        if output==True:
            deduct_resources(MENU,resources)
            print("Please insert coins.")
            quarters=int(input("How many quarters ? : "))
            dimes=int(input("How many dimes ? : "))
            nickles=int(input("How many nickles ? : "))
            pennies=int(input("How many pennies ? : "))
            amount=quarters*0.25+dimes*0.10+nickles*0.05+pennies*0.01
            if customer_choice=='espresso':
                if amount==MENU['espresso']['cost']:
                    print("Here is your espresso ☕ Enjoy ! ")
                    resources['money']+=MENU['espresso']['cost']
                elif amount>MENU['espresso']['cost']:
                    change=amount-MENU['espresso']['cost']
                    resources['money'] += MENU['espresso']['cost']
                    print(f"Here is {change} in change.")
                    print("Here is your espresso ☕ Enjoy ! ")

                else:
                    print("Sorry that's not enough money. Money refunded.")

            elif customer_choice=='latte':
                if amount==MENU['latte']['cost']:
                    print("Here is your latte ☕ Enjoy ! ")
                    resources['money']+=MENU['latte']['cost']
                elif amount>MENU['latte']['cost']:
                    change=round(amount-MENU['latte']['cost'],2)
                    resources['money'] += MENU['latte']['cost']
                    print(f"Here is ${change} in change.")
                else:
                    print("Sorry that's not enough money. Money refunded.")

            elif customer_choice=='cappuccino':
                if amount==MENU['cappuccino']['cost']:
                    print("Here is your cappuccino ☕ Enjoy ! ")
                    resources['money']+=MENU['cappuccino']['cost']
                elif amount>MENU['cappuccino']['cost']:
                    change=amount-MENU['cappuccino']['cost']
                    resources['money'] += MENU['cappuccino']['cost']
                    print(f"Here is {change} in change.")
                else:
                    print("Sorry that's not enough money. Money refunded.")

        else:
            shortage=resource_shortage(MENU, resources)
            print(f"Sorry there is not enough {shortage}.")







