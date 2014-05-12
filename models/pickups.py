# Pickups

import pygame
from models import Pickup


class Rupee(Pickup):
    def __init__(self, spawn_x, spawn_y,):
        self.RUPEE_SIZE_X = 8 # in pixels
        self.RUPEE_SIZE_Y = 16
        self.RUPEE_RECT = pygame.Rect(spawn_x, spawn_y, self.RUPEE_SIZE_X, self.RUPEE_SIZE_Y)
        Pickup.__init__(self, self.RUPEE_RECT)
        self.base_speed = 2

    def __init__(self, position=(0,0), dim=(8, 16), sign=None, speed=2):
        Pickup.__init__(self, [position[0], position[1], dim[0], dim[1]], sign)
        self.base_speed = speed

