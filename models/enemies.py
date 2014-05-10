# Enemies
import pygame
from entities import Enemy

class Waddle_Dee(Enemy):
    def __init__(self, spawn_x, spawn_y):
        self.WADDLE_DEE_SIZE = 32
        self.WADDLE_DEE_RECT = pygame.Rect(spawn_x, spawn_y, self.WADDLE_DEE_SIZE, self.WADDLE_DEE_SIZE)

        Enemy.__init__(self, self.WADDLE_DEE_RECT)
        self.SPEED = 2

