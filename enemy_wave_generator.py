#enemy_wave_generator.py
# Enemy Wave Generator
import environment as settings
from models.enemies import Waddle_Dee

def generate_vertical_wave():
    wave = []
    for i in range(5):
        new_enemy = Waddle_Dee(settings.WINDOW_WIDTH + 100, i * settings.WINDOW_HEIGHT/5 + 10)
        wave.append(new_enemy)
    print wave
    return wave

def generate_diagonal_wave_1():
    wave = []
    for i in range(7):
        new_enemy = Waddle_Dee(settings.WINDOW_WIDTH + 100* (i+1), settings.WINDOW_HEIGHT - 40 * (i+1))
        wave.append(new_enemy)
    print wave
    return wave

def generate_diagonal_wave_2():
    wave = []
    for i in range(7):
        new_enemy = Waddle_Dee(settings.WINDOW_WIDTH + 100* (i+1), 10 + (40 * i))
        wave.append(new_enemy)
    print wave
    return wave

def generate_v_shaped_wave():
    wave = []
    wave.append(Waddle_Dee(settings.WINDOW_WIDTH + 100, settings.WINDOW_HEIGHT/2 + 20))
    wave.append(Waddle_Dee(settings.WINDOW_WIDTH + 200, settings.WINDOW_HEIGHT/2 + 50))
    wave.append(Waddle_Dee(settings.WINDOW_WIDTH + 200, settings.WINDOW_HEIGHT/2 - 50))
    wave.append(Waddle_Dee(settings.WINDOW_WIDTH + 300, settings.WINDOW_HEIGHT/2 + 100))
    wave.append(Waddle_Dee(settings.WINDOW_WIDTH + 300, settings.WINDOW_HEIGHT/2 - 100))
    print wave
    return wave

def generate_inverse_v_shaped_wave():
    wave = []
    wave.append(Waddle_Dee(settings.WINDOW_WIDTH + 300, settings.WINDOW_HEIGHT/2 + 20))
    wave.append(Waddle_Dee(settings.WINDOW_WIDTH + 200, settings.WINDOW_HEIGHT/2 + 50))
    wave.append(Waddle_Dee(settings.WINDOW_WIDTH + 200, settings.WINDOW_HEIGHT/2 - 50))
    wave.append(Waddle_Dee(settings.WINDOW_WIDTH + 100, settings.WINDOW_HEIGHT/2 + 100))
    wave.append(Waddle_Dee(settings.WINDOW_WIDTH + 100, settings.WINDOW_HEIGHT/2 - 100))
    print wave
    return wave




