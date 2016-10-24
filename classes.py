
def battle(actor1, actor2):
	actorFighting = actor1
	actorDefending = actor2
	winner = None

	while True:
		print(actorFighting.name + " deals", actorFighting.attackPower, "damage!")
		actorDefending.hpDecrease(actorFighting.attackPower)

		if actorDefending.alive:
			print(actorDefending.name + " has", actorDefending.hp, "HP left!")
		else:
			print(actorDefending.name + " died!")
			winner = actorFighting
			break

		actorFighting, actorDefending = actorDefending, actorFighting

		input()

	print("\n" + winner.name + " wins!")



class Actor:
	def __init__(self, name, hpMax, attackPower):
		self.name = name
		self.hpMax = hpMax
		self.hp = self.hpMax
		self.attackPower = attackPower
		self.alive = True

	def hpDecrease(self, amount):
		self.hp -= amount
		if self.hp <= 0:
			self.alive = False

	def hpIncrease(self, amount):
		self.hp += amount
		if self.hp >= self.hpMax:
			self.hp = self.hpMax



def main():
	actors = [
		Actor("Pepe the Frog", 100, 10),
		Actor("Shrek", 200, 20),
		Actor("Kincade", 5, 1)
	]

	for i in actors:
		print(i.name)

	actor1 = None
	actor2 = None

	while True:
		selection = input("Choose an actor\n")
		for i in actors:
			if i.name == selection:
				if actor1 is None:
					actor1 = i
				else:
					actor2 = i
				break

		if actor2 is not None:
			break

	battle(actor1, actor2)






if __name__ == "__main__":
	main()