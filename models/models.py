#models.py
#Models

import time
import pygame
import physics

pygame.init()


class Signature():
    def __init__(self, construct):
        self.spawn_time = time.clock()
        if construct is not None:
            self.instance_of = construct[0]
            self.id = construct[1]
        else:
            self.instance_of = 'Actor'
            self.id = ['Basic', []]


# Everything in the game that can be seen is an Actor. This is the master class for all the models to be implemented.
class Actor(pygame.Rect):

    def __init__(self, rect, sign=None):
        pygame.Rect.__init__(self, rect)
        self.sign = Signature(sign)
        self.base_speed = 0
        self.dir_x = 0
        self.dir_y = 0
        self.direction = (0, 0)

    def change_direction(self, direction):
        self.dir_x = direction[0]
        self.dir_y = direction[1]

    def update_direction(self, direction):
        self.direction = physics.normalize(direction)

    def update_pos(self):
        self.x += self.dir_x * self.base_speed
        self.y += self.dir_y * self.base_speed


#-Subclasses of Actor-----------------------

# Every type of projectile in the game such as a laser or bullet will be a subclass of this.
class Projectile(Actor):
    def __init__(self, proj_rect, sign=None):
        Actor.__init__(self, proj_rect, sign)

    def move(self):
        self.left += self.base_speed


# Every type of pickup, such as rupees, power-ups, or items will be a subclass of this.
class Pickup(Actor):
    def __init__(self, pickup_rect, sign=None):
        Actor.__init__(self, pickup_rect, sign)

    def move(self):
        self.left -= self.base_speed


# Every type of living or sentient being in the game will be a subclass of Entity, such as Enemy, Hero, etc
class Entity(Actor):
    def __init__(self, entity_rect):
        Actor.__init__(self, entity_rect)