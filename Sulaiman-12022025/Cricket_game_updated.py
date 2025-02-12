import random

def play_turn(target_score=None):
    score = 0
    while True:

        player = int(input("Enter a number (1-5): "))
        computer = random.randint(1, 5)
        print(f"Player: {player}, Computer: {computer}")

        if player == computer:
            print("Game Over")
            return score
        elif player > 5:
            print("Enter a valid number!")
        else:
            score += player if target_score is None else computer
            print(f"Score: {score}")
            if target_score and score > target_score:
                return score

player_score = play_turn()
print(f"Player Score: {player_score}")

computer_score = play_turn(player_score)
print(f"Computer Score: {computer_score}")


if player_score > computer_score:
    print(f"You won by {player_score-computer_score} runs.")
elif player_score == computer_score:
    print("It's a Draw!")
else:
    print(f"You Lose by {computer_score-player_score} runs.")


