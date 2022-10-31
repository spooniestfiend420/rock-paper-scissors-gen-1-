import random
valid_plays = ['rock', 'paper', 'scissors']
insults = ['learn to spell then you can try again', 'that is not an option you fool', 'the game is called rock, paper, scissors. maybe try picking one of those next time', 'this is a kids game, smarten up']
win_dict = {'rock': 0, 'paper': 1, 'scissors': 2}
los_dict = {'scissors': 0, 'rock': 1, 'paper': 2}
player_score = 0
pc_score = 0

while player_score < 2 and pc_score < 2:
    
    player_choice = input('do you choose rock, paper or scissors? ')
    if player_choice not in valid_plays:
        print(f'really? {player_choice}? really? {random.choice(insults)}')
        break
    else:
        pass
    pc_choice = random.choice(valid_plays)
    print(f'you chose {player_choice}. the pc chose {pc_choice}')
    
    for c, v in win_dict.items():
        if c == player_choice:
            player_number = v
          
    for c, v in los_dict.items():
        if c == pc_choice:
            pc_number = v
            
    
    if player_choice == pc_choice:
        print('it is a tie')
        pass
    elif player_number == pc_number:
        print('you won the hand')
        player_score += 1
    else:
        print('you lost the hand')
        pc_score += 1
        
print(f'player score equals {player_score} and pc score equals {pc_score}')
    