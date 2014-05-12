#Graphics Manager
# The class that manages the drawing of all objects in the game.


import random
import pygame
import environment

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WING_YELLOW = pygame.image.load('img/colorwings/wing yellow.png')
WING_GREY = pygame.image.load('img/colorwings/wing grey.png')
WING_PURPLE = pygame.image.load('img/colorwings/wing purple.png')
WING_PINK = pygame.image.load('img/colorwings/wing pink.png')
WING_ORANGE = pygame.image.load('img/colorwings/wing orange.png')
WING_GREEN = pygame.image.load('img/colorwings/wing green.png')
WING_AQUA = pygame.image.load('img/colorwings/wing aqua.png')
WING_BLUE = pygame.image.load('img/colorwings/wing blue.png')
WING_RED = pygame.image.load('img/colorwings/wing red.png')

WING_COLORS = [
    "YELLOW", "PURPLE", "PINK", "ORANGE", "GREEN", "AQUA", "RED", "BLUE", "GREY"
]

WINGS = {
    "YELLOW": WING_YELLOW,
    "GREY": WING_GREY,
    "PURPLE": WING_PURPLE,
    "PINK": WING_PINK,
    "ORANGE": WING_ORANGE,
    "GREEN": WING_GREEN,
    "AQUA": WING_AQUA,
    "BLUE": WING_BLUE,
    "RED": WING_RED
}

ORB_YELLOW = pygame.image.load('img/orbs/orb yellow.png')
ORB_WHITE = pygame.image.load('img/orbs/orb white.png')
ORB_PURPLE = pygame.image.load('img/orbs/orb purple.png')
ORB_PINK = pygame.image.load('img/orbs/orb pink.png')
ORB_ORANGE = pygame.image.load('img/orbs/orb orange.png')
ORB_GREEN = pygame.image.load('img/orbs/orb green.png')
ORB_AQUA = pygame.image.load('img/orbs/orb aqua.png')
ORB_BLUE = pygame.image.load('img/orbs/orb blue.png')
ORB_RED = pygame.image.load('img/orbs/orb red.png')

ORB_COLORS = [
    "YELLOW", "WHITE", "PURPLE", "PINK", "ORANGE", "GREEN", "AQUA"
]
ORBS = {
    "YELLOW": ORB_YELLOW,
    "WHITE": ORB_WHITE,
    "PURPLE": ORB_PURPLE,
    "PINK": ORB_PINK,
    "ORANGE": ORB_ORANGE,
    "GREEN": ORB_GREEN,
    "AQUA": ORB_AQUA,
    "BLUE": ORB_BLUE,
    "RED": ORB_RED
}

LASER_ITEM = pygame.image.load('img/laser/laser item.png')

LASER = {
    "PICKUP": LASER_ITEM,
    "HUD": LASER_ITEM,
    "LASER": {
        "CHAINS": [],
        "AURAS": []
    }
}


# Images		
BACKGROUND = pygame.image.load('img/cloud background.png')
HERO_IMG = pygame.image.load('img/hero and goatee.png')
HERO_IMG = pygame.Surface.convert_alpha(HERO_IMG)
RUPEE_IMG = pygame.image.load('img/item thingie.png')
ENEMY_IMG = pygame.image.load('img/enemy navi.png')
LASER_IMG = pygame.image.load('img/laser.png')
PEW_IMG = pygame.image.load('img/pew.png')


"""
Handles all the drawing of the Actor instance.
-> screen is the Surface object which the Actor will be drawn on
"""


def draw_background(screen):
    if BACKGROUND is None:
        pygame.draw.rect(screen, BLACK, [0, 0, environment.WINDOW_WIDTH, environment.WINDOW_HEIGHT])
    else:
        screen.blit(BACKGROUND, (0, 0))


def draw_hero(screen, hero):
    if HERO_IMG is None:
        pygame.draw.rect(screen, RED, [hero.x, hero.y, hero.get_width(), hero.get_height()])
    else:
        screen.blit(HERO_IMG, (hero.x, hero.y))


def draw_enemy(screen, enemy):
    if ENEMY_IMG is None:
        pygame.draw.rect(screen, RED, [enemy.x, enemy.y, enemy.get_width(), enemy.get_height()])
    else:
        screen.blit(WINGS[WING_COLORS[random.randint(0, 6)]], (enemy.x+enemy.width/2, enemy.y))
        screen.blit(ORBS[ORB_COLORS[random.randint(0, 6)]], (enemy.x, enemy.y))


def draw_rupee(screen, rupee):
    if RUPEE_IMG is None:
        pygame.draw.rect(screen, RED, [rupee.x, rupee.y, rupee.get_width(), rupee.get_height()])
    else:
        screen.blit(RUPEE_IMG, (rupee.x, rupee.y))


def draw_laser(screen, laser):
    if LASER_IMG is None:
        pygame.draw.rect(screen, RED, [laser.x, laser.y, laser.get_width(), laser.get_height()])
    else:
        screen.blit(LASER_IMG, (laser.x, laser.y))


def draw_pewpew(screen, pewpew):
    if PEW_IMG is None:
        pygame.draw.rect(screen, RED, [pewpew.x, pewpew.y, pewpew.width, pewpew.height])
    else:
        screen.blit(PEW_IMG, (pewpew.x, pewpew.y))






