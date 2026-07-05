"""
Main program
"""
from menu import Menu
from Juegos.rps import RPS
from Juegos.num_guessing import NumGuessing


if __name__ == '__main__':

    games = {1: RPS(0, "Rock Paper Scissors", 5),
             2: NumGuessing(100, "Number Guessing Game")}

    menu1 = Menu("Gaming house")
    menu1.display_menu(games)
