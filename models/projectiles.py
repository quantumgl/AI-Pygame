# Projectiles
import pygame

import environment
from models import Projectile


class Laser(Projectile):
    def __init__(self, laser_x, laser_y, sign=None, speed=20):
        self.laser_height = 40
        self.laser_width = environment.WINDOW_WIDTH - laser_x
        self.laser_rect = pygame.Rect(laser_x, laser_y, self.laser_width, self.laser_height)

        Projectile.__init__(self, self.laser_rect, sign)
        self.base_speed = speed


class Bullet(Projectile):
    """ def __init__(self, spawn_x, spawn_y):
        self.bullet_width = 10
        self.bullet_height = 3
        self.bullet_rect = pygame.Rect(spawn_x, spawn_y, self.bullet_width, self.bullet_height)
        Projectile.__init__(self, self.bullet_rect)
        self.base_speed = 20
    """
    def __init__(self, posx=0, posy=0, dimx=10, dimy=3, sign=None, parent_stat=None, speed=20):
        dummy_rect = pygame.Rect(posx, posy, dimx, dimy)
        Projectile.__init__(self, dummy_rect, sign, parent_stats=parent_stat)
        self.base_speed = speed

    def is_out_of_screen(self):
        return self.right > environment.WINDOW_WIDTH









