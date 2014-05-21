import time
import physics as helper
from managers import score_manager
from managers import sound_manager as dj
from models.entities import Hero
from models.models import Bar
from models.mastermind import Mastermind
import enemy_wave_generator as mavericks

from queue import Queue
import engines


class GameState:
    def __init__(self):
        self.time = time.clock()
        self.hero = Hero()
        self.score = 0  # Score increments from defeating enemies and picking up rupees
        self.paused = False
        self.win = False
        self.game_over = False
        self.projectile_list = []  # List of projectiles onscreen.
        self.pickup_list = []  # List of present rupees onscreen.
        self.enemy_list = []  # List of present enemies of one wave.
        self.wave_queue = Queue()  # List used as a queue of waves
        #self.initialize_waves()  # Initialize all of the waves into the the wave queue
        #self.next_wave()  # Start First Wave
        self.hero_bar = Bar(self.hero.stats, self.hero)
        self.master = Mastermind("DYNAMIC", time.clock())
        #self.enemy_bar = Bar()

    def hpp(self):
        return self.hero.stats.current_hp/self.hero.stats.hp

    def toggle_paused(self):
        self.paused = not self.paused

    def update_pickups(self):
        for i in range(0, len(self.pickup_list)):
            collision = helper.check_collision(self.hero, self.pickup_list[i])
            self.pickup_list[i].move()
            if collision:
                dj.play_beep()
                pickup_type = self.pickup_list[i].sign.id[0]
                self.score += score_manager.calculate_score(pickup_type)  # Increment Score

                if pickup_type == "DEFENSE":
                    self.hero.stats.defense += 1

                if pickup_type == "HP":
                    if self.hpp() < 0.8:
                        self.hero.stats.current_hp += 20
                    else:
                        self.hero.stats.current_hp = 100
                    self.update_hero_bar()

                if pickup_type == "LASER":
                    self.hero.equip_laser()

                del self.pickup_list[i]
                break

    def update_pews(self):
        for pew in range(len(self.projectile_list)):
            if self.projectile_list[pew].is_out_of_screen():
                del self.projectile_list[pew]
                break
        for pew in self.projectile_list:
            pew.move()

    def hero_fire(self):
        pew = self.hero.fire_bullet()
        self.projectile_list.append(pew)

    def update_enemies(self):
        for enemy_index in range(len(self.enemy_list)):
            self.enemy_list[enemy_index].update_bar()
            for projectile_index in range(len(self.projectile_list)):
                if helper.check_collision(self.projectile_list[projectile_index], self.enemy_list[enemy_index]):
                    if self.enemy_list[enemy_index].sign.id[0] != "GHOST":
                        self.score += 100
                        self.enemy_list[enemy_index].get_hit_by(self.projectile_list[projectile_index])
                        del self.projectile_list[projectile_index]
                    break

        for enemy_index in range(len(self.enemy_list)):
            if not self.enemy_list[enemy_index].alive:
                if self.master.ask_if_drop(self.hero.stats.current_hp/self.hero.stats.hp):
                    drop_signature = ["PICKUP", [self.master.determine_drop(self.hpp())]]
                    self.pickup_list.append(self.enemy_list[enemy_index].drop(drop_signature))
                del self.enemy_list[enemy_index]
                break

        for enemy_index in range(len(self.enemy_list)):
            if self.enemy_list[enemy_index].right < 0:
                del self.enemy_list[enemy_index]
                self.hero.stats.attack += 1
                break

        # For the laser detection
        for enemy_index in range(len(self.enemy_list)):
            if self.hero.is_firing_laser:
                if helper.check_collision(self.enemy_list[enemy_index], self.hero.laser):
                    if self.master.ask_if_drop(self.hero.stats.current_hp/self.hero.stats.hp):
                        drop_signature = ["PICKUP", [self.master.determine_drop(self.hpp())]]
                        self.pickup_list.append(self.enemy_list[enemy_index].drop(drop_signature))
                    self.score += 300
                    del self.enemy_list[enemy_index]
                    self.hero.stats.attack += 1
                    break

        for enemy in self.enemy_list:
            enemy.move()
            engines.siny(enemy)

        if len(self.enemy_list) == 0:
            print "Less than two enemies left"
            self.next_wave()

    def initialize_waves(self):
        w = self.master.get_weight()
        wave_1 = mavericks.generate_inverse_v_shaped_wave(w)
        wave_2 = mavericks.generate_diagonal_wave_1(w)
        wave_3 = mavericks.generate_diagonal_wave_2(w)
        wave_4 = mavericks.generate_vertical_wave(w)
        wave_5 = mavericks.generate_vertical_wave(w)
        wave_6 = mavericks.generate_diagonal_wave_2(w)
        wave_7 = mavericks.generate_diagonal_wave_1(w)
        wave_8 = mavericks.generate_inverse_v_shaped_wave(w)
        self.wave_queue.enqueue(wave_1)
        self.wave_queue.enqueue(wave_2)
        self.wave_queue.enqueue(wave_3)
        self.wave_queue.enqueue(wave_4)
        self.wave_queue.enqueue(wave_5)
        self.wave_queue.enqueue(wave_6)
        self.wave_queue.enqueue(wave_7)
        self.wave_queue.enqueue(wave_8)

    def next_wave(self):
        print "Next wave called"
        if self.wave_queue.size > 1:
            self.enemy_list = self.enemy_list + self.wave_queue.dequeue()
        else:
            print "Initializing waves again"
            self.initialize_waves()

    def update_hero_bar(self):
        self.hero_bar.update(self.hero.stats)

