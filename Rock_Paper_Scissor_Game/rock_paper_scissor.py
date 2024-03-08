import random

while True:
    user_wins = 0
    computer_wins = 0
    options = {'r': 'rock', 'p': 'paper', 's': 'scissors'}

    print("\nWelcome to Rock, Paper, Scissors Game!!!")

    while True:
        print("\nType 'R' for Rock, 'P' for Paper, 'S' for Scissors, or 'Q' to Quit")
        user_input = input("Enter your choice: ").lower()
        if user_input == 'q':
            break

        if user_input not in options:
            print("Invalid input. Please try again.")
            continue

        computer_pick = random.choice(list(options.keys()))
        print("You Chose:", options[user_input])
        print("Computer Chose:", options[computer_pick])

        if user_input == computer_pick:
            print("It's a tie!")

        elif user_input == "r" and computer_pick == 's':
            print("You won!")
            user_wins += 1

        elif user_input == "p" and computer_pick == "r":
            print("You won!")
            user_wins += 1

        elif user_input == "s" and computer_pick == "p":
            print("You won!")
            user_wins += 1

        else:
            print("Computer wins! You Lost!")
            computer_wins += 1

    print("\nYou won", user_wins, "times.")
    print("The computer won", computer_wins, "times.")

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        break

print("Thanks for Playing!")
