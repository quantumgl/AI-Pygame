import pygame

import environment as settings
from models import Entity
from projectiles import Bullet, Laser
from pickups import Rupee


pygame.init()

class Hero(Entity):
    def __init__(self):
        # Default Rectangle for Hero
        self.hero_start_x = 20
        self.hero_start_y = settings.WINDOW_HEIGHT/2
        self.hero_size = 50 # in pixels
        self.hero_rect = pygame.Rect(self.hero_start_x, self.hero_start_y, self.hero_size, self.hero_size)

        Entity.__init__(self, self.hero_rect)
        
        self.hit_points = 3
        self.base_speed = 5  # Default speed
        self.is_firing_laser = False
        self.laser = None
        self.ok2shoot = True

    # Laser
    def fire_laser(self, time=0):
        if self.laser is not None:
            #self.is_firing_laser = True
            self.laser.x = self.right
            self.laser.y = (self.top + self.bottom)/2
            self.laser.width = settings.WINDOW_WIDTH - self.right
        else:
            self.laser = Laser(self.right, (self.top + self.bottom)/2)
        
    def stop_firing_laser(self):
        self.is_firing_laser = False
        self.laser = None

    # Bullet
    def fire_bullet(self):
        pew = Bullet(self.right, (self.top + self.bottom)/2)
        self.ok2shoot = False
        return pew

    #Recharge - TODO: this code seems excessive, need to see if all of this can be refactored more efficiently
    def ok_to_shoot(self):
        return self.ok2shoot

    def recharge(self):
        self.ok2shoot = True


class Enemy(Entity):
    def __init__(self, enemy_rect, drop_type="NONE"):
        self.drop_type = drop_type
        Entity.__init__(self, enemy_rect)
    
    def move(self):
        self.left -= self.base_speed
    
    def drop(self):
        return Rupee(self.right, self.bottom)
