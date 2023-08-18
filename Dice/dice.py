'''
   This is a simple dice program where you choose 2-5 players. 
   When you choose to roll you can continue until you roll a 1 then your
   roll stops and score is added to the running total.  When a player reaches 
   a score of 50 then the game stops.
'''
import random
import time
import colorama
colorama.init()


def roll():
    minValue = 1
    maxValue = 6
    diceValue = random.randint(minValue, maxValue)
    return diceValue


while True:
    players = input("Enter the number of players between 2-5: ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 5:
            break
        else:
            print("Please enter in a value between 2-5.")
    else:
        print("Invalid please enter in a numeric value")


maxScore = 50
playerScore = [0 for _ in range(players)]

while max(playerScore) < maxScore:
    for player_idx in range(players):
        currentScore = 0
        print(
            f"Player {player_idx + 1} your current score is {playerScore[player_idx]} ")
        while True:
            rolling = input(
                f"Do you want to roll player {player_idx + 1} (y) ")
            if rolling.lower() == "n":
                break
            dice = roll()
            if dice == 1:
                print("You rolled a 1!  Turn over")
                print(f"Player {player_idx +1} your current score is {playerScore[player_idx]}")
                time.sleep(5)
                break
            else:
                print("You rolled a ", dice)
                currentScore += dice
                print("Your current roll score is ", currentScore)
                playerScore[player_idx] += dice
                print(f"Your overall total is {playerScore[player_idx]}")
                if playerScore[player_idx] > maxScore:
                    break
        print("\033[2J\033[1;1f")
highest_score = max(playerScore)        
winningIdx = playerScore.index(highest_score)

print(f"The winner is Player {winningIdx + 1} with a score of {highest_score}" )
