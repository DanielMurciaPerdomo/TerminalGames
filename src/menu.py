"""Module providing a funtion to display menu"""
class Menu:
    """Class representing a Menu"""
    def __init__(self, titulo):
        self.titulo = titulo

    def display_menu(self, games):
        """Showing the menu using the titulo """
        is_running = True
        while is_running:
            print("*******************************")
            print(f"        {self.titulo}         ")
            print("*******************************")
            for num, game in games.items():
                print(f"{num}. {game.name}")
            choice = input("Select the number of game to play or 0 to quit: ")
            if not choice.isdigit():
                print("Invalid input. Please enter a number.")
                continue
            choice = int(choice)
            if choice in games.keys():
                games[choice].display_game()
            elif choice == 0:
                is_running = False
            else:
                print("Invalid choice. Please select a valid game number.")
