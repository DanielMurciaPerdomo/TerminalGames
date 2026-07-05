"""
Game Class for general attributes on all the games
"""
class Game:
    """Class representing a game"""
    def __init__(self, score, name):
        self.score = score
        self.name = name

    def display_score(self):
        """Show the score"""
        print(f"The score is: {self.score}")

