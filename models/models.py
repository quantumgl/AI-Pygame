#models.py
#Models

import pygame

pygame.init()

# Inherits from pygame.Rect
# Therefore, every method from pygame.Rect can be called
# on each instance of Actor and its subclasses

# Everything in the game that can be seen is an Actor. This is the master class for all the models to be implemented.
class Actor(pygame.Rect):

    def __init__(self, rect):
        pygame.Rect.__init__(self, rect.left, rect.top, rect.width, rect.height)
        self.SPEED = 0 # Default speed    
        self.dir_x = 0
        self.dir_y = 0

    def change_direction(self, direction):
        self.dir_x = direction[0]
        self.dir_y = direction[1]

    def update_pos(self):
        self.x += self.dir_x * self.SPEED
        self.y += self.dir_y * self.SPEED


#-Subclasses of Actor-----------------------

# Every type of projectile in the game such as a laser or bullet will be a subclass of this.
class Projectile(Actor):
    def __init__(self, proj_rect):
        Actor.__init__(self, proj_rect)

    def move(self):
        self.left += self.SPEED

# Every type of pickup, such as rupees, power-ups, or items will be a subclass of this.
class Pickup(Actor):
    def __init__(self, pickup_rect):
        Actor.__init__(self, pickup_rect)

    def move(self):
        self.left -= self.SPEED

# Every type of living or sentient being in the game will be a subclass of Entity, such as Enemy, Hero, etc
class Entity(Actor):
    def __init__(self, entity_rect):
        Actor.__init__(self, entity_rect)
			
