import pygame
from pygame.locals import *
import random
import model_a
import model_b
import action
import class2

class Controller:
    def __init__(self):
        pygame.init()
        """
        """
        self.screen = pygame.display.set_mode((800, 600))
    
    def mainloop(self):
        """
        hi
        """
        while(True):
            """
            summary_
            """
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() 
                    exit()
            pygame.display.flip()