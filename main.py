MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 120,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 200,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 250,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def res_deduction():
    resources['money'] += MENU[type_coffee]['cost']
    resources['water'] -= MENU[type_coffee]['ingredients']["water"]
    resources['milk'] -= MENU[type_coffee]['ingredients']['milk']
    resources['coffee'] -= MENU[type_coffee]['ingredients']['coffee']


while True:
    type_coffee = input('\n#MENU#\n'
                        'Espresso:' + str(MENU["espresso"]["cost"])+'\n'
                        'Cappuccino:' + str(MENU["cappuccino"]["cost"])+'\n'
                        'Latte:' + str(MENU["latte"]["cost"])+'\n'
                        'What type of coffee do you want??\n')

    if type_coffee == 'report':
        print(resources)
    else:
        print('please insert money')
        money = int(input())
        change = money - MENU[type_coffee]['cost']
        if change > 0 and resources['water'] > MENU[type_coffee]['ingredients']["water"] and resources['milk'] > MENU[type_coffee]['ingredients']['milk'] and resources['coffee'] > MENU[type_coffee]['ingredients']['coffee']:
            print(f'here is your change:{change}')
            print('Thanks for your order.')
            res_deduction()
        elif change>0 and (resources['water'] > MENU[type_coffee]['ingredients']["water"] or resources['milk'] > MENU[type_coffee]['ingredients']['milk'] or resources['coffee'] > MENU[type_coffee]['ingredients']['coffee']):
            print('Sorry insufficient resources.\n'
                  'Money has been refunded.\n'
                  'Please refill the depleting resources:\n')
            print(resources)
            break
        elif change < 0:
            print("Sorry that's not enough money. Money refunded")
        else:
            print('Thanks for your order.')
