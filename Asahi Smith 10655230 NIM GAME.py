##  ASAHI SMITH
##  10655230
##  Nim game programming assignment 

"""
*	Functions need to include the parameters outlined in the assignment brief. Functions should not be referring to global variables.

*	Having extra functions is fine so long as they add some readability or functionality. 
*	Have another look at your created functions and see if they are achieving this.

*	Extra commenting for the more complicated parts of the code is needed.

*	The checks for the users valid row and sticks choices are quite complex. 

Think about how this could be made simpler, you should have a (list with how many sticks are in each row )???
this will help you to check for valid numbers.

*	Your sticks should be printing out similar to the screenshot in the brief.
"""

#Define variables and list
import random
import time
from random import randrange
current_player = ""
cpu = "CPU"
row = 0
stick_quantity = 0
stick_list = [1, 3, 5, 7]
won = 0
lost = 0
play = True


#Print to user what move was made and by whom
def print_move(stick_quantity, current_player, row):
	if stick_quantity > 1:
		#If there are multiple stick_list taken, use word 'stick_list'
		print(current_player, "takes", stick_quantity, "sticks from row", row)
	elif stick_quantity == 1:
		#If there is just one stick taken, use word 'stick'
		print(current_player, "takes", stick_quantity, "stick from row", row)
	time.sleep(0.5)

def display_board():
	print("-----------------------------")
	for i in range(0, 4):
		b = (f"Row {i + 1}:")
		a = (f" {'|' * stick_list[i]}")
		print(b , a.center(20))
	print("-----------------------------")
	time.sleep(0.5)


#Get user input and play game
while play:
	#Welcome user and randomly choose starting player
	print("Welcome to NIM!")
	user = str(input("Please enter your name to begin: "))
	user = user.capitalize()
	current_player = random.choice([user, cpu])
	time.sleep(0.5)
	
	print("Game is starting,", current_player, "will be going first!")
	time.sleep(0.5)

	print("The current board is:" )
	time.sleep(0.5)

	#Display the current board by printing the list
	display_board()

	#This loop will run so long as there is at least 1 stick left on the board, asking the current player to make a move
	while sum(stick_list) > 0:
		#If it's users turn, ask to take stick_list. Set current player to CPU after
		if current_player == user:
			while True:
				try:
					row = int(input("What row would you like to take sticks from? "))
					stick_quantity = int(input("How many sticks would you like to take from this row? "))
					#Checks if user input is greater than 0 and less than the maximum number possible (out of range)
					if (stick_list[row-1] >= stick_quantity > 0) and (len(stick_list) >= row > 0):
						break

				except:
					ValueError
					print("Invalid input. Please try again")
					continue
			
			#Remove stick_list from chosen row
			stick_list[row - 1] = stick_list[row - 1] - stick_quantity
			time.sleep(0.5)

			print_move(stick_quantity, current_player, row)

			display_board()

			current_player = cpu

		#CPU makes random turn, sets current player to user after
		elif current_player == cpu:
			#CPU will randomly generate a number for row and stick quantity, if the number is out of range then it will retry
			try:
				row = (randrange(len(stick_list)) + 1)
				stick_quantity = random.randint(1, stick_list[row-1])
				#remove stick_list from chosen row
				stick_list[row - 1] = stick_list[row - 1] - stick_quantity

			except (IndexError, ValueError):
				continue
			time.sleep(1)

			print_move(stick_quantity, current_player, row)

			display_board()

			current_player = user
	time.sleep(0.5)

	#Game ending screen
	print("Game Over!")
	if current_player == user:
		print(user, "wins!")
		won = won + 1

	elif current_player == cpu:
		print("CPU wins!")
		lost = lost + 1

	time.sleep(0.5)
	
	print("You have won ", won,"time(s) and lost ",lost,"time(s)")

	#Ask the user if they wish to play again, loop again if yes, end program if no
	while True:
		restart = str.lower(input("Do you wish to play again? (Y/N) "))
		if restart == 'y':
			#Restore list back to original quantities (1,3,5,7)
			stick_list[0] = 1; stick_list[1] = 3; stick_list[2] = 5; stick_list[3] = 7
			break
		elif restart == 'n':
			print("Goodbye.")
			play = False
			break
		else:
			print("Invalid input. Please enter either a 'Y' or an 'N'")

