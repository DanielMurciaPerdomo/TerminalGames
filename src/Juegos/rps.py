"""
Rock Paper Scissors game
"""
import random

try:
    from .juego import Game
except ImportError:
    from juego import Game

class RPS(Game):
    """Class representing a rock paper scissors game"""
    options = ('Rock', 'Paper', 'Scissors')
    def __init__(self, score, name, limite):
        super().__init__(score, name)
        self.limite = limite

    def display_game(self):
        """Show the game to play"""
        is_running = True
        computer_point = 0
        player_point = 0
        while is_running:
            choice = input("Rock, Paper or Scissors ?(Just one of them) or q to quit: \n").lower()
            computer = random.choice(self.options).lower()
            #Ending game when the total points reach the limit
            if choice == 'q' or (player_point+computer_point) >= self.limite:
                is_running = False
                print(f"Game over! Final score: Player {player_point} - Computer {computer_point}")

            #Confirming the user input is valid
            if choice not in [option.lower() for option in self.options]:
                print("Invalid choice. Please select Rock, Paper, or Scissors.")
                continue

            #Comparing the user input with the computer choice and updating the score
            if choice == computer:
                print(f"Tie! Points: Player {player_point} - Computer {computer_point}")
            elif choice == 'rock' and computer == 'scissors':
                player_point += 1
                print(f"You win! Points: Player {player_point} - Computer {computer_point}")
            elif choice == 'paper' and computer == 'rock':
                player_point += 1
                print(f"You win! Points: Player {player_point} - Computer {computer_point}")
            elif choice == 'scissors' and computer == 'paper':
                player_point += 1
                print(f"You win! Points: Player {player_point} - Computer {computer_point}")
            else:
                computer_point += 1
                print(f"You lose! Points: Player {player_point} - Computer {computer_point}")
