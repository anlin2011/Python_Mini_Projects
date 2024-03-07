import random
import time

def generate_random_number():
    return random.randint(1, 100)

def get_user_guess():
    while True:
        try:
            guess = int(input("Take a guess (between 1 and 100): "))
            if(guess>=1 and guess<=100):
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Please enter a valid number.")

def play_game():
    random_number = generate_random_number()
    attempts = 0

    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")

    while True:
        user_guess = get_user_guess()
        attempts += 1

        if user_guess < random_number:
            print("Too low! Try again.")
        elif user_guess > random_number:
            print("Too high! Try again.")
        else:
            print("\nCongratulations! You guessed the number {} correctly in {} attempts.".format(random_number, attempts))
            break

def main():
    print("Initializing game...")
    time.sleep(1)  

    while True:
        play_game()
        print("\nGame over.")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()


