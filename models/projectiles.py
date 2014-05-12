# Projectiles
import pygame

import environment as settings
from models import Projectile


class Laser(Projectile):
    def __init__(self, laser_x, laser_y, sign=None, speed=20):
        self.laser_height = 40
        self.laser_width = settings.WINDOW_WIDTH - laser_x
        self.laser_rect = pygame.Rect(laser_x, laser_y, self.laser_width, self.laser_height)

        Projectile.__init__(self, self.laser_rect, sign)
        self.base_speed = speed


class Bullet(Projectile):
    def __init__(self, spawn_x, spawn_y):
        self.bullet_width = 10
        self.bullet_height = 3
        self.bullet_rect = pygame.Rect(spawn_x, spawn_y, self.bullet_width, self.bullet_height)
        Projectile.__init__(self, self.bullet_rect)
        self.base_speed = 20

    def __init__(self, position, dim=(10, 3), sign=None, speed=20):
        dummy_rect = pygame.Rect(position[0], position[1], dim[0], dim[1])
        Projectile.__init__(self, dummy_rect, sign)
        self.base_speed = speed

    def is_out_of_screen(self):
        return self.right > settings.WINDOW_WIDTH









