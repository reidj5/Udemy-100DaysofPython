menu = {
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
    "coffee": 150,
}


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f'Sorry there is not enough {item}.')
            return False
    return True


isOn = True
while isOn:
    choice = input("What would you like: ")
    if choice == 'Off':
        isOn = False
    elif choice == 'report':
        for resource in resources:
            if resource == 'coffee':
                print(resource.capitalize() + " " + str(resources[resource]) + ' g')
            else:
                print(resource.capitalize() + " " + str(resources[resource]) + ' ml')
    else:
        drink = menu[choice]
        if is_resource_sufficient(drink["ingredients"]):


