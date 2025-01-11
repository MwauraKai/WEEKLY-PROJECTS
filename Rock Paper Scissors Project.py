import random
#We start by Randomly selecting rock, paper, or scissors for the computer.
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)
 
#We now Determine the winner of a single round based on the rules:
    #Rock beats Scissors, Scissors beats Paper, Paper beats Rock.
    
def determine_winner(user_choice, computer_choice):
   
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_game(rounds=3):
    # variables used to track the scores for both the user and the computer.
    user_points = 0
    computer_points = 0
    round_number = 1

    print("Welcome to Rock-Paper-Scissors!")
    print("First to win 2 out of 3 (or 3 our of 5) rounds wins the game.\n")

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
# testing
        if result == "tie":
            print("It's a tie! No points awarded.\n")
        elif result == "user":
            print("You win this round!\n")
            user_points += 1
        else:
            print("Computer wins this round!\n")
            computer_points += 1

        # Check if there's a clear winner: calculates the number of points needed to win
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

    print(f"Final Score - You: {user_points}, Computer: {computer_points}")

# Play the game 
play_game(5)

# comment
