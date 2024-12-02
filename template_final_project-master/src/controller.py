import pygame
from class2 import CarGame, Window

class Controller:
    def __init__(self):
        pygame.init()  # Initialize Pygame
        self.window = Window()  # Create the game window
        self.car_game = CarGame(self.window)  # Pass the window to CarGame

    def mainloop(self):
        self.car_game.start_gameloop()  # Start the game loop


if __name__ == "__main__":
    app = Controller()
    app.mainloop()