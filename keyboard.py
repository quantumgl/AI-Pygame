__author__ = 'Andres'

import pygame
from pygame.locals import *
pygame.init()

question = {
    "YES": K_y,
    "NO": K_n
}

arrow_keys = {
    "UP": K_UP,
    "DOWN": K_DOWN,
    "LEFT": K_LEFT,
    "RIGHT": K_RIGHT
}

system = {
    "MUTE": K_m,
    "=": K_EQUALS,
    "K+": K_KP_PLUS,
    "-": K_MINUS,
    "K-": K_KP_MINUS,
    "PAUSE": K_p,
    "QUIT": K_q,
    "ESCAPE": K_ESCAPE,
    "ENTER": K_RETURN
}

weapons = {
    "LASER": K_SPACE,
    "PEW": K_x
}

directions = {
    "NONE": (0, 0),
    "UP": (0, -1),
    "DOWN": (0, 1),
    "LEFT": (-1, 0),
    "RIGHT": (1, 0),
    "UP_LEFT": (-1, -1),
    "UP_RIGHT": (1, -1),
    "DOWN_LEFT": (-1, 1),
    "DOWN_RIGHT": (1, 1)
}


def start(event):
    """
    Whether or not return was pressed
    """
    return event.type == KEYDOWN and event.key == system["ENTER"]


def escape_prompt(event, gameover=False):
    """
    True if escape or red x is pressed, also true if n is pressed during a continue prompt
    """
    red_x_pressed = event.type == QUIT
    escape_pressed = event.type == KEYDOWN and event.key == system["ESCAPE"]
    negative_answer = event.type == KEYDOWN and event.key == question["NO"]

    if not gameover:
        return red_x_pressed or escape_pressed
    else:
        return red_x_pressed or escape_pressed or negative_answer


def restart(event, gameover=False):
    """
    True if y is pressed during a continue prompt
    """
    if gameover:
        return event.type == KEYDOWN and event.key == question["YES"]
    else:
        return False


def pause_prompt(keys):
    """
    Returns true if 'p' was pressed
    """
    return keys[system["PAUSE"]]


def music_prompt(keys):
    """
    Returns true if 'm' was pressed
    """
    return keys[system["MUTE"]]


def increase_prompt(keys):
    """
    Returns true if keypad '+' or '=' was pressed
    """
    return keys[system["K+"]] or keys[system["="]]


def decrease_prompt(keys):
    """
    Returns true if '-' or keypad '-' was pressed
    """
    return keys[system["-"]] or keys[system["K-"]]


def laser_prompt(keys):
    """
    Returns true if the space bar was pressed
    """
    if keys[weapons["LASER"]]:
        return True
    return False


def pew_prompt(keys):
    """
    Returns true if 'x' was pressed
    """
    if keys[weapons["PEW"]]:
        return True
    return False


def movement(keys):
    """
     Returns direction as a tuple based on arrow keys
    """
    up = keys[arrow_keys["UP"]]
    left = keys[arrow_keys["LEFT"]]
    right = keys[arrow_keys["RIGHT"]]
    down = keys[arrow_keys["DOWN"]]
    direction = directions["NONE"]
    for d in arrow_keys:
        if keys[arrow_keys[d]]:
            direction = directions[d]
    #Diagonals
    if up and left:
        direction = directions["TOP_LEFT"]
    if up and right:
        direction = directions["TOP_RIGHT"]
    if down and left:
        direction = directions["BOTTOM_LEFT"]
    if down and right:
        direction = directions["BOTTOM_RIGHT"]

    return direction
