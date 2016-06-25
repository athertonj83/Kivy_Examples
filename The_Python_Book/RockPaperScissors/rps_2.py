#!/usr/bin/env python3

#this creates rock, paper, scissors from the Python book

import random
import time

rock=1
paper=2
scissors=3

#Dictionary of keys, I'm using this like a format
names={rock:"Rock", paper:"Paper",scissors:"Scissors"}
names_plural={rock:"Rocks are",paper:"Paper is",scissors:"Scissors are"}

#Which type wins over which others
rules={rock:scissors, paper:rock, scissors:paper}

#Starting conditions, vars keep ongoing score
human_score=0
comp_score=0


def start():
	print("Now let's play Rock, Paper, Scissors!")
	while game():
		pass
	scores()

#Referencing the modules used in the game, determining whether another game will be played
def game():
	player1=move()
	computer=random.randint(1,3)
	result(player1,computer)
	return play_again()

def move():
	while True:
		player=input("Rock?\nPaper?\nScissors?\nMake your move!:")
		print(player)
		if player.upper() in ("ROCK","PAPER","SCISSORS"):
			if player.upper()=="ROCK":
				player1=1
			elif player.upper()=="PAPER":
				player1=2
			else:
				player1=3
			return player1
	#except ValueError:
		#pass
	print("Eh? I didn't get that. I need you to enter Rock, Paper, or Scissors")

# This prints the results of the game (i.e. who won)
def result(player1,computer):
	print("3...")
	#time.sleep(1)
	print("2...")
	#time.sleep(1)
	print("1!")
	#time.sleep(0.5)
	print("Computer threw {0}".format(names[computer]))

	global human_score,comp_score
	if player1==computer:
		print("The game is tied!")
		human_score+=1
		comp_score+=1
	else:
		if rules[player1]==computer:
			print("Congratulations! Your ",format(names[player1]), " beat the Computer's ",format(names[computer]),". Go ",format(names[player1]),"! ",format(names_plural[computer])," for losers.",sep="")
			human_score+=1
		else:
			print("Shame. Your ",format(names[player1])," was beaten by the Computer's ",format(names[computer]),".",sep="")
			comp_score+=1

def play_again():
	answer=input("Another game? Y/N?")
	if answer.upper() in ("Y","YES"):
		return answer
	else:
		print("No more games? Ok...See you again soon!")


def scores():
	global human_score,comp_score
	print(" ")
	print("***********")
	print("HIGH SCORES")
	print("Player:", human_score)
	print("Computer:", comp_score)
	print("***********")

if __name__=='__main__':
	start()
