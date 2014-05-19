__author__ = 'Andres'

import math
import time


def sinx(actor):
    t = time.clock() - actor.sign.spawn_time
    actor.centerx -= math.cos(t*math.pi)


def siny(actor):
    t = time.clock() - actor.sign.spawn_time
    actor.centery -= 5*math.cos(t*math.pi)


def cosx(actor):
    t = time.clock() - actor.sign.spawn_time
    actor.centerx += math.sin(t*math.pi)


def cosy(actor):
    t = time.clock() - actor.sign.spawn_time
    actor.centery += math.sin(t*math.pi)