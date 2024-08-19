import random
import math

us = 0
cs = 0

print("*********WELCOME TO SNAKE GUN WATER*********")
print("Some instructions to play:\n 1 for Snake\n 2 for Water\n 3 for Gun\n 4 to exit")

ccl = ['gun', 'water', 'snake']

x = input('Are you ready to play: yes or no?___ ')
res = x.lower()

while res == 'no':
	x = input('Are you ready to play: yes or no?___ ')
	res = x.lower()

else:
	while True:
		uc = int(input('Enter your Choice: '))
		if uc == 4:
			break
		
		cc = math.floor((random.random() * 3))
		computer_choice = ccl[cc]
		
		if computer_choice == ccl[uc - 1]:
			print("Draw")
		elif uc == 1 and computer_choice == 'gun':
			print("My Point")
			cs += 1
		elif uc == 1 and computer_choice == 'water':
			print("Your Point")
			us += 1
		elif uc == 2 and computer_choice == 'gun':
			print("Your point")
			us += 1
		elif uc == 2 and computer_choice == 'snake':
			print("My point")
			cs += 1
		elif uc == 3 and computer_choice == 'water':
			print("My point")
			cs += 1
		elif uc == 3 and computer_choice == 'snake':
			print("Your point")
			us += 1
		else:
			print("******INVALID INPUT******")
		
		print(f"My score: {cs}")
		print(f"Player score: {us}")

print(f"THE FINAL SCORES ARE:\nPLAYER: {us}\nMY SCORE: {cs}")

		
		
		
		
	
		
		
		
		
		
	
		
		
		
		
		
		
		
		
		
	
	
	