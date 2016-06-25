#!/usr/bin/env python2

#this creates hangman - copied from the python book

from random import *
import collections

player_score=0
computer_score=0

def hangedman_mod(hangman):
        graphic=["1st go","2nd go","3rd go","4th go","5th go","6th go","you lost!"]

graphic=[
        """
          +---------+
          |
          |
          |
          |
          |
        ===============
        """,
        """
          +---------+
          |         |
          |         O
          |
          |
          |
        ===============
        """,
        """
          +---------+
          |         |
          |         O
          |         |
          |
          |
        ===============
        """,
        """
          +---------+
          |         |
          |         O
          |        -|
          |
          |
        ===============
        """,
        """
          +---------+
          |         |
          |         O
          |        -|-
          |
          |
        ===============
        """,        
        """
          +---------+
          |         |
          |         O
          |        -|-
          |        /
          |
        ===============
        """,
        """
          +---------+
          |         |
          |         O
          |        -|-
          |        //
          |
        ===============
        """]

def start():
        print "Let's play a game of Linux Hangman!"
        while game():
                pass
        scores()



def game():
        dictionary=["boston","aerosmith","stereophonics","blur","metallica","gorillaz","carpenters"]
        word=choice(dictionary) #choice is a function from the random module
        word_length=len(word)
        clue=list(word_length*"_") #this creates a line of underscores the length of the word - a list since strings are IMMUTABLE!!
        letter=""

        tries=6 # number of tries the human gets
        letters_tried=""
        letters_wrong=0

        global computer_score, player_score

        while (letters_wrong!=tries) and ("".join(clue)!=word):
                letter=guess_letter()
                
                if len(letter)==1 and letter.isalpha(): #if the letter guessed is 1 character and alphabetical
                        letter=letter.strip()
                        letter=letter.lower()

                        # if already picked, print message. Otherwise add to letters tried list and see if in the word
                        if letters_tried.find(letter)!=-1:
                                print "You've already picked",letter
                        else:
                                letters_tried=letters_tried+letter
                                first_index=word.find(letter)
                                
                                # How many underscores remaining?
                                cnt=collections.Counter()
                                for wrd in clue:
                                    cnt[wrd]+=1
                                
                                # if letter is wrong
                                if first_index==-1:
                                     letters_wrong+=1
                                     print "Sorry,",letter,"isn't what we're looking for."
                                     print "Letter Guesses: ", letters_tried
                                     print "Number of Guesses Remaining:", tries-letters_wrong
                                     print " ".join(clue)
                                     print (graphic[letters_wrong])


                                #if letter is right    
                                elif first_index>=0:
                                    for i in range(word_length):
                                        if letter==word[i]:
                                            clue[i]=letter
                                    cnt=collections.Counter()
                                    for wrd in clue:
                                        cnt[wrd]+=1

                                    #if some letters left to get
                                    if cnt["_"]>1:
                                        print "Congratulations,",letter,"is correct!"
                                        print "Letter Guesses: ", letters_tried
                                        print "Number of Guesses Remaining:", tries-letters_wrong
                                        print " ".join(clue)                                    

                                    # 1 letter remaining to guess
                                    if cnt["_"]==1:
                                        print "Congratulations,",letter,"is correct!"
                                        print "Letter Guesses: ", letters_tried
                                        print "Number of Guesses Remaining:", tries-letters_wrong
                                        print "Only 1 letter remains!"
                                        print " ".join(clue)

                                    # none left to get!
                                    if cnt["_"]==0:
                                        print "Congratulations, You Win!"
                                        print " ".join(clue)
                                        player_score+=1
                                        break
                                                       
                else:
                        print "Please choose a single letter!"
                        
                if letters_wrong==tries:
                        print "Game Over"
                        print "The word was", word
                        computer_score+=1
                        break
             
        return play_again()

def guess_letter():
        print # creating an empty line
        letter=raw_input("Take a guess at a letter in our mystery word:")
        print
        return letter

def play_again():
        answer=raw_input("Would you like to play again? y/n?")
        if answer in ("y","Y","yes","YES","Yes"):
                return answer
        else:
                print "Thank you for playing. See you next time!"

def scores():
        global player_score,computer_score
        print "HIGH SCORES"
        print "Player: ",player_score
        print "Computer: ",computer_score

if __name__=='__main__':
        start()

























                

















        
                                                
                                        
        




















































        
