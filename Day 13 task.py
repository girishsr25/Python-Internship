#Day 13 Task
#Coffee Machine
import os

clear = lambda : os.system('cls')


class Bank:
	def __init__(self):
		self.amount = 0

	def add_money(self, quarters : int, dimes : int, nickles : int, pennies : int) -> None:
		self.amount += (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)

	def give_change(self,received : float, amount : float):
		if received < amount:
			return 'Amount too less'
		else:
			return amount - received

	def get_sum(self, quarters : int, dimes : int, nickles : int, pennies : int) -> float:
		return (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)


class Stock:
	def __init__(self):
		self.milk = 0
		self.water = 0
		self.coffee = 0

	def add_water(self, qty: int):
		self.water += qty

	def add_milk(self, qty : int):
		self.milk += qty

	def add_coffee(self, qty : int):
		self.coffee += qty




class Recipe:
	def __init__(self,bank : Bank):
		self.espresso   = {'water' : 100, 'milk' : 150, 'coffee' : 75, 'price' : 2.50}
		self.latte      = {'water' : 125, 'milk' : 180, 'coffee' : 90, 'price' : 5.00}
		self.cappuccino = {'water' :  75, 'milk' : 120, 'coffee' : 50, 'price' : 1.75}
		self.stock = Stock()
		self.bank = bank
		self.order = None

	def get_recipe(self, type : str, amount : float = 10000):
		self.served = False
		self.order = type
		if type == 'Espresso':
			if amount >= self.espresso['price']:
				if self.stock.milk >= self.espresso['milk']:
					if self.stock.water >= self.espresso['water']:
						if self.stock.coffee >= self.espresso['coffee']:
							self.served = True
							self.stock.add_water(-self.espresso['water'])
							self.stock.add_coffee(-self.espresso['coffee'])
							self.stock.add_milk(-self.espresso['milk'])
							self.get_money(self.espresso['price'])
			else:
				print('Insufficient amount')
				return
			if not self.served:
				print('Stocks are too low...contact a salesperson')

		if type == 'Latte':
			if amount >= self.latte['price']:
				if self.stock.milk >= self.latte['milk']:
					if self.stock.water >= self.latte['water']:
						if self.stock.coffee >= self.latte['coffee']:
							self.served = True
							self.stock.add_water(-self.latte['water'])
							self.stock.add_coffee(-self.latte['coffee'])
							self.stock.add_milk(-self.latte['milk'])
							self.get_money(self.latte['price'])
			else:
				print('Insufficient amount')
				return
			if not self.served:
				print('Stocks are too low...contact a salesperson')

		if type == 'Cappuccino':
			if amount >= self.cappuccino['price']:
				if self.stock.milk >= self.cappuccino['milk']:
					if self.stock.water >= self.cappuccino['water']:
						if self.stock.coffee >= self.cappuccino['coffee']:
							self.served = True
							self.stock.add_water(-self.cappuccino['water'])
							self.stock.add_coffee(-self.cappuccino['coffee'])
							self.stock.add_milk(-self.cappuccino['milk'])
							self.get_money(self.cappuccino['price'])
			else:
				print('Insufficient amount')
				return
			if not self.served:
				print('Stocks are too low...contact a salesperson')

	def add_stock(self):
		milk = float(input('Enter the Milk stock:'))
		self.stock.add_milk(milk)

		water = float(input('Enter the Water stock:'))
		self.stock.add_water(water)

		coffee = float(input('Enter the Coffee stock:'))
		self.stock.add_coffee(coffee)

	def get_report(self):
		print(f'Water : {self.stock.water}')
		print(f'Milk  : {self.stock.milk}')
		print(f'Coffee: {self.stock.coffee}')
		print(f'Money : {self.bank.amount}')

	def get_money(self,price):
		quarters = int(input('Quarters:'))
		dimes    = int(input('Dimes:'))
		nickels  = int(input('Nickels:'))
		pennies  = int(input('Pennies:'))

		amount = self.bank.get_sum(quarters, dimes, nickels, pennies)
		

		if amount >= price:
			self.bank.add_money(quarters, dimes, nickels, pennies)
			print(f'Enjoy your {self.order}')
			change = amount - price
			if change > 0:
				print(f'Here you go....have your change of ${change}')
				self.bank.amount -= change
		else:
			print(f'Insufficient funds...try again')

		return amount





class Coffee_Machine:
	def __init__(self):
		self.option = None
		
		self.bank = Bank()
		self.bank.amount = 500
		self.recipe = Recipe(self.bank)
		self.get_input()




	def get_input(self):
		print("Enter your choice :(1.espresso/2.latte/3.cappuccino)")
		choice = 0
		try:
			choice = input()
			clear()
			choice = int(choice)
		except:
			if choice == 'off':
				exit(1)
			if choice == 'report':
				self.recipe.get_report()
				self.get_input()

			if choice == 'add':
				self.recipe.add_stock()
				self.get_input()
			
			print('Bad Input \n Try again')
			self.get_input()

		if choice == 1:
			self.option = 'Espresso'
			self.recipe.get_recipe(self.option)

		elif choice == 2:
			self.option = 'Latte'
			self.recipe.get_recipe(self.option)

		else:
			self.option = 'Cappuccino'
			self.recipe.get_recipe(self.option)

		self.get_input()

	def print_details(self):
		print(self.option)


starbucks = Coffee_Machine()







		

