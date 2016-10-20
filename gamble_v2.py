import random, time, sys

gold = 0
name = ""

#Typing effect!
def main_third():
	global name, gold, gambles
	print("You bet", gamble_a ,"good luck")
	dealer_roll = random.randrange(1, 6)
	player_gusse = int(input("Gusse the die roll!"))
	if player_gusse == dealer_roll:
		gold ** gold
	else:
		gambles -= gold
	









def main_second():
	global name, gold, gambles
	print("  Ready to gamble? you have", gold ,"gold good luck!")
	gambles = int(input("\n  The dealer is going to roll the dice\n  Bet the amount of money you want to gamble."))
	if gambles > gold:
		print("\n  You dont have that amount of money please try again")
		main_second()
	elif gambles == gold:
		print("\n  You bet your whole hand good luck!")
		main_third()
	else:
		print("\n  You bet", gold ,"gold good luck!")
		main_third()













def gamble_second():
	global gold, name, life
	life = 3
	gamble = random.randrange(1, 6)
	gusse = int(input("\nGusse the number.\n"))
	if gamble == gusse:
		print("  The Rollers rolls a", gamble ,"\n  You Win congratulations!")
		print("You win!")
		gold += 12
		print("You have ", gold ,"gold.")
		main_second()
	else:
		print("  The Rollers rolls a", gamble ,"\n  You Lose congratulations!")
		gold -= 3
		life -= 1
		if life == 0:
			main_second()
		else:
			print("You have ", gold ,"gold.")
			gamble_second()
	
def gamble_start():
	print("\n  [:CARTER:]  I'm going to roll a die, try to gusse which side it lands on\n  You have 3 trys to gusse it correctly.")
	print("\n  [:BANKER:]  You have", gold ,"gold good luck!")
	gamble_second()
def main_start():
	global name
	name = input("  What is your name? \n[:\n:]") 
	print("Hello", name , "nice to meet you.\n  I'm going to let you gamble for some money good luck!")
	gamble_start()
main_start()
