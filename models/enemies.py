# Enemies
import pygame
from entities import Enemy


class Waddle_Dee(Enemy):
    def __init__(self, spawn_x, spawn_y):
        self.waddle_dee_size = 32
        self.waddle_dee_rect = pygame.Rect(spawn_x, spawn_y, self.waddle_dee_size, self.waddle_dee_size)

        Enemy.__init__(self, self.waddle_dee_rect, "Rupee")
        self.base_speed = 2

