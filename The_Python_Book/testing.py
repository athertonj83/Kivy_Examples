#!/usr/bin/env python2

#this creates hangman - copied from the python book

from random import *
import collections

player_score=0
computer_score=0

test_list=["j","_","v"]

cnt=collections.Counter()

for word in test_list:
        cnt[word]+=1

print cnt
print cnt["_"]
        




        
#def start():
 #       letters_wrong=1
  #      
   #     print letters_wrong                
    #    print(graphic[letters_wrong])

#if __name__=='__main__':
 #       start()

        



        
