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

STACHE_LONG = pygame.image.load('img/staches/stache long.png')
STACHE_HITLER = pygame.image.load('img/staches/stache hitler.png')
STACHE_CURLY = pygame.image.load('img/staches/stache curly end.png')
STACHE_SHARP = pygame.image.load('img/staches/stache sharp.png')
STACHE_WIDE = pygame.image.load('img/staches/stache wide.png')



STACHES = {
    "LONG": STACHE_LONG,
    "HITLER": STACHE_HITLER,
    "CURLY": STACHE_CURLY,
    "SHARP": STACHE_SHARP,
    "WIDE": STACHE_WIDE
}

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

CLASS_TO_TYPE = {
    "TANK": "YELLOW",
    "SWARM": "ORANGE",
    "NORMAL": "GREEN",
    "BOSS": "RED",
    "SCATTER": "PURPLE",
    "SPEED": "PINK",
    "GHOST": "WHITE",
    "MIMIC": "AQUA"
}

LASER_ITEM = pygame.image.load('img/laser/laser item.png')
GLOW_ORANGE = pygame.image.load('img/laser/laser glow orange long.png').convert_alpha()
GLOW_BLUE = pygame.image.load('img/laser/laser glow blue long.png').convert_alpha()
GLOW_GREEN = pygame.image.load('img/laser/laser glow green long.png').convert_alpha()
GLOW_PINK = pygame.image.load('img/laser/laser glow pink long.png').convert_alpha()
GLOW_VIOLET = pygame.image.load('img/laser/laser glow violet long.png').convert_alpha()

ORBITAL_LONG = pygame.image.load('img/laser/laser orbital long.png').convert_alpha()
BUMPS_LONG = pygame.image.load('img/laser/laser bumps long.png').convert_alpha()

empty_laser = pygame.image.load('img/laser/empty_laser.png')

LASER = {
    "PICKUP": LASER_ITEM,
    "HUD": LASER_ITEM,
    "LASER": {
        "BEAMS": [
            ORBITAL_LONG, BUMPS_LONG
        ],
        "AURAS": [
            GLOW_ORANGE, GLOW_BLUE, GLOW_GREEN, GLOW_PINK, GLOW_VIOLET
        ]
    }
}

the_range = range(len(LASER["LASER"]["AURAS"]))
the_other_range = range(len(LASER["LASER"]["BEAMS"]))

HP_BORDER = pygame.image.load('img/misc/hp bar border.png')
HP_ITEM = pygame.image.load('img/misc/heart icon purple.png')
HP_HEART = pygame.image.load('img/misc/heart icon red.png')

SHIELD_ITEM = pygame.image.load('img/misc/shield item.png')
MONEY_ITEM = pygame.image.load('img/item thingie.png')

ITEMS = {
    "HP": HP_ITEM,
    "LASER": LASER_ITEM,
    "DEFENSE": SHIELD_ITEM,
    "MONEY": MONEY_ITEM
}

# Images		
BACKGROUND = pygame.image.load('img/cloud background.png')
HERO_IMG = pygame.image.load('img/hero and goatee.png')
RUPEE_IMG = pygame.image.load('img/item thingie.png')
ENEMY_IMG = pygame.image.load('img/enemy navi.png')
LASER_IMG = pygame.image.load('img/laser.png')
PEW_IMG = pygame.image.load('img/pew.png')

laser_offset = 0
ticks = 0
"""
Handles all the drawing of the Actor instance.
-> screen is the Surface object which the Actor will be drawn on
"""


def draw_bar(screen, bar, hero_bar=False):
    if hero_bar:
        screen.blit(HP_HEART, (bar.left - 27, bar.top + 2))
        screen.blit(HP_BORDER, (bar.x - 4, bar.y - 4))
    if bar.visible:
        pygame.draw.rect(screen, bar.color, bar)


def draw_background(screen):
    if BACKGROUND is None:
        pygame.draw.rect(screen, BLACK, [0, 0, environment.WINDOW_WIDTH, environment.WINDOW_HEIGHT])
    else:
        screen.blit(BACKGROUND, (0, 0))


def draw_hero(screen, hero):
    if HERO_IMG is None:
        pygame.draw.rect(screen, RED, hero)
    else:
        screen.blit(HERO_IMG, (hero.x, hero.y))


def draw_enemy(screen, enemy):
    if ENEMY_IMG is None:
        pygame.draw.rect(screen, RED, [enemy.x, enemy.y, enemy.get_width(), enemy.get_height()])
    else:
        screen.blit(WINGS[enemy.sign.id[1]], (enemy.x+enemy.width/2, enemy.y))
        enemy_class = enemy.sign.id[0]
        screen.blit(ORBS[CLASS_TO_TYPE[enemy_class]], (enemy.x, enemy.y))
        screen.blit(STACHES[enemy.sign.id[2]], ((enemy.x + enemy.centerx - 5)/2, enemy.centery + 5))


def draw_rupee(screen, rupee):
    if RUPEE_IMG is None:
        pygame.draw.rect(screen, RED, [rupee.x, rupee.y, rupee.get_width(), rupee.get_height()])
    else:
        screen.blit(LASER_ITEM, (rupee.x, rupee.y))


def draw_pickup(screen, pickup):
    screen.blit(ITEMS[pickup.sign.id[0]], (pickup.x, pickup.y))


def draw_laser(screen, laser):
    if LASER_IMG is None:
        pygame.draw.rect(screen, RED, [laser.x, laser.y, laser.get_width(), laser.get_height()])
    else:
        global laser_offset, the_range, the_other_range, ticks, empty_laser
        graphical_laser = pygame.Surface((laser.width, laser.height)).convert_alpha()

        if not ticks % 200:
            random.shuffle(the_range)
            ticks %= 200

        if not ticks % 15:
            random.shuffle(the_other_range)

        for laser_index in the_range:
            graphical_laser.blit(LASER["LASER"]["AURAS"][laser_index], ((laser_offset/10 - GLOW_ORANGE.get_width() + environment.WINDOW_WIDTH), -15))
        #graphical_laser.blit(GLOW_BLUE, ((laser_offset - GLOW_ORANGE.get_width() + environment.WINDOW_WIDTH), -15))

        for laser_index in the_other_range:
            graphical_laser.blit(LASER["LASER"]["BEAMS"][laser_index], ((laser_offset - GLOW_ORANGE.get_width() + environment.WINDOW_WIDTH), -11))

        screen.blit(graphical_laser, (laser.x, laser.y))

        laser_offset += 60
        laser_offset %= GLOW_ORANGE.get_width() - environment.WINDOW_WIDTH


def draw_pewpew(screen, pewpew):
    if PEW_IMG is None:
        pygame.draw.rect(screen, RED, [pewpew.x, pewpew.y, pewpew.width, pewpew.height])
    else:
        screen.blit(PEW_IMG, (pewpew.x, pewpew.y))


def draw_score(screen, score):
    font=pygame.font.Font(None, 30)
    scoretext = font.render("Score: "+str(score), 1,(255,255,255))
    screen.blit(scoretext, (environment.WINDOW_WIDTH - 200, 5))




