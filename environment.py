#settings.py
#
# All of the additional info needed to initialize the game.
# 
import pygame
pygame.init()

#CONSTANTS
WINDOW_WIDTH = 1366
WINDOW_HEIGHT = 768
WINDOW_SIZE = [WINDOW_WIDTH, WINDOW_HEIGHT]
DISPLAY_SURFACE = pygame.display.set_mode(WINDOW_SIZE, pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)
#DISPLAY_SURFACE = pygame.display.set_mode(WINDOW_SIZE)

#CLOCK
FPS = 60
CLOCK = pygame.time.Clock()

# Paused
FONT = pygame.font.Font('freesansbold.ttf',50)
PAUSED_TEXT = FONT.render('PAUSED', False, (255,255,255,0))
GAME_OVER_TEXT = FONT.render('GAME OVER', False, (255,255,255,0))
WIN_TEXT = FONT.render('CONGRATULATIONS!', False, (255,255,255,0))

PROMPT_TEXT = FONT.render('Retry (y/n)', False, (255,255,255,0))

# Boundary
BOUNDARY = pygame.Rect(0, 0, WINDOW_WIDTH/2, WINDOW_HEIGHT)