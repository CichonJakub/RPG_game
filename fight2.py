import random
from time import sleep
import pygame

# call worrior
from pip._vendor.distlib.compat import raw_input

""" spis akronimów
hp -healt points
ad - attack damage
ap - ability power
arm - armor
mr - magic resist
pa -  points (of) action // cos ala mana do silnyhc ciosów
"""
pygame.init()

class Worrior():
    def __init__(self, name='xyz', hp=0, ad=0, arm=0, pa=10):
        self.name = name
        self.hp = hp
        self.ad = ad
        self.arm = arm
        self.pa = pa

    def attack(self):
        return random.randint(min(10, self.ad), max(10, self.ad))

    def defence(self):
        return random.randint(min(10, self.arm), max(10, self.arm))

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
            duel2(hero, monster)  # 1 parametr atakuje 2
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
    print(f'{y} lost {dmg} health point(s)')
    y.lost_hp(dmg)


def duel2(x, y):
    print(f'{x} has attaced {y}')
    waiting = True
    while waiting:
        attack = raw_input("choose attack type: ")
        print(attack)
        if attack == '1':
            dmg = x.attack() - y.defence()
            if dmg < 0:
                dmg = 0
            x.pa += 2
            y.lost_hp(dmg)
            print(f'{y} lost {dmg} health point(s)')
            waiting = False

        if attack == '2':
            if x.pa >= 5:
                dmg = 2 * (x.attack() - y.defence())
                if dmg < 0:
                    dmg = 0
                x.pa -= 5
                y.lost_hp(dmg)
                print(f'{y} lost {dmg} health point(s)')
                waiting = False
            else:
                print(f"You don't have enough PA to do strong attack, now you have {x.pa} PA")


def show_stats(x, y):
    for i in (x, y):
        print(f"{i} has {i.hp} health point(s)")


hero1 = Worrior('Knight', random.randint(100, 300), random.randint(50, 100), random.randint(5, 10))
monster1 = Worrior('Demogorgon', random.randint(100, 300), random.randint(50, 100), random.randint(5, 10))

fight(hero1, monster1)
