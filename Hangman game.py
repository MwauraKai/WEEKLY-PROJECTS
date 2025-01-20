import random
import turtle

# List of words for the hangman game
hangman_words_easy = ["cat", "dog", "apple", "bird", "fish"]
hangman_words_medium = ["python", "java", "hangman", "computer", "soccer"]
hangman_words_hard = ["transcript", "programming", "algorithm", "cryptography", "multiverse"]

# Initialize turtle screen
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.title("Hangman Game - Turtle Visualization")

# Create turtle for drawing
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(3)

# Function to choose word based on difficulty
def choose_word(difficulty):
    if difficulty == "easy":
        return random.choice(hangman_words_easy)
    elif difficulty == "medium":
        return random.choice(hangman_words_medium)
    elif difficulty == "hard":
        return random.choice(hangman_words_hard)

# Function to draw gallows
def draw_gallows():
    pen.penup()
    pen.goto(-200, -100)
    pen.pendown()
    pen.setheading(0)
    pen.forward(100)  # Base
    pen.left(90)
    pen.forward(200)  # Pole
    pen.left(90)
    pen.forward(50)   # Top horizontal line
    pen.left(90)
    pen.forward(20)   # Short vertical line for the rope

# Function to draw the head of the hangman
def draw_head():
    pen.penup()
    pen.goto(-100, 40)
    pen.pendown()
    pen.circle(20)

# Function to draw the body of the hangman
def draw_body():
    pen.penup()
    pen.goto(-100, 40)
    pen.pendown()
    pen.setheading(270)  # Facing down
    pen.forward(60)

# Function to draw left arm
def draw_left_arm():
    pen.penup()
    pen.goto(-100, 20)
    pen.pendown()
    pen.setheading(180)  # Left arm
    pen.forward(40)

# Function to draw right arm
def draw_right_arm():
    pen.penup()
    pen.goto(-100, 20)
    pen.pendown()
    pen.setheading(0)  # Right arm
    pen.forward(40)

# Function to draw left leg
def draw_left_leg():
    pen.penup()
    pen.goto(-100, -20)
    pen.pendown()
    pen.setheading(225)  # Left leg
    pen.forward(40)

# Function to draw right leg
def draw_right_leg():
    pen.penup()
    pen.goto(-100, -20)
    pen.pendown()
    pen.setheading(45)  # Right leg
    pen.forward(40)

# Function to handle the game
def play_game():
    # Choose difficulty level and word
    difficulty = choose_difficulty()
    print(f"You chose {difficulty} level")
    word = choose_word(difficulty)
    guessed_word = ['_'] * len(word)
    guesses = set()
    attempts = 6  # Fixed number of attempts for all difficulties
    hint_used = False  # To track if the hint has been used

    # Draw gallows
    draw_gallows()

    while attempts > 0:
        display_word(guessed_word)

        if not hint_used:  # Allow the player to use the hint once
            hint_choice = input("Would you like a hint? (yes/no): ").lower()
            if hint_choice == 'yes':
                hint_letter = get_hint(word, guessed_word)
                guessed_word[word.index(hint_letter)] = hint_letter
                guesses.add(hint_letter)
                hint_used = True
                # Print the word with the hint letter inserted
                display_word(guessed_word)
                print(f"Now, try guessing another letter!")
            elif hint_choice == 'no':
                pass  # Do nothing if the user says no
            else:
                print("Invalid input! Please enter yes or no.")
                continue

        guess = get_guess(guesses)
        guesses.add(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
            if "_" not in guessed_word:
                display_word(guessed_word)
                print("Congratulations! You won!")
                break
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

            # Drawing hangman parts based on incorrect guesses
            if attempts == 5:
                draw_head()
            elif attempts == 4:
                draw_body()
            elif attempts == 3:
                draw_left_arm()
            elif attempts == 2:
                draw_right_arm()
            elif attempts == 1:
                draw_left_leg()
            elif attempts == 0:
                draw_right_leg()
                print(f"You lost! The word was: {word}")
                break

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == 'y':
        play_game()
    elif play_again == 'n':
        print("Thanks for playing!")
    else:
        print("Invalid input! Please enter 'y' or 'n'.")
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == 'y':
            play_game()
        elif play_again == 'n':
            print("Thanks for playing!")

# Function to display the current word
def display_word(guessed_word):
    print("Current word is: " + " ".join(guessed_word))

# Function to get the player's guess
def get_guess(guesses):
    while True:
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1:
            print("Please enter only one letter.")
        elif guess in guesses:
            print("You've already guessed that letter.")
        elif not guess.isalpha():
            print("Please enter a valid letter.")
        else:
            return guess

# Function to provide a hint
def get_hint(word, guessed_word):
    hint_letter = random.choice([letter for letter in word if letter not in guessed_word])
    print(f"Hint: One of the letters in the word is '{hint_letter}'.")
    return hint_letter

# Function to choose difficulty level
def choose_difficulty():
    print("Choose a difficulty level:")
    print("1. Easy\n2. Medium\n3. Hard")
    while True:
        choice = input("Enter 1, 2, or 3: ")
        if choice == "1":
            return "easy"
        elif choice == "2":
            return "medium"
        elif choice == "3":
            return "hard"
        else:
            print("Invalid input. Please choose 1, 2, or 3.")

# Start the game
print("Hello and welcome to the Hangman game! There are three exciting levels to choose from. You'll only be allowed to use a hint once, so make it count! Each difficulty level has a limited number of attempts, so think carefully with every guess. Good luck, and enjoy the challenge!")
play_game()
turtle.done()  # Keeps the Turtle window open after the game ends
