__author__ = 'New'

import time
import csv


class Log():
    def __init__(self, name, gamestate):
        self.persons_name = name
        self.time = time.time()
        self.mode = gamestate.mode
        self.count = 1
        self.directory = "datos/"
        self.filename = name + str(self.count) + ".csv"
        self.fullpath = self.directory + self.filename
        self.file = open(self.fullpath, "wb")
        self.writer = csv.writer(self.file, dialect='excel')


    def refresh(self, new_choice):
        self.time = time.time()
        self.mode = new_choice
        self.count += 1
        self.filename = self.persons_name + str(self.count) + ".csv"
        self.fullpath = self.directory + self.filename
        self.file = open(self.fullpath, "wb")
        self.writer = csv.writer(self.file, dialect='excel')

    def first_row(self):
        head = [self.persons_name, self.mode]
        self.writer.writerow(head)
        values = ["WEIGHT", "CLOCK", "HP", "CURRENTHP", "DECISION", "ATTACK", "DEFENSE", "HITCOUNT", "KILLCOUNT", "SCORE"]
        self.writer.writerow(values)

    def add_row(self, gamestate):
        values = [
            gamestate.master.weight,
            time.clock() - gamestate.time,
            gamestate.hero.stats.hp,
            gamestate.hero.stats.current_hp,
            gamestate.master.decision(gamestate.hpp()),
            gamestate.hero.stats.attack,
            gamestate.hero.stats.defense,
            gamestate.hitcount,
            gamestate.killcount,
            gamestate.score
        ]
        self.writer.writerow(values)

