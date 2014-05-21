__author__ = 'Andres'

import math
import time


def sinx(actor, stats):
    t = time.clock() - actor.sign.spawn_time
    actor.centerx -= stats.speed*math.cos(t*math.pi)


def siny(actor, stats):
    t = time.clock() - actor.sign.spawn_time
    actor.centery -= stats.speed*math.cos(t*math.pi)


def cosx(actor, stats):
    t = time.clock() - actor.sign.spawn_time
    actor.centerx += stats.speed*math.sin(t*math.pi)


def cosxx(actor, stats):
    t = time.clock() - actor.sign.spawn_time
    actor.centerx += stats.speed*math.sin(t*math.pi) - t


def cosy(actor, stats):
    t = time.clock() - actor.sign.spawn_time
    actor.centery += stats.speed*math.sin(t*math.pi)