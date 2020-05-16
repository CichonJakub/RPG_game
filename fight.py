import random
from time import sleep

# call worrior
""" spis akronimów
hp -healt points
ad - attack damage
ap - ability power
arm - armor
mr - magic resist
"""


class Worrior():
    def __init__(self, name='xyz', hp=0, ad=0, arm=0):
        self.name = name
        self.hp = hp
        self.ad = ad
        self.arm = arm

    def attack(self):
        return random.randint(0, self.ad)

    def defence(self):
        return random.randint(0, self.arm)

    def lost_hp(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            print(f"{self.name} has been slain")

    def is_alive(self):
        if self.hp <= 0:
            return False
        else:
            return True

    # wypisywanie imion, przeładowanie funkcji, jak print(objekt) to wyswietli sie tylko imie
    def __str__(self):
        return self.name


def fight(hero, monster):
    round_num = 1

    while hero.is_alive() and monster.is_alive():  # zwraca true tylko kiedy oba warunki sa prawdziwe => jeden umiera i loop sie konczy
        print(f"It is: {round_num} round!")
        show_stats(hero, monster)

        if round_num % 2 == 1:
            duel(hero, monster)  # 1 parametr atakuje 2
        else:
            duel(monster, hero)
        print('\n')

        sleep(2)
        round_num += 1

    if hero.is_alive():
        print('Hero won')
    else:
        print('Monster won')


def duel(x, y):
    print(f'{x} has attaced {y}')
    dmg = x.attack() - y.defence()
    if dmg < 0:
        dmg = 0
    print(f'{x} lost {dmg} health point(s)')
    x.lost_hp(dmg)


def show_stats(x, y):
    for i in (x, y):
        print(f"{i} has {i.hp} health point(s)")


hero1 = Worrior('Knight', random.randint(100, 300), random.randint(50, 100), random.randint(5, 10))
monster1 = Worrior('Demogorgon', random.randint(100, 300), random.randint(50, 100), random.randint(5, 10))

fight(hero1, monster1)
