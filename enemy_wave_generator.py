#enemy_wave_generator.py
# Enemy Wave Generator
import random
import time
import environment as settings
from models.enemies import Waddle_Dee

ENEMY_CLASSES = [
    "TANK", "SWARM", "NORMAL", "BOSS", "SCATTER", "SPEED", "GHOST", "MIMIC"
]


def generate_vertical_wave(w=1.0, enemy_class="NORMAL", wing_class="GREY", stache_class="HITLER"):
    enemy_type = ["ORB", [enemy_class, wing_class, stache_class]]
    wave = []
    for i in range(5):
        #enemy_type = ["ORB", [ENEMY_CLASSES[random.randint(0, 7)], None]]
        new_enemy = Waddle_Dee(settings.WINDOW_WIDTH + 200, i * settings.WINDOW_HEIGHT/5 + 10, enemy_type, w)
        wave.append(new_enemy)
    #print wave
    return wave


def generate_diagonal_wave_1(w=1.0, enemy_class="NORMAL", wing_class="GREY", stache_class="HITLER"):
    enemy_type = ["ORB", [enemy_class, wing_class, stache_class]]
    wave = []
    for i in range(7):
        #enemy_type = ["ORB", [ENEMY_CLASSES[random.randint(0, 7)], None]]
        new_enemy = Waddle_Dee(settings.WINDOW_WIDTH + 100* (i+2), settings.WINDOW_HEIGHT - 40 * (i+1), enemy_type, w)
        wave.append(new_enemy)
    #print wave
    return wave


def generate_diagonal_wave_2(w=1.0, enemy_class="NORMAL", wing_class="GREY", stache_class="HITLER"):
    enemy_type = ["ORB", [enemy_class, wing_class, stache_class]]
    wave = []
    for i in range(7):
        #enemy_type = ["ORB", [ENEMY_CLASSES[random.randint(0, 7)], None]]
        new_enemy = Waddle_Dee(settings.WINDOW_WIDTH + 100* (i+2), 10 + (40 * i), enemy_type, w)
        wave.append(new_enemy)
    #print wave
    return wave


def generate_v_shaped_wave(w=1.0, enemy_class="NORMAL", wing_class="GREY", stache_class="HITLER"):
    enemy_type = ["ORB", [enemy_class, wing_class, stache_class]]
    wave = []
    #enemy_type = ["ORB", [ENEMY_CLASSES[random.randint(0, 7)], None]]
    wave.append(Waddle_Dee(settings.WINDOW_WIDTH + 100, settings.WINDOW_HEIGHT/2 + 20, enemy_type, w))
    wave.append(Waddle_Dee(settings.WINDOW_WIDTH + 400, settings.WINDOW_HEIGHT/2 + 50, enemy_type, w))
    wave.append(Waddle_Dee(settings.WINDOW_WIDTH + 400, settings.WINDOW_HEIGHT/2 - 50, enemy_type, w))
    wave.append(Waddle_Dee(settings.WINDOW_WIDTH + 800, settings.WINDOW_HEIGHT/2 + 100, enemy_type, w))
    wave.append(Waddle_Dee(settings.WINDOW_WIDTH + 800, settings.WINDOW_HEIGHT/2 - 100, enemy_type, w))
    #print wave
    return wave


def generate_inverse_v_shaped_wave(w=1.0, enemy_class="NORMAL", wing_class="GREY", stache_class="HITLER"):
    enemy_type = ["ORB", [enemy_class, wing_class, stache_class]]
    wave = []
    #enemy_type = ["ORB", [ENEMY_CLASSES[random.randint(0, 7)], None]]
    wave.append(Waddle_Dee(settings.WINDOW_WIDTH + 300, settings.WINDOW_HEIGHT/2 + 20, enemy_type, w))
    wave.append(Waddle_Dee(settings.WINDOW_WIDTH + 200, settings.WINDOW_HEIGHT/2 + 50, enemy_type, w))
    wave.append(Waddle_Dee(settings.WINDOW_WIDTH + 200, settings.WINDOW_HEIGHT/2 - 50, enemy_type, w))
    wave.append(Waddle_Dee(settings.WINDOW_WIDTH + 100, settings.WINDOW_HEIGHT/2 + 100, enemy_type, w))
    wave.append(Waddle_Dee(settings.WINDOW_WIDTH + 100, settings.WINDOW_HEIGHT/2 - 100, enemy_type, w))
    #print wave
    return wave

Patterns = [
    generate_vertical_wave,
    generate_diagonal_wave_1,
    generate_diagonal_wave_2,
    generate_v_shaped_wave,
    generate_inverse_v_shaped_wave
]


def generate_a_wave(w=1.0, enemy_class="NORMAL", wing_class="GREY", stache_class="HITLER"):
    return Patterns[random.randint(0, 4)](w, enemy_class, wing_class, stache_class)


