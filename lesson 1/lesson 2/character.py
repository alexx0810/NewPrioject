import random


class Character:
    name = ''
    health = 100
    damage = 1
    defence = 0

    def __init__(self, name='',health=100,damage=1,defence=0):
        self.name = name
        self.health = health
        self.damage = damage
        self.defence = defence

    def __str__(self):
        return f'{self.name} ==\n' \
               f'health: {self.health}\n' \
               f'damage: {self.damage}\n' \
               f'defence: {self.defence}\n'

    def roll_defence(self):
        return random.randint(0, self.defence)

    def take_damage(self, damage):
        self.health -= max(damage - self.defence, 0)

    def attack(self, target):
        target.take_damage(self.damage)