espresso = {"water":100,"milk":150,"coffee":50,"price":4.70}
latte = {"water":110,"milk":120,"coffee":60,"price":5.50}
capuccino = {"water":90,"milk":80,"coffee":70,"price":3.20}
water = milk = coffee = 1000
while True:
    print("What would you like to have?(espresso-$4.70/latte-$5.50/capuccino-$3.20)")
    choice = input()
    if choice == 'espresso':
        print("espresso")
        if water >= espresso['water'] and milk >= espresso['milk'] and coffee >=espresso['coffee']:
            print("Please insert the amount in the machine")
            q = float(input("Enter the quarters: "))
            d = float(input("Enter the dimes: "))
            n = float(input("Enter the nickles: "))
            p = float(input("Enter the pennies: "))
            amount = (q*0.25) + (d*0.1) + (n*0.05) + (p*0.01)
            print(f'Inserted amount',amount)
            if amount == espresso['price']:
                print("Enjoy your espresso!")
            elif amount > espresso['price']:
                print("Enjoy your espresso!")
                print("please take the change..")
                print(amount-espresso['price'])
                water = water - espresso['water']
                milk = milk - espresso['milk']
                coffee = coffee - espresso['coffee']
            else:
                print("Please enter the sufficient amount")
        else:
            print("Sorry temporarily unavilable due to low stock")
    elif choice == 'latte':
        print("latte")
        if water >= latte['water'] and milk >= latte['milk'] and coffee >=latte['coffee']:
            print("Please insert the amount in the machine")
            q = float(input("Enter the quarters: "))
            d = float(input("Enter the dimes: "))
            n = float(input("Enter the nickles: "))
            p = float(input("Enter the pennies: "))
            amount = (q*0.25) + (d*0.1) + (n*0.05) + (p*0.01)
            print(f'Inserted amount',amount)
            if amount == latte['price']:
                print("Enjoy your latte!")
            elif amount > latte['price']:
                print("Enjoy your latte!")
                print("please take the change..")
                print(amount-latte['price'])
                water = water - latte['water']
                milk = milk - latte['milk']
                coffee = coffee - latte['coffee']
            else:
                print("Please enter the sufficient amount")
        else:
            print("Sorry temporarily unavilable due to low stock")
    elif choice == 'capuccino':
        print("capuccino")
        if water >= capuccino['water'] and milk >= capuccino['milk'] and coffee >=capuccino['coffee']:
            print("Please insert the amount in the machine")
            q = float(input("Enter the quarters: "))
            d = float(input("Enter the dimes: "))
            n = float(input("Enter the nickles: "))
            p = float(input("Enter the pennies: "))
            amount = (q*0.25) + (d*0.1) + (n*0.05) + (p*0.01)
            print(f'Inserted amount',amount)
            if amount == capuccino['price']:
                print("Enjoy your capuccino!")
            elif amount > capuccino['price']:
                print("Enjoy your capuccino!")
                print("please take the change..")
                print(amount-capuccino['price'])
                water = water - capuccino['water']
                milk = milk - capuccino['milk']
                coffee = coffee - capuccino['coffee']
            else:
                print("Please enter the sufficient amount")
        else:
            print("Sorry temporarily unavilable due to low stock")
            
    elif choice == 'report':
        print(f'Water: ',water)
        print(f'Milk :',milk)
        print(f'Coffee :',coffee)
    elif choice == 'off':
        break
    elif choice == 'add':
        print("Adding extra stocks..")
        m = int(input("Add Milk: "))
        w = int(input("Add Water: "))
        c = int(input("Add Coffee: "))
        milk = m + milk
        water = w + water
        coffee = c + coffee
        
        
