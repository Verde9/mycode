#!/usr/bin/python3

import random
import time

class Boss: 
    def __init__ (self):
        self.health = 100

    def decrease_health(self):
        number = random.randrange(15, 30) 
        self.health = self.get_health() - number

    def get_health(self):
        if self.health > 0:
            return self.health
        else:
            return 0          

    def bossDance(nothing, player, currentEnemy):
        bd_dance_moves = ["Dictator", "Showoff", "Cabbage Patch",]
        number = random.randrange(0,4)
        if number == 0:
            print(f"The {currentEnemy} hit you with a {bd_dance_moves[0]}")
            print()
            time.sleep(1.5)
            player.boss_decrease_health()
            print(f"Soulsteppers current health is {player.get_health()}")
            print()
        elif number == 1:
            print(f"The {currentEnemy} hit you with a {bd_dance_moves[1]}")
            print()
            time.sleep(1.5) 
            player.boss_decrease_health()
            print(f"Soulsteppers current health is {player.get_health()}")
            print()
        elif number == 2:
            print(f"The {currentEnemy} hit you with a {bd_dance_moves[2]}")
            print()
            time.sleep(1.5) 
            player.boss_decrease_health()
            print(f"Soulsteppers current health is {player.get_health()}")
            print()
        elif number == 3:
            print(f"The {currentEnemy} tried hit you with a move but missed!")          