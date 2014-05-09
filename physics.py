#!/usr/bin/env python
"""physics.py: Functions that help control the physics in the game environment"""

__author__ = "Andres"
__email__ = "andresgl@live.com"
__status__ = "Development"

import random
import pygame
import environment as env


pygame.init()


def get_random_coordinates(width, height):
    """
    Returns a random 2D coordinate as a 2-tuple, scaled to current window size

    :type height: int
    :type width: int
    :rtype : (int, int)
    """
    rand_x = random.randint(width, env.WINDOW_WIDTH-width)
    rand_y = random.randint(height, env.WINDOW_HEIGHT-height)
    return rand_x, rand_y


def check_collision(rect_1, rect_2):
    """
    Returns True if rectangles are colliding
    """
    dx = abs(rect_1.centerx - rect_2.centerx)
    dy = abs(rect_1.centery - rect_2.centery)
    return dx < (rect_1.width + rect_2.width)/2 and dy < (rect_1.height + rect_2.height)/2

#---Movement-Management(Boundary and hero movement constraint)

#---BOUNDARY---


def locate_in_boundary(target, boundary):
    """
    Returns a loc_string location string, indicating where target is with respect to its boundary
    """
    b_top = target.top - boundary.top
    b_bottom = target.bottom - boundary.bottom
    b_left = target.left - boundary.left
    b_right = target.right - boundary.right

    top = b_top <= 0
    bottom = b_bottom >= 0
    left = b_left <= 0
    right = b_right >= 0

    if top and right:
        return "TOP_RIGHT"
    elif top and left:
        return "TOP_LEFT"
    elif bottom and right:
        return "BOTTOM_RIGHT"
    elif bottom and left:
        return "BOTTOM_LEFT"
    elif top:
        return "TOP"
    elif bottom:
        return "BOTTOM"
    elif left:
        return "LEFT"
    elif right:
        return "RIGHT"
    else: 
        return "BOUNDED"


#movement manager (hero) 
def movement_manager(target, loc_string):
    """
    Neutralizes target's dir_x and/or dir_y attributes according to loc_string infraction.
    """
    if loc_string == "TOP":
        if target.dir_y < 0:
            target.dir_y = 0

    if loc_string == "BOTTOM":
        if target.dir_y > 0:
            target.dir_y = 0

    if loc_string == "LEFT":
        if target.dir_x < 0:
            target.dir_x = 0

    if loc_string == "RIGHT":
        if target.dir_x > 0:
            target.dir_x = 0

    if loc_string == "TOP_RIGHT":
        if (target.dir_y < 0) and (target.dir_x > 0):
            target.dir_y = 0
            target.dir_x = 0
        if target.dir_y < 0:
            target.dir_y = 0
        if target.dir_x > 0:
            target.dir_x = 0

    if loc_string == "TOP_LEFT":
        if (target.dir_y < 0) and (target.dir_x < 0):
            target.dir_y = 0
            target.dir_x = 0
        if target.dir_y < 0:
            target.dir_y = 0
        if target.dir_x < 0:
            target.dir_x = 0

    if loc_string == "BOTTOM_RIGHT":
        if (target.dir_y > 0) and (target.dir_x > 0):
            target.dir_y = 0
            target.dir_x = 0
        if target.dir_y > 0:
            target.dir_y = 0
        if target.dir_x > 0:
            target.dir_x = 0

    if loc_string == "BOTTOM_LEFT":
        if (target.dir_y > 0) and (target.dir_x < 0):
            target.dir_y = 0
            target.dir_x = 0
        if target.dir_y > 0:
            target.dir_y = 0
        if target.dir_x < 0:
            target.dir_x = 0
