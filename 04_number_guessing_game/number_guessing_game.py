"""
Number Guessing Game Project
Author: Faranak Moayeri

Description:
A console-based number guessing game with difficulty levels,
input validation, score tracking, and replay option.
"""

import random
import time

PENALTY = 50

# Track high scores in memory during the game session
high_scores = {"easy": 0, "medium": 0, "hard": 0}


def choose_difficulty():
    """Prompt the user to select a difficulty level and return settings."""
    while True:
        difficulty = input(
            "Choose difficulty (Easy / Medium / Hard): ").strip().lower()

        if difficulty == "easy":
            return 10, 100, difficulty
        elif difficulty == "medium":
            return 7, 200, difficulty
        elif difficulty == "hard":
            return 5, 300, difficulty
        else:
            print("Invalid choice! Please choose Easy, Medium, or Hard.")


def get_valid_guess(prompt):
    """Prompt the user for a number between 1 and 100 with validation."""
    while True:
        try:
            guess = int(input(prompt))
            if 1 <= guess <= 100:
                return guess
            print("Out of range! Please enter a number from 1 to 100.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


def play_game():
    """Handle a single round of the game."""
    max_attempts, base_score, difficulty = choose_difficulty()

    score = base_score
    attempts = 0
    won = False
    secret_number = random.randint(1, 100)

    start_time = time.perf_counter()

    print(f"\nYou selected {difficulty.title()} mode.")
    print(f"You have {max_attempts} attempts to guess the number.")

    while attempts < max_attempts:
        if attempts == 0:
            prompt = "Enter your guess (1-100): "
        else:
            prompt = "Enter next guess: "

        user_guess = get_valid_guess(prompt)
        attempts += 1

        if user_guess == secret_number:
            print("\nCongratulations! You found the correct number!")
            won = True
            break
        elif user_guess > secret_number:
            print("Too high!")
        else:
            print("Too low!")

        score = max(0, score - PENALTY)
        remaining = max_attempts - attempts

        if remaining > 0:
            print(f"Attempts left: {remaining}")

    if not won:
        print(f"\nGame over! The correct number was {secret_number}.")

    duration = time.perf_counter() - start_time

    # Display game summary
    print("\n---------- Round Summary ----------")
    print(f"Difficulty: {difficulty.title()}")
    print(f"Attempts used: {attempts}")
    print(f"Final score: {score}")
    print(f"Time taken: {duration:.2f} seconds")

    # Update session high score if the player won
    previous_best = high_scores[difficulty]
    if won and score > previous_best:
        high_scores[difficulty] = score
        print("New high score for this level! Great job!")
    else:
        print(f"Current best score for {difficulty.title()}: {previous_best}")


def ask_to_play_again():
    """Ask the player if they want to start a new round."""
    while True:
        choice = input(
            "\nDo you want to play again? (yes/no): ").strip().lower()
        if choice in ("yes", "y"):
            return True
        elif choice in ("no", "n"):
            return False
        else:
            print("Invalid input! Please type 'yes' or 'no'.")


def main():
    """Main program entry point."""
    print("Welcome to the Number Guessing Game!")

    while True:
        play_game()
        if not ask_to_play_again():
            print("\nThank you for playing! Goodbye!")
            break
        print("\nStarting a new round...\n")


if __name__ == "__main__":
    main()
