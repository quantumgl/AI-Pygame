import pygame as pg

#Variables
background_playback = False
vol_adj = 0

#Constants
BEEP_VOLUME = 0.5
VOL_ADJUSTER = 0.20

#Load Sound
BEEP = pg.mixer.Sound('sound/beep.wav') 
MUSIC = pg.mixer.Sound('sound/ParagonX9_Chaoz-Fantasy-8-Bit.wav')
PEW = pg.mixer.Sound('sound/pew.wav')

#Manual Channels
BACKGROUND = pg.mixer.find_channel()

#Manual Adjustments
BEEP.set_volume(BEEP_VOLUME)

def loop_background_music():
    """Loops the background music"""
    global background_playback
    BACKGROUND.play(MUSIC, -1)
    background_playback = True

def switch_background_music():
    """Switch background music on or off"""
    global background_playback
    if background_playback:
        BACKGROUND.pause()
        background_playback = False
    else:
        BACKGROUND.unpause()
        background_playback = True


def change_volume(Dir, Target=BACKGROUND):
    """For sound adjustment"""
    volume = Target.get_volume()

    if Dir == "UP":
        if (volume+VOL_ADJUSTER)<=1:
            Target.set_volume(volume+VOL_ADJUSTER)
    if Dir == "DOWN":
        if (volume-VOL_ADJUSTER)>=0:
            Target.set_volume(volume-VOL_ADJUSTER)


def increase_volume(Target=BACKGROUND):
    change_volume("UP")

def decrease_volume(Target=BACKGROUND):
    change_volume("DOWN")

def play_beep():
    """Plays a beep"""
    BEEP.play()

def play_pew():
    PEW.play()
