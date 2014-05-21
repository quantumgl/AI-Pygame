#models.py
#Models

import time
import math
import pygame
import physics
import environment

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

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
        print w
        if actor_class is None:
            self.hp = 1
            self.attack = 1
            self.defense = 0
            self.speed = 1

        if actor_class == "HERO":
            self.hp = 100
            self.attack = 15
            self.defense = 0
            self.speed = 2

        if actor_class == "TANK":
            self.hp = 15 + w
            self.attack = 5 + math.sqrt(w)
            self.defense = 5 + w*math.log(w)
            self.speed = 1 + math.log(w/10 + 5)

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
            self.hp = 3 + math.log(w)
            self.attack = 3 + math.sqrt(w)
            self.defense = 2 + math.sqrt(w)*math.log(w)
            self.speed = 2 + math.sqrt(w)/20

        if actor_class == "SPEED":
            self.hp = 10 + math.log(w)
            self.attack = 5 + math.sqrt(w)
            self.defense = 2 + math.log(w)
            self.speed = 5 + math.sqrt(w)/math.log(w+1)

        if actor_class == "GHOST":
            self.hp = 2 + math.log(w)
            self.attack = 10 + math.sqrt(w)
            self.defense = 10 + math.sqrt(w)
            self.speed = 3 + math.log(w)*math.sqrt(w)/20
        """
        if actor_class == "SPEED":
            self.hp = 10 + math.log(w)
            self.attack = 5 + math.sqrt(w)
            self.defense = 2 + math.log(w)
            self.speed = 5 + math.sqrt(w)
        """
        if actor_class == "MIMIC":
            self.hp = 100 + math.sqrt(w)
            self.attack = 5 + 2*math.sqrt(w)
            self.defense = 1 + math.log(w)
            self.speed = 3 + 2*math.log(w)

        self.current_hp = self.hp


class Bar(pygame.Rect):
    def __init__(self, stats=None, actor=None):
        pygame.Rect.__init__(self, [0,0,0,0])
        if stats is None:
            self.color = RED
            self.centerx = environment.WINDOW_WIDTH - 400
            self.centery = environment.WINDOW_HEIGHT - 40
        else:
            self.height = 20
            self.width = (212.0*stats.current_hp)/stats.hp
            if actor.sign.id[0] == "HERO":
                self.color = GREEN
                self.centerx = 145
                self.centery = 15
            else:
                self.color = RED
                self.centerx = environment.WINDOW_WIDTH - 400
                self.centery = environment.WINDOW_HEIGHT - 40
        self.stats = stats
        self.visible = True

    def update(self, stats):
        self.height = 20
        self.width = (212.0*stats.current_hp)/stats.hp
        print "width", self.width

    def reset(self, stats):
        if stats == self.stats:
            self.width = 0
            self.height = 0


class Enemy_Bar(pygame.Rect):
    def __init__(self, parents_stats, parent_pos):
        pygame.Rect.__init__(self, parent_pos[0], parent_pos[1], parents_stats.hp/5, 5)
        self.color = RED
        self.visible = False

    def update(self, parent_stats, parent_pos, parent_size):
        self.centerx = parent_pos[0]
        self.centery = parent_pos[1] + parent_size[1]/2
        self.width = parent_stats.current_hp/5

    def set_visible(self):
        self.visible = True


# Everything in the game that can be seen is an Actor. This is the master class for all the models to be implemented.
class Actor(pygame.Rect):

    def __init__(self, rect, sign=None):
        pygame.Rect.__init__(self, rect)
        self.sign = Signature(sign)
        self.base_speed = 6
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
            self.stats = Stats(self.sign.id[0], w)
        self.alive = True
        self.vulnerable = True
        self.vulnerability_time = -1

    def get_hit_by(self, projectile):
        if self.vulnerable:
            possible_damage = projectile.parent_stats.attack - self.stats.defense
            self.stats.defense -= 1
            if possible_damage > 0:
                self.stats.current_hp -= possible_damage
            if self.stats.current_hp <= 0:
                self.alive = False

    def give_immunity(self):
        self.vulnerable = False
        self.vulnerability_time = time.clock()

    def take_immunity(self):
        self.vulnerable = True
        self.vulnerability_time = -1