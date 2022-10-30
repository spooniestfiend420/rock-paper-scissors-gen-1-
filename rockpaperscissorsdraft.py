# rock paper scissors
import random

valid_plays = ['rock', 'paper', 'scissors']
player_score = 0
pc_score = 0

while player_score < 2 and pc_score < 2:
	
	player_choice = input("Do you choose: rock, paper, or scissors? ")
	pc_choice = random.choice(valid_plays)
	print(f'you chose {player_choice} the pc chose {pc_choice}')
	
	if player_choice == pc_choice:
		pass
		
	elif player_choice == 'rock' and pc_choice == 'scissors' or player_choice == 'paper' and pc_choice == 'rock' or player_choice == 'scissors' and pc_choice == 'paper':
		player_score += 1
		
	else:
		pc_score += 1

print(f'player score equals {player_score} and pc score equals {pc_score}')


  