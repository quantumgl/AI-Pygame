import pygame

import environment as settings
from models import Entity
from projectiles import Bullet, Laser
from pickups import Rupee


pygame.init()

class Hero(Entity):
    def __init__(self):
        # Default Rectangle for Hero
        self.HERO_START_X = 20
        self.HERO_START_Y = settings.WINDOW_HEIGHT/2
        self.HERO_SIZE = 50 # in pixels
        self.HERO_RECT = pygame.Rect(self.HERO_START_X, self.HERO_START_Y, self.HERO_SIZE, self.HERO_SIZE)

        Entity.__init__(self, self.HERO_RECT) # pygame.Rect super constructor
        
        self.hit_points = 3
        self.SPEED = 5 # Default speed
        self.is_firing_laser = False
        self.laser = None
        self.ok2shoot = True

    # Laser - TODO: fix laser so that it is not instantiated every frame, which causes collision skipping.
    def fire_laser(self):
        if self.is_firing_laser and self.laser != None:
            self.laser.x = self.right
            self.laser.y = (self.top + self.bottom)/2
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
    def __init__(self, enemy_rect):

        Entity.__init__(self, enemy_rect) # pygame.Rect super constructor
    
    def move(self):
        self.left -= self.SPEED
    
    def drop(self):
        return Rupee(self.right, self.bottom)
