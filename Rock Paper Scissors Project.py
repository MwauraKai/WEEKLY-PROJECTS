import random

# Randomly selecting rock, paper, or scissors for the computer.
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Determine the winner of a single round based on the rules.
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    while True:  # Outer loop ensures the user keeps being asked to play again or not
        # Ask the user to select the number of rounds (3 or 5)
        while True:
            try:
                rounds = int(input("Choose the number of rounds (3 or 5): "))
                if rounds in [3, 5]:
                    break
                else:
                    print("Please enter either 3 or 5.")
            except ValueError:
                print("Invalid input! Please enter a number (3 or 5).")

        # Variables used to track the scores for both the user and the computer.
        user_points = 0
        computer_points = 0
        round_number = 1

        print("\nWelcome to Rock-Paper-Scissors!")
        print(f"First to win {(rounds // 2) + 1} out of {rounds} rounds wins the game.\n")

        while round_number <= rounds:
            print(f"Round {round_number}")
            computer_choice = get_computer_choice()
            user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

            # Validate user input
            if user_choice not in ["rock", "paper", "scissors"]:
                print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.\n")
                continue

            print(f"Computer chose: {computer_choice}")
            result = determine_winner(user_choice, computer_choice)

            if result == "tie":
                print("It's a tie! No points awarded.\n")
            elif result == "user":
                print("You win this round!\n")
                user_points += 1
            else:
                print("Computer wins this round!\n")
                computer_points += 1

            # Check if there's a clear winner
            if user_points == (rounds // 2) + 1:
                print("Congratulations! You won the game!\n")
                break
            elif computer_points == (rounds // 2) + 1:
                print("The computer won the game. Better luck next time!\n")
                break

            round_number += 1

        # Final score if no early winner
        if user_points == computer_points:
            print("The game is a tie!")
        elif user_points > computer_points:
            print("You are the overall winner!")
        else:
            print("The computer is the overall winner!")

        print(f"Final Score - You: {user_points}, Computer: {computer_points}\n")

        # Ask if the user wants to play again
        while True:  # Loop until a valid response is given
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again in ["yes", "no"]:
                break  # Valid response, exit loop
            else:
                print("Invalid input! Please type 'yes' or 'no'.")

        if play_again == "no":
            print("Thanks for playing! Goodbye!")
            break

# Start the game
play_game()
