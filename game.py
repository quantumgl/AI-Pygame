# game.py
#
# This script initializes all the resources and sets up the game logic,
# to finally run the game.
# 
# Carlos N. Abreu Takemura
# Andres A. Gonzalez Lagares
# License(s): CC By 3.0
# 
# Python.org (PEP 8) Coding Style Suggestions

"""Initializes and runs the game."""

import sys
import pygame
import environment
import keyboard
import physics as helper
from managers import graphics_manager as picasso
from managers import sound_manager as dj
from gamestate import GameState

pygame.init()
#---MAIN------------------------------------------------


def main():
    global game_state
    while True:
        handle_input()
        
        if not game_state.paused:
            game_logic()
            draw()
            end_game()     
        else:
            environment.DISPLAY_SURFACE.blit(environment.PAUSED_TEXT,(environment.WINDOW_WIDTH/2,environment.WINDOW_HEIGHT/2))
            pygame.display.update()
        game_state.time += 1
        environment.CLOCK.tick(environment.FPS)
        print "Score: " + str(game_state.score)


#---FUNCTIONS-------------------------------------------
#
#---PRIMARY-FUNCTIONS-----------------------------------

def handle_input(END_GAME = False):
    """
    Handles all external input,such as those  keyboard and mouse.
    """
    for event in pygame.event.get():

        keys = pygame.key.get_pressed()

        # Closing
        handle_quit(event)
        
        # Pausing game
        if keyboard.pause_prompt(keys):
            game_state.toggle_paused()   

        # Hero's movement
        hero_dir = keyboard.movement(keys)
        game_state.hero.change_direction(hero_dir)

        #END_GAME
        global game_state
        handle_quit(event, END_GAME)
        if keyboard.restart(event, END_GAME):
            game_state = GameState()
            

        # Sound Adjustment
        if keyboard.music_prompt(keys):
            dj.switch_background_music()
        if keyboard.increase_prompt(keys):
            dj.increase_volume()
        if keyboard.decrease_prompt(keys):
            dj.decrease_volume()
        
        # Shoot Laser
        if keyboard.laser_prompt(keys):
            game_state.hero.is_firing_laser = True
        else:
            if game_state.hero.is_firing_laser:
                game_state.hero.stop_firing_laser()

        # Shoot Pew
        if keyboard.pew_prompt(keys):
            if game_state.hero.ok_to_shoot():
                game_state.hero_fire()
                dj.play_pew()
        elif not game_state.hero.ok_to_shoot():
            game_state.hero.recharge()       
        
                
def game_logic():
    """
    Handles all game logic,
    such as collisions, damage calculation, movement,etc.
    """
    #Hero
    location = helper.locate_in_boundary(game_state.hero, environment.BOUNDARY)
    helper.movement_manager(game_state.hero, location)
    game_state.hero.update_pos()

    for enemy in game_state.enemy_list:
        if helper.check_collision(enemy, game_state.hero):
            game_state.game_over = True
            print "GAME_OVER"  # GAME OVER - TODO

    # Hero - Laser
    if game_state.hero.is_firing_laser:
        game_state.hero.fire_laser()

    # Pews
    game_state.update_pews()
    
    # Rupees
    game_state.update_rupees()

    # Enemies and Waves
    game_state.update_enemies()

    
def draw():
    """
    Draws everything and updates the changes in the screen
    """
    picasso.draw_background(environment.DISPLAY_SURFACE)

    picasso.draw_hero(environment.DISPLAY_SURFACE, game_state.hero)

    for pewpew in game_state.projectile_list:
        if not pewpew.is_out_of_screen():
            picasso.draw_pewpew(environment.DISPLAY_SURFACE, pewpew)

    for rupee in game_state.rupee_list:
        picasso.draw_rupee(environment.DISPLAY_SURFACE, rupee)
    
    if game_state.hero.is_firing_laser:
        picasso.draw_laser(environment.DISPLAY_SURFACE, game_state.hero.laser)
     
    for enemy in game_state.enemy_list:
        picasso.draw_enemy(environment.DISPLAY_SURFACE, enemy)

    pygame.display.update()


#End Game
def end_game():
    if game_state.game_over:
        picasso.draw_background(environment.DISPLAY_SURFACE)
        environment.DISPLAY_SURFACE.blit(environment.GAME_OVER_TEXT,(environment.WINDOW_WIDTH/4,environment.WINDOW_HEIGHT/2))
        environment.DISPLAY_SURFACE.blit(environment.PROMPT_TEXT,(environment.WINDOW_WIDTH/4,environment.WINDOW_HEIGHT*(3.0/4.0)))
        pygame.display.update()

        while game_state.game_over:
            handle_input(game_state.game_over)

    if game_state.win:
        picasso.draw_background(environment.DISPLAY_SURFACE)
        environment.DISPLAY_SURFACE.blit(environment.WIN_TEXT,(environment.WINDOW_WIDTH/8,environment.WINDOW_HEIGHT/2))
        environment.DISPLAY_SURFACE.blit(environment.PROMPT_TEXT,(environment.WINDOW_WIDTH/4,environment.WINDOW_HEIGHT*(3.0/4.0)))
        pygame.display.update()

        while game_state.win:
            handle_input(game_state.win)


def handle_quit(event, GAME_OVER = False):
    if keyboard.escape_prompt(event, GAME_OVER):
            pygame.quit()
            sys.exit()

#---BLACK-MAGIC---

if __name__ == '__main__':
    dj.loop_background_music()
    pygame.display.set_caption("BitCuisine Experiment")
    game_state = GameState()
    main()






