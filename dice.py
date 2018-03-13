from random import randint

class Die:
    def __init__(self, n_faces=6):
        self.faces = 6

    def roll(self):
        return randint(1,n_faces)

class Dice:
    def __init__(self, die_list):
        self.die_list = die_list

    def roll(self):
        rolls = []
        for die in self.die_list:
            rolls.append(die.roll())
        return rolls, sum(rolls)
