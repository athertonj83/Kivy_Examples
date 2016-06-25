#!/usr/bin/env python2

#this creates rock, paper, scissors from the Python book

import random
import time

rock=1
paper=2
scissors=3

#Dictionary of keys
names={rock:"Rock", paper:"Paper",scissors:"Scissors"}

#Which type wins over which others
rules={rock:scissors, paper:rock, scissors:paper}

#Starting conditions, vars keep ongoing score
human_score=0
comp_score=0


def start():
	print "Now let's play Rock, Paper, Scissors!"
	while game():
		pass
	scores()

#Referencing the modules used in the game, determining whether another game will be played
def game():
	player=move()
	computer=random.randint(1,3)
	result(player,computer)
	return play_again()

def move():	
	while True:
		print 
		player=raw_input("Rock=1\nPaper=2\nScissors=3\nMake a move!:")
		try:
			player=int(player)
			if player in (1,2,3):
				return player
		except ValueError:
			pass
		print "Eh? I didn't get that. I need you to enter 1, 2, or 3"

# This prints the results of the game (i.e. who won)
def result(player,computer):
	print "3..."
	time.sleep(1)
	print "2..."
	time.sleep(1)
	print "1!"
	time.sleep(0.5)
	print "Computer threw {0}".format(names[computer])
	
	global human_score,comp_score
	if player==computer:
		print "The game is tied!"
		human_score+=1
		comp_score+=1
	else:
		if rules[player]==computer:
			print "Congratulations! You've won a random game!"
			human_score+=1
		else:
			print "Shame. You lost."
			comp_score+=1
			
def play_again():
	answer=raw_input("Another game? Y/N?")
	if answer.upper() in ("Y","YES"):
		return answer
	else:
		print "No more games? Ok... See you again soon!"
		

def scores():
	global human_score,comp_score
	print "HIGH SCORES"
	print "Player: ", human_score
	print "Computer: ", comp_score
	
if __name__=='__main__':
	start()
		
		
		
		
		







