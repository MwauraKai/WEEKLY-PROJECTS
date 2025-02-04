import random
import time

def print_rules():
    """
    Prints the welcome message and game rules.
    """
    print("\nWelcome to Snakes and Ladders!")
    print("Rules:")
    print("1. You and the Computer both start at position 0.")
    print("2. On your turn, press Enter to roll a dice (1 to 6).")
    print("3. The Computer will roll automatically on its turn.")
    print("4. Move forward the number of spaces shown on the dice.")
    print("5. If you land at the bottom of a ladder, you'll climb up to a higher position.")
    print("6. If you land on the head of a snake, you'll slide down to a lower position.")
    print("7. The first to reach exactly 100 wins.\n")

# Define snakes and ladders as dictionaries.
# For snakes: key is the snake's head (where you land) and value is where you slide down.
snakes = {
    97: 78,
    95: 56,
    88: 24,
    62: 18,
    36: 6
}

# For ladders: key is the ladder's bottom (where you land) and value is where you climb up.
ladders = {
    2: 38,
    7: 14,
    8: 31,
    15: 26,
    28: 84,
    21: 42,
    51: 67,
    78: 98,
    71: 91
}

def roll_dice():
    """
    Simulates rolling a dice by returning a random integer between 1 and 6.
    """
    return random.randint(1, 6)

def play_game(player_name):
    """
    Runs a single instance of the game.
    - Initializes player positions.
    - Alternates turns between the user (with their given name) and the computer.
    - Prompts the user to roll the dice and shows interactive messages for each move.
    - The computer takes its turn automatically.
    - Checks for snakes, ladders, and win conditions.
    """
    # Create a list with the user's name and "Computer"
    players = [player_name, "Computer"]
    # Initialize positions for both players at 0.
    positions = {player: 0 for player in players}
    turn = 0

    # Print the game rules before starting.
    print_rules()
    input("Press Enter to start the game...")  # Ensure the game starts when the user is ready.

    # Game loop continues until a player wins.
    while True:
        # Determine whose turn it is.
        current_player = players[turn % len(players)]
        
        if current_player == player_name:
            # Human player's turn: wait for input.
            input(f"{current_player}, press Enter to roll the dice...")
        else:
            # Computer's turn: simulate a brief pause.
            print("Computer's turn... Rolling the dice...")
            time.sleep(1)  # Wait 1 second for realism

        dice = roll_dice()  # Roll the dice.
        print(f"{current_player} rolled a {dice}.")

        old_position = positions[current_player]
        new_position = old_position + dice

        # If the move would exceed 100, it doesn't count.
        if new_position > 100:
            print(f"{current_player} needs to roll exactly {100 - old_position} to win. Remains at {old_position}.")
        else:
            positions[current_player] = new_position  # Update the player's position.
            print(f"{current_player} moves from {old_position} to {new_position}.")

            # Check for a ladder at the new position.
            if new_position in ladders:
                final_pos = ladders[new_position]
                print(f"Great! {current_player} found a ladder and climbs from {new_position} to {final_pos}.")
                positions[current_player] = final_pos
            # Check for a snake at the new position.
            elif new_position in snakes:
                final_pos = snakes[new_position]
                print(f"Oh no! {current_player} got bitten by a snake and slides down from {new_position} to {final_pos}.")
                positions[current_player] = final_pos

        # Check if the current player has won by reaching exactly 100.
        if positions[current_player] == 100:
            # Identify the loser.
            loser = players[(turn + 1) % len(players)]
            print(f"\nCongratulations {current_player}! You have won the game!")
            print(f"Better luck next time, {loser}!")
            break  # End the game loop if a win is detected.

        print()  # Blank line for readability.
        turn += 1  # Next player's turn.

def main():
    # Ask the user for their name once.
    player_name = input("Enter your name: ").strip() or "Player"
    
    while True:
        play_game(player_name)
        # Input validation loop for replay prompt.
        while True:
            again = input("Do you want to play again? (yes/no): ").strip().lower()
            if again in ("yes", "no"):
                break
            else:
                print("Please enter 'yes' or 'no'.")
        
        if again == "yes":
            continue
        else:
            print("Thanks for playing! Goodbye! See you again next time!")
            break

if __name__ == '__main__':
    main()
