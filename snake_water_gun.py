import random

game_matrix = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
options = ["s", "w", "g"]
option_names = ["snake", "water", "gun"]

rounds = int(input("Enter number of rounds: "))
player_score = 0
computer_score = 0

for _ in range(rounds):
    print("Options:")
    print("s - Snake")
    print("w - Water")
    print("g - Gun")

    user_input = input("Enter your choice: ").lower()
    bot_input = random.choice(options)

    if user_input not in options:
        print("Invalid input. Please choose s, w, or g.")
        continue

    user_choice = options.index(user_input)
    bot_choice = options.index(bot_input)

    print(f"You chose: {option_names[user_choice]}")
    print(f"Bot chose: {option_names[bot_choice]}")

    if game_matrix[user_choice][bot_choice] == 0:
        print("It's a draw!")
    elif game_matrix[user_choice][bot_choice] == 1:
        print("You win!")
        player_score += 1
    else:
        print("You lose!")
        computer_score += 1

print("Game Over")
print(f"Your score: {player_score}")
print(f"Bot score: {computer_score}")
if player_score > computer_score:
    print("Congratulations! You win the game.")
elif player_score < computer_score:
    print("Oops! Bot wins the game.")
else:
    print("It's a tie!")
