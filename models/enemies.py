# Enemies
import pygame
from entities import Enemy


class Waddle_Dee(Enemy):
    def __init__(self, spawn_x, spawn_y, sign=None, w=1.0):
        self.waddle_dee_size = 32
        self.waddle_dee_rect = pygame.Rect(spawn_x, spawn_y, self.waddle_dee_size, self.waddle_dee_size)

        Enemy.__init__(self, self.waddle_dee_rect, sign, w)
        if self.stats.speed > 1:
            self.base_speed = self.stats.speed