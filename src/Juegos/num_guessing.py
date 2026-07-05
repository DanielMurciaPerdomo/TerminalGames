"""
Game to guess a number
"""
import random

try:
    from .juego import Game
except ImportError:
    from juego import Game


class NumGuessing(Game):
    """"Class to guess a number with 4 digits"""

    def display_game(self):
        """Show the game to play"""
        print("Welcome to the Number Guessing Game!")
        print("I have selected a 4-digit number without repetition. Try to guess it!")
        print("0 is a number that can be used in the number")
        # Generate a random 4-digit number
        secret_number = "".join(random.sample("0123456789", 4))
        attempts = 0
        is_running = True
        while is_running:
            guess = input("Enter your guess (4 digits) or 'q' to exit: ")
            #End the game if the user wants to quit or if the score is less than or equal to 0
            if guess == 'q' or self.score <= 0:
                is_running = False
                self.score = 0
                print(f"You lost, your score is: {self.score - self.score}")
                print(f"The secret number was {secret_number} ")
                break
            #Check if the guess is valid (4 digits)
            if len(guess) != 4 or not guess.isdigit():
                print("Invalid input. Please enter a 4-digit number.")
                continue


            #Update the score based on the number of attempts
            attempts += 1
            if guess == secret_number:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                print(f"Your score is: {self.score}")
                is_running = False
                break
            else:
                #Compare the guess with the secret number and provide feedback
                right, in_the_number, wrong = self.compare_numbers(secret_number, guess)
                print(f"Your guess: {guess}")
                print(f"{right} digits in the right position")
                print(f"{in_the_number} digits in the number but in the wrong position")
                print(f"and {wrong} digits not in the number.")
                print(f"Your score is: {self.score}")
            self.score -= 1

    def compare_numbers(self, secret_number, guess):
        """Compare the secret number with the guess and return the counts of right position,
         in the number, and wrong position"""
        right = 0
        in_the_number = 0
        wrong = 0
        remaining_secret = []
        remaining_guess = []
        #Count the digits in the right position and prepare lists for remaining digits
        for s_num, g_num in zip(secret_number, guess):
            if s_num == g_num:
                right += 1
            else:
                remaining_secret.append(s_num)
                remaining_guess.append(g_num)
        #Count the digits that are in the number but in the wrong position
        for g_num in remaining_guess:
            if g_num in remaining_secret:
                in_the_number += 1
                remaining_secret.remove(g_num)
            else:
                wrong += 1
        return right, in_the_number, wrong
