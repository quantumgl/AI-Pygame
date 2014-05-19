#enemy_wave_generator.py
# Enemy Wave Generator
import random
import environment as settings
from models.enemies import Waddle_Dee

ENEMY_CLASSES = [
    "TANK", "SWARM", "NORMAL", "BOSS", "SCATTER", "SPEED", "GHOST", "MIMIC"
]


def generate_vertical_wave():
    wave = []
    for i in range(5):
        enemy_type = ["ORB", [ENEMY_CLASSES[random.randint(0, 6)], None]]
        new_enemy = Waddle_Dee(settings.WINDOW_WIDTH + 200, i * settings.WINDOW_HEIGHT/5 + 10, enemy_type)
        wave.append(new_enemy)
    #print wave
    return wave


def generate_diagonal_wave_1():
    wave = []
    for i in range(7):
        enemy_type = ["ORB", [ENEMY_CLASSES[random.randint(0, 6)], None]]
        new_enemy = Waddle_Dee(settings.WINDOW_WIDTH + 100* (i+2), settings.WINDOW_HEIGHT - 40 * (i+1), enemy_type)
        wave.append(new_enemy)
    #print wave
    return wave


def generate_diagonal_wave_2():
    wave = []
    for i in range(7):
        enemy_type = ["ORB", [ENEMY_CLASSES[random.randint(0, 6)], None]]
        new_enemy = Waddle_Dee(settings.WINDOW_WIDTH + 100* (i+2), 10 + (40 * i), enemy_type)
        wave.append(new_enemy)
    #print wave
    return wave


def generate_v_shaped_wave():
    wave = []
    enemy_type = ["ORB", [ENEMY_CLASSES[random.randint(0, 6)], None]]
    wave.append(Waddle_Dee(settings.WINDOW_WIDTH + 100, settings.WINDOW_HEIGHT/2 + 20, enemy_type))
    wave.append(Waddle_Dee(settings.WINDOW_WIDTH + 400, settings.WINDOW_HEIGHT/2 + 50, enemy_type))
    wave.append(Waddle_Dee(settings.WINDOW_WIDTH + 400, settings.WINDOW_HEIGHT/2 - 50, enemy_type))
    wave.append(Waddle_Dee(settings.WINDOW_WIDTH + 800, settings.WINDOW_HEIGHT/2 + 100, enemy_type))
    wave.append(Waddle_Dee(settings.WINDOW_WIDTH + 800, settings.WINDOW_HEIGHT/2 - 100, enemy_type))
    #print wave
    return wave


def generate_inverse_v_shaped_wave():
    wave = []
    enemy_type = ["ORB", [ENEMY_CLASSES[random.randint(0, 6)], None]]
    wave.append(Waddle_Dee(settings.WINDOW_WIDTH + 300, settings.WINDOW_HEIGHT/2 + 20, enemy_type))
    wave.append(Waddle_Dee(settings.WINDOW_WIDTH + 200, settings.WINDOW_HEIGHT/2 + 50, enemy_type))
    wave.append(Waddle_Dee(settings.WINDOW_WIDTH + 200, settings.WINDOW_HEIGHT/2 - 50, enemy_type))
    wave.append(Waddle_Dee(settings.WINDOW_WIDTH + 100, settings.WINDOW_HEIGHT/2 + 100, enemy_type))
    wave.append(Waddle_Dee(settings.WINDOW_WIDTH + 100, settings.WINDOW_HEIGHT/2 - 100, enemy_type))
    #print wave
    return wave




