import time, random

class Money:
	def __init__(self, startingValue = 0):
		self.value = startingValue

	def get(self):
		return self.value

	def increase(self, amount):
		self.value += amount

	def decrease(self, amount):
		if self.canAfford(amount):
			self.value -= amount
		else:
			raise Exception("Can't afford")

	def canAfford(self, amount):
		return self.value >= amount


class Building:
	def __init__(self, name, cost, moneyPerSecond):
		self.name = name
		self.cost = cost
		self.moneyPerSecond = moneyPerSecond
		self.quantity = 0

	def calcPerSecond(self):
		return self.moneyPerSecond * self.quantity

	def getData(self):
		return self.name + ": " + str(self.cost) + ", " + str(self.moneyPerSecond)


class Clicker:
	def __init__(self):
		self.money = Money()
		self.buildings = [
			Building("Lemonade Stand", 1000, 1),
			Building("Arnold Palmer Stand", 5000, 10),
			Building("Krusty Krab", 8478, 40),
			Building("Bank", 10000, 70),
			Building("Politics", 15000, 150)
		]
		self.clickerValue = 1

	def run(self):
		while True:
			inp = input('> (' + str(self.money.get()) + ') ')

			if inp == "quit":
				self.save()
				break

			elif inp == "shop":
				self.shop()
				
			else:
				self.money.increase(self.clickerValue)

	def shop(self):
		for i in range(len(self.buildings)):
			print(i+1, self.buildings[i].getData())

		inp = int(input("Which one? "))

		if inp == 0:
			break
		else:
			assert (inp <= len(self.buildings))
			self.buildings[inp].quantity += 1



	def save(self):
		pass



def main():
	clicker = Clicker()
	clicker.run()






if __name__ == "__main__":
	main()