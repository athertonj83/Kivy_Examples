#!/usr/bin/env python3

#this creates fizz buzz woof

# Dictionary of associations
assoc={3:"Fizz", 5:"Buzz", 7:"Woof"}

for i in range(20):
	word=""
	if i%3==0:
		word="Fizz"
	if i%5==0:
		word=word+"Buzz"
	if i%7==0:
		word=word+"Woof"
	if word=="":
		word=str(i)
	print(word)
