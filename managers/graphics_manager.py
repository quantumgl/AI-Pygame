#Graphics Manager
# The class that manages the drawing of all objects in the game.

import pygame, environment

# Colors!!!
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# Images		
BACKGROUND = pygame.image.load('img/cloud background.png')
HERO_IMG = pygame.image.load('img/hero and goatee.png')
RUPEE_IMG = pygame.image.load('img/item thingie.png')
ENEMY_IMG = pygame.image.load('img/enemy navi.png')
LASER_IMG = pygame.image.load('img/laser.png')
PEW_IMG = pygame.image.load('img/pew.png')


"""
Handles all the drawing of the Actor instance.
-> screen is the Surface object which the Actor will be drawn on
"""
def draw_background(screen):
    if BACKGROUND == None:
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
        screen.blit(ENEMY_IMG, (enemy.x, enemy.y))


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






