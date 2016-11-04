import random
COLORS = ['yellow', 'red', 'blue', 'green']

class Actor:
	def __init__(self, name, hp, weapon, color, sound):
		self.name   = name
		self.hp     = hp
		self.hpMax  = self.hp
		self.weapon = weapon
		self.color  = color
		self.sound  = sound

	def battleCry(self):
		return self.sound.upper()


def main():
	actors = [
		Actor("Bob", 100, "Salad", "red", "REEEEEEEEEEEEEEEEEEEEE"),
		Actor("Kincade", 1, None, "black", "pepé memé")
	]

	for i in actors:
		print(i.name + " goes " + i.battleCry() + "!")

	pass

if __name__ == "__main__":
	main()



