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
import time
import random
import pygame
import environment
import keyboard
import physics as helper
from managers import graphics_manager as picasso
from managers import sound_manager as dj
from gamestate import GameState
import logger

pygame.init()
#---MAIN------------------------------------------------


def main(log):
    global game_state
    while True:
        handle_input(log)
        
        if not game_state.paused:
            game_logic(log)
            draw(log)
            end_game(log)
        else:
            environment.DISPLAY_SURFACE.blit(environment.PAUSED_TEXT,(environment.WINDOW_WIDTH/2,environment.WINDOW_HEIGHT/2))
            pygame.display.update()
        #game_state.time += 1
        environment.CLOCK.tick(environment.FPS)
        #print "Score: " + str(game_state.score)


#---FUNCTIONS-------------------------------------------
#
#---PRIMARY-FUNCTIONS-----------------------------------

def handle_input(log, END_GAME = False):
    """
    Handles all external input,such as those  keyboard and mouse.
    """
    for event in pygame.event.get():

        keys = pygame.key.get_pressed()

        # Closing
        handle_quit(event)

        if keyboard.queue_prompt(event):
            game_state.next_wave()

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
            if game_state.mode == "FIXED":
                new_choice = "DYNAMIC"
            else:
                new_choice = "FIXED"
            game_state = GameState(new_choice)
            log.refresh(new_choice)
            log.first_row()
            

        # Sound Adjustment
        if keyboard.music_prompt(keys):
            dj.switch_background_music()
        if keyboard.increase_prompt(keys):
            dj.increase_volume()
        if keyboard.decrease_prompt(keys):
            dj.decrease_volume()
        
        # Shoot Laser
        if keyboard.laser_prompt(keys):
            if game_state.hero.laser_equipped:
                game_state.hero.is_firing_laser = True
                game_state.hero.fire_time = time.clock()

        # Shoot Pew
        if keyboard.pew_prompt(keys):
            if game_state.hero.ok_to_shoot():
                game_state.hero_fire()
                dj.play_pew()


        
                
def game_logic(log):
    """
    Handles all game logic,
    such as collisions, damage calculation, movement,etc.
    """
    #Hero
    location = helper.locate_in_boundary(game_state.hero, environment.BOUNDARY)
    helper.movement_manager(game_state.hero, location)
    game_state.hero.update_pos()
    game_state.hero.recharge()

    if game_state.hero.vulnerable:
        for enemy in game_state.enemy_list:
            if helper.check_collision(enemy, game_state.hero):
                game_state.hitcount += 1
                game_state.hero.get_hit_by_enemy(enemy)
                game_state.hero.knockback()
                game_state.hero.give_immunity()
                game_state.update_hero_bar()
                if game_state.hero.isdead():
                    game_state.game_over = True
                    print "GAME_OVER"  # GAME OVER - TODO
    else:
        if (time.clock() - game_state.hero.vulnerability_time) > 1.5:
            game_state.hero.take_immunity()

    # Hero - Laser
    if game_state.hero.is_firing_laser:
        if time.clock() - game_state.hero.fire_time < 6:
            game_state.hero.fire_laser()
        else:
            game_state.hero.stop_firing_laser()

    # Pews
    game_state.update_pews()
    
    # Rupees
    game_state.update_pickups()

    # Enemies and Waves
    game_state.update_enemies()

    hp_100 = game_state.hero.stats.current_hp / game_state.hero.stats.hp
    game_state.master.update(hp_100)

    log.add_row(game_state)

    
def draw(log):
    """
    Draws everything and updates the changes in the screen
    """
    screen = environment.DISPLAY_SURFACE

    picasso.draw_background(screen)

    picasso.draw_hero(screen, game_state.hero)

    for pewpew in game_state.projectile_list:
        if not pewpew.is_out_of_screen():
            picasso.draw_pewpew(screen, pewpew)

    for pickup in game_state.pickup_list:
        picasso.draw_pickup(screen, pickup)
    
    if game_state.hero.is_firing_laser:
        picasso.draw_laser(screen, game_state.hero.laser)
     
    for enemy in game_state.enemy_list:
        picasso.draw_enemy(screen, enemy)
        picasso.draw_bar(screen, enemy.bar)

    picasso.draw_bar(screen, game_state.hero_bar, hero_bar=True)

    picasso.draw_score(screen, game_state.score)

    pygame.display.update()


#End Game
def end_game(log):
    if game_state.game_over:
        surf = environment.DISPLAY_SURFACE

        picasso.draw_background(surf)
        surf.blit(environment.GAME_OVER_TEXT,(environment.WINDOW_WIDTH/4,environment.WINDOW_HEIGHT/2))
        surf.blit(environment.PROMPT_TEXT,(environment.WINDOW_WIDTH/4,environment.WINDOW_HEIGHT*(3.0/4.0)))
        pygame.display.update()

        while game_state.game_over:
            handle_input(log, game_state.game_over)

    if game_state.win:
        picasso.draw_background(surf)
        surf.blit(environment.WIN_TEXT,(environment.WINDOW_WIDTH/8,environment.WINDOW_HEIGHT/2))
        surf.blit(environment.PROMPT_TEXT,(environment.WINDOW_WIDTH/4,environment.WINDOW_HEIGHT*(3.0/4.0)))
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
    possibilities = ["FIXED", "DYNAMIC"]
    game_state = GameState(possibilities[random.randint(0, 1)])
    log = logger.Log("", game_state)
    log.first_row()
    main(log)




