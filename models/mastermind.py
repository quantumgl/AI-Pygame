__author__ = 'New'

import time
import math
import random


class Mastermind():
    def __init__(self, game_type="FIXED", instance_time=1.0):
        self.weight = 1.0
        self.game_type = game_type
        self.instance_time = instance_time

    def update(self, hp_percentage=1.0):
        if self.game_type == "FIXED":
            self.weight += 0.6

        if self.game_type == "DYNAMIC":
            if hp_percentage > 0.75:
                self.weight += 1.0
            elif hp_percentage > 0.25:
                self.weight += 0.5
            else:
                self.weight += 0.25

    def get_weight(self, hp_percentage=1.0):
        if self.game_type == "FIXED":
            return self.weight/120.0 + 5

        if self.game_type == "DYNAMIC":
            if hp_percentage > 0.75:
                return self.weight/120.0 + 5
            elif hp_percentage > 0.25:
                return self.weight*0.5/120.0 + 5
            else:
                return self.weight*0.25/120.0 + 5

    def ask_if_drop(self, hp_percentage=1.0):
        return 1/math.log(self.get_weight(hp_percentage)*2 + 5) > random.randint(0, 100)/100.0

    def determine_drop(self, hp_percentage=1.0):
        luck = random.randint(0, 100)

        if self.game_type == "FIXED":
            if luck < 50:
                return "MONEY"
            if luck < 75:
                return "DEFENSE"
            if luck < 95:
                return "HP"
            return "LASER"

        if self.game_type == "DYNAMIC":
            if hp_percentage < 0.10:
                if luck < 50:
                    return "HP"
                if luck < 75:
                    return "LASER"
                if luck < 95:
                    return "DEFENSE"
                return "MONEY"

            if hp_percentage < 0.40:
                if luck < 50:
                    return "DEFENSE"
                if luck < 75:
                    return "HP"
                if luck < 95:
                    return "LASER"
                return "MONEY"

            if hp_percentage < 0.75:
                if luck < 50:
                    return "DEFENSE"
                if luck < 75:
                    return "MONEY"
                if luck < 95:
                    return "HP"
                return "LASER"

            if hp_percentage <= 1:
                if luck < 50:
                    return "MONEY"
                if luck < 75:
                    return "DEFENSE"
                if luck < 95:
                    return "HP"
                return "LASER"




