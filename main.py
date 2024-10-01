# Programmer: Megan
# Course: Cs151, Professor Zee
# Due Date: 9/25/2024
# PA Assignment: 01
# Problem statement: Create a text adventure game! In this /
# game, the user gives input that affects the path of the story. /
# You must create a game that meets the requirements in the specification below.

# Data In: Code needs input the players name, the players level of soccer skills, /
# the distance a player can score from, how tired the player is.

# Data Out: What will be the result of the soccer match? A win, tie or loss.

# Purpose: This code outlines the decision-making process in the soccer /
# game code and the structure of the game flow based on the user's input.

def start_game():
    # Introduction and name input
    print("Welcome to the Soccer game!")
    player_name = input("What is your name, field player? ")
    print(f"Hello, {player_name}! Your game begins now.")

    # First decision based on integer input
    skilled = int(input("On a scale from 1 to 10, how skilled are you? "))
    if skilled >= 5:
        print("You are skilled enough to play a soccer game!")
        enter_soccer_game(player_name)
    else:
        print("You decide it's safer to stay on the bench. The game ends here.")
        end_game()


def enter_soccer_game(player_name):
    # Second decision based on float input
    scoring_distance = float(input("You reach a scoring opportunity. How far can you "
                                   "shoot a ball? (Enter a number in meters): "))
    if scoring_distance > 1.5:
        print("The goal is not too far. You can score easily. Now you are up 1-0!!")
    else:
        print("The goal is too far. You decide to pass the ball instead.")

    # Third decision based on string input
    subbed = input("Oh no you are getting tired. Do you want to be subbed off?").lower()
    if subbed == "no":
        print(f"{player_name}, you finish playing the game! You win!")
    elif subbed == "yes":
        print(f"{player_name}, you get subbed off and the other team scores a minute  "
              f"later. The game ends in a tie")
    else:
        print("You were too tired. The other team scored twice. You lost the game 1-2.")
        end_game()


def end_game():
    print("Game Over. Thanks for playing!")


# Start the game
start_game()
