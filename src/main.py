"""
Main program
"""
from menu import Menu
from Juegos.rps import RPS


if __name__ == '__main__':

    games = {1: RPS(0, "Rock Paper Scissors", 5)}

    menu1 = Menu("Gaming house")
    menu1.display_menu(games)
