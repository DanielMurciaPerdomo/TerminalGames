"""Module providing a funtion to display menu"""
class Menu:
    """Class representing a Menu"""
    def __init__(self, titulo):
        self.titulo = titulo

    def display_menu(self):
        """Showing the menu using the titulo """
        print("*******************************")
        print(f"        {self.titulo}         ")
        print("*******************************")
