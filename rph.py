import random

class Character:
    def __init__(self, name, maxhp, hp, attack, alive):
        self.name = name
        self.maxhp = maxhp
        self.hp = hp
        self.attack = attack 
        self.alive = alive            

    def hpDecrease(self, amount):
    	self.hp -= amount
    	if self.hp <= 0:
    		self.alive = False
    def hpIncrease(self, amount):
    	self.hp += amount
    	if self.hp < self.maxhp:
    		self.hp = self.maxhp

class Player(Character):
	self.name = ""
	self.maxhp = 0
	self.attack = 0
	self.alive = True

class Fighter(Player):
	self.name = "Fighter"
	self.maxhp = 15
	self.attack = random.randrange(0, 5)
	self.alive = True

class Mage(Player):
	self.name = "Mage"
	self.maxhp = 10
	self.attack = random.randrange(0, 10)
	self.alive = True

class Archer(Player):
	self.name = "Archer"
	self.maxhp = 5
	self.attack = random.randrange(5, 10)
	self.alive = True

class Monster(Character):
	self.name = ""
	self.maxhp = 0
	self.attack = 0
	self.alive = True

class Wolf(Monster):
	self.name = "Wolf"
	self.maxhp = 15
	self.attack = random.randrange(0, 2)
	self.alive = True


class Goblin(Monster):
	self.name = "Goblin"
	self.maxhp = 5
	self.attack = random.randrange(0, 5)
	self.alive = True


class PoisinIvy(Monster):
	self.name = "Posin Ivy"
	self.maxhp = 10
	self.attack = 5
	self.alive = True










def main():

if __name__ == "__main__":
main()
