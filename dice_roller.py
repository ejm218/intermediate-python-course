# farkle simulation using Python
import random

class player():
    self.score = 0
    def roll_dice():
        num_dice = 6
        roll_count = 1
        for i in range(0,num_dice):
            roll = random.randint(1,6)
            elif roll == 1:
                 += 100
                num_dice -= 1
                roll_count += 1
                def roll_again:
                    roll_again = input('Would you like to roll again? [Y/N] ')
                        if roll_again == 'Y' and num_dice > 0:
                            roll_dice()
                        elif roll_again == 'Y' and num_dice == 0:
                            num_dice = 6
                            roll_dice()
                        else:
                            print('Next player')
                roll_again()
            elif roll == 5:
                dice_sum += 50
                num_dice -= 1
                roll_count += 1
                roll_again()
            else:
                print('Farkle!')
                roll_count = 1
                num_dice = 6

#### setup the game
# player_count = int(input('How many people are playing? '))
player1 = player()
player2 = player()
players = [player1, player2]
# if player_count > 2:
  #  for i in range(3,player_count):
   #     player = player()
    #    players.append(player%i)

def gameplay():
    while player1.score < 10000 and player2.score < 10000:
        for i in players:
            print(f'Your score is {i.score}')
            player.roll_dice()
    if player1.score >= 10000:
        print(f'Player 1 wins with {player1.score} points!')
    elif player2.score >= 10000:
        print(f'Player 2 wins with {player2.score} points!')
    
        
        
