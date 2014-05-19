#models.py
#Models

import time
import math
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
            self.id = ['Basic', None]


class Stats():
    def __init__(self, actor_class=None, w=1.0):
        if actor_class is None:
            self.hp = 1
            self.attack = 1
            self.defense = 0
            self.speed = 1

        if actor_class == "HERO":
            self.hp = 100
            self.attack = 15
            self.defense = 5
            self.speed = 2

        if actor_class == "TANK":
            self.hp = 15 + w/5
            self.attack = 5 + math.sqrt(w)
            self.defense = 5 + math.sqrt(w)
            self.speed = 1 + math.log(w/20)

        if actor_class == "SWARM":
            self.hp = 5 + math.sqrt(w)
            self.attack = 1 + math.log(w)
            self.defense = 1 + math.log(w)
            self.speed = 3 + math.sqrt(w)/3

        if actor_class == "NORMAL":
            self.hp = 10 + 2*math.sqrt(w)
            self.attack = 1 + math.sqrt(w)
            self.defense = 1 + math.sqrt(w)
            self.speed = 2 + math.log(w)

        if actor_class == "BOSS":
            self.hp = 50 + w*math.log(w)
            self.attack = 10 + math.sqrt(w)*math.log(w)
            self.defense = 10 + math.sqrt(w)*math.log(w)
            self.speed = 2 + math.log(w)

        if actor_class == "SCATTER":
            self.hp = 1 + math.log(w)
            self.attack = 3 + math.sqrt(w)
            self.defense = 2 + math.sqrt(w)*math.log(w)
            self.speed = 2 + math.sqrt(w)/20

        if actor_class == "SPEED":
            self.hp = 10 + math.log(w)
            self.attack = 5 + math.sqrt(w)
            self.defense = 2 + math.log(w)
            self.speed = 5 + math.sqrt(w)/10

        if actor_class == "GHOST":
            self.hp = 1 + math.log(w)
            self.attack = 10 + math.sqrt(w)
            self.defense = 1000000
            self.speed = 3 + math.log(w)*math.sqrt(w)/50

        if actor_class == "SPEED":
            self.hp = 10 + math.log(w)
            self.attack = 5 + math.sqrt(w)
            self.defense = 2 + math.log(w)
            self.speed = 5 + math.sqrt(w)/10

        if actor_class == "MIMIC":
            self.hp = 100 + math.sqrt(w)
            self.attack = 5 + 2*math.sqrt(w)
            self.defense = 1 + math.log(w)
            self.speed = 3 + 5*math.log(w)

        self.current_hp = self.hp


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
    def __init__(self, proj_rect, sign=None, parent_stats=None):
        Actor.__init__(self, proj_rect, sign)
        self.parent_stats = parent_stats

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
    def __init__(self, entity_rect, sign=None, w=1):
        Actor.__init__(self, entity_rect, sign)
        if sign is None:
            self.stats = Stats(None, w)
        else:
            self.stats = Stats(self.sign.id[0])
        self.alive = True

    def get_hit_by(self, projectile):
        possible_damage = projectile.parent_stats.attack - self.stats.defense
        self.stats.defense -= 1
        if possible_damage > 0:
            self.stats.current_hp -= possible_damage
        if self.stats.current_hp <= 0:
            self.alive = False