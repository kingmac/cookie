import sys, random, time
name = ""
gold = 0
left = 0
right = 0

def lrchoice():
	global name, left, right
	if left == 0:
		leftwyd = input("What should you do?")





def choiceAF():
	global left, right
	if left == 1:
		print("As you walk down the path you notice its scary theme its not good.\nYou feel things staring at you... what should you do?")
		left = 0
		lrchoice()
	elif right == 1:
		print("You walk down the path what do you want to do!")
		right = 0
		lrchoice()





def decion_q1():
	global name, left, right
	print("" + name +", There is a fork in the road.\nMake up your mind.")
	question1 = input("Do you want to go left or right:\n")
	if question1 == "Left".lower():
		print("You decided to walk left on the path")
		left = 1
		choiceAF()
	elif question1 == "right".lower():
		print("You decided to walk to the right, enjoy the path.")
		right = 1
		choiceAF()
	else:
		print("That was not a option!")



def main():
	global name, gold
	name = input("What is your name?:\n")
	print("Hello" + name +", nice to meet you!")
	time.sleep(1)
	decion_q1()




if __name__ == '__main__':
	main()
