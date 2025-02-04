import random
player_score=0
computer_score=0
game_on=True

#User Batting

while game_on:
    player= int(input("Enter a number from 1 to 5: "))
    computer=random.randint(1,6)
    if player==computer:
        print(f"Game Over")
        game_on=False
    elif player>5:
        print("Enter below 6")
    else:
        player_score+=player

print(f"The score is {player_score}")
computer_game_on=True

#Computer Batting

while computer_game_on:
    player= int(input("Enter a number from 1 to 5: "))
    computer=random.randint(1,6)
    if player==computer:
        print(f"Game Over")
        computer_game_on=False
    elif player>5:
        print("Enter below 6")
    else:
        computer_score+=player
        if computer_score>player_score:
            computer_game_on=False


#Result

if player_score > computer_score:
    print("You win")
elif player_score == computer_score:
    print("draw")
else:
    print("You Loose")
print(f"The score is {computer_score}")

