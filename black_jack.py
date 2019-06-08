#This program is similar to the Blackjack card game, where the sum of the user's cards shouldn't go beyond 21.

#For my program's functions, I first import Python's math and random libraries 
import math
import random

#This fruitful function takes 2 variables for its parameters, which are both random ints in the range
#of 1 through 13  
def sum_of_cards(user_card_1, user_card_2):
	user_card_1 = random.randint(1,13)
	user_card_2 = random.randint(1,13)
	#prints both cards that the user was dealt
	print('Here are the cards you were dealt:', user_card_1, 'and', user_card_2)	 	
	result = user_card_1 + user_card_2	
	return result

#This defines the main function
def main():
	user_card_1 = random.randint(1,13)
	user_card_2 = random.randint(1,13)
	#Call to my fruitful function, sum_of_cards, whose value is then 
	#assigned to the variable total
	total = sum_of_cards(user_card_1, user_card_2)
	print('Here is the total sum: ', total) 
	#This if statement checks to see whether or not the sum of the 
	#player's cards is less than or equal to 21
	if total > 0 and total <= 21:
		print('You won!!')
	#If not, the player has lost the game
	else:
		print('You lost. Try again :(')	


    
#Here is the call to my main function
main()