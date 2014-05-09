# Projectiles
import pygame

import settings
from models.models import Projectile


class Laser(Projectile):
    def __init__(self, laser_x, laser_y):
        self.LASER_HEIGHT = 10
        self.LASER_WIDTH = settings.WINDOW_WIDTH - laser_x
        self.LASER_RECT = pygame.Rect(laser_x, laser_y, self.LASER_WIDTH, self.LASER_HEIGHT)

        Projectile.__init__(self, self.LASER_RECT)
        self.SPEED = 0


class Bullet(Projectile):
    def __init__(self, spawn_x, spawn_y):
        self.BULLET_WIDTH = 10
        self.BULLET_HEIGHT = 3
        self.BULLET_RECT = pygame.Rect(spawn_x, spawn_y, self.BULLET_WIDTH, self.BULLET_HEIGHT)

        Projectile.__init__(self, self.BULLET_RECT)
        self.SPEED = 20

    def is_out_of_screen(self):
        return self.right > settings.WINDOW_WIDTH









