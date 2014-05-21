import pygame

import environment as settings
from models import Entity, Enemy_Bar
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

        Entity.__init__(self, self.hero_rect, ["HERO", ["HERO", "HERO"]])
        
        self.hit_points = 3
        self.base_speed = 5  # Default speed
        self.is_firing_laser = False
        self.laser = None
        self.ok2shoot = True
        self.laser_equipped = False
        self.fire_time = -1

    def equip_laser(self):
        self.laser_equipped = True

    # Laser
    def fire_laser(self, time=0):
        if self.laser_equipped:
            if self.laser is not None:
                #self.is_firing_laser = True
                self.laser.x = self.right
                self.laser.y = (self.top + self.bottom)/2
                self.laser.width = settings.WINDOW_WIDTH - self.right
            else:
                self.laser = Laser(self.right, (self.top + self.bottom)/2)
        
    def stop_firing_laser(self):
        self.laser_equipped = False
        self.is_firing_laser = False
        self.laser = None

    # Bullet
    def fire_bullet(self):
        pew = Bullet(self.right, (self.top + self.bottom)/2, parent_stat=self.stats)
        self.ok2shoot = False
        return pew

    #Recharge - TODO: this code seems excessive, need to see if all of this can be refactored more efficiently
    def ok_to_shoot(self):
        return self.ok2shoot

    def recharge(self):
        self.ok2shoot = True

    def knockback(self):
        new_pos = self.x - 30
        if new_pos > 0:
            self.x = new_pos
        else:
            self.x = 0

    def get_hit_by_enemy(self, enemy):
        if self.vulnerable:
            damage = enemy.stats.attack - self.stats.defense
            print "Damage: ", damage
            if damage > 1:
                if damage > self.stats.current_hp:
                    self.stats.current_hp = 0
                else:
                    self.stats.current_hp -= damage
                print "Current hp updated:", self.stats.current_hp

    def isdead(self):
        return self.stats.current_hp == 0


class Enemy(Entity):
    def __init__(self, enemy_rect, sign=None, w=1.0):
        Entity.__init__(self, enemy_rect, sign, w)
        self.bar = Enemy_Bar(self.stats, (self.centerx, self.centery))
    
    def move(self):
        self.left -= self.base_speed
    
    def drop(self, pickup_sign):
        return Rupee(self.right, self.bottom, sign=pickup_sign)

    def update_bar(self):
        self.bar.update(self.stats, (self.centerx, self.centery), (self.width, self.height))

    def get_hit_by(self, projectile):
        super(Enemy, self).get_hit_by(projectile)
        self.bar.set_visible()