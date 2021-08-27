import random

choices = ["rock","paper","scissors"]
while True:
    computer = random.choice(choices)
    player = None

    while player not in choices:
        print("Choose between these 3")
        player = input("rock, paper, scissors: ").lower()

    if player == computer:
        print(f"computer:{computer}|player:{player}")
        print("equal!")

    elif player == "rock":
        if computer == "paper":
            print(f"computer:{computer}|player:{player}")
            print("You lose!")
        elif computer == "scissors":
            print(f"computer:{computer}|player:{player}")
            print("You win!")

    elif player == "scissors":
        if computer == "rock":
            print(f"computer:{computer}|player:{player}")
            print("You lose!")
        elif computer == "paper":
            print(f"computer:{computer}|player:{player}")
            print("You win!")

    elif player == "paper":
        if computer == "scissors":
            print(f"computer:{computer}|player:{player}")
            print("You lose!")
        elif computer == "rock":
            print(f"computer:{computer}|player:{player}")
            print("You win!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Thanks for playing my game!")