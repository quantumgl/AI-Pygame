# Pickups

import pygame
from models import Pickup

class Rupee(Pickup):
    def __init__(self, spawn_x, spawn_y):
        self.RUPEE_SIZE_X = 8 # in pixels
        self.RUPEE_SIZE_Y = 16
        self.RUPEE_RECT = pygame.Rect(spawn_x, spawn_y, self.RUPEE_SIZE_X, self.RUPEE_SIZE_Y)
        Pickup.__init__(self, self.RUPEE_RECT)
        self.SPEED = 2

