#!/usr/bin/python3

import random

class Soulstepper: 
    def __init__ (self):
        self.health = 100
        

    def decrease_health(self):
        number = random.randrange(5, 15)
        self.health = self.get_health() - number  

    def boss_decrease_health(self):
        number = random.randrange(15, 25)
        self.health = self.get_health() - number        

    def get_health(self):
        if self.health > 0:
            return self.health
        else:
            return 0 

    def increase_health(self):
        self.health = self.get_health() + 40


    


      