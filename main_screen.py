import pygame
import sys
from settings import *


mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Game')
screen = pygame.display.set_mode((1280, 720), 0, 32)

font = pygame.font.SysFont(None, 20)


def make_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False
background = (43, 45, 56)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 128, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)

def main_manu():
    while True:

        screen.fill(background)
        make_text('Menu głowne', font, black, screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        # left, top, width, height
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        make_text('Create a Hero', font, black, screen, 55, 110)

        if button_1.collidepoint((mx, my)):
            if click:
                hero()

        if button_2.collidepoint((mx, my)):
            if click:
                hero2()

        pygame.draw.rect(screen, green, button_1)
        pygame.draw.rect(screen, green, button_2)

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def hero():
    global click
    running = True
    available_points = 20
    strength = 0
    agility = 0
    intelligence = 0
    endurance = 0
    luck = 0
    charisma = 0

    # strength, agility, intelligence, endurance, luck, charisma = 0

    while running:
        screen.fill(darkgray)
        make_text('Tworzenie postaci', font, black, screen, 20, 20)
        mx, my = pygame.mouse.get_pos()

        screen.blit(minus2, (200, 100))
        screen.blit(plus2, (300, 100))

        #strength --------------------
        # button_strength_add = pygame.Rect(200, 100, 50, 50)
        # button_strength_reduce = pygame.Rect(300, 100, 50, 50)
        #
        # make_text(f'Twojr punkty siły: {strength}', font, black, screen, 400, 100)
        #
        # if button_strength_add.collidepoint((mx, my)):
        #     if click:
        #         if available_points > 0:
        #             available_points -= 1
        #             strength += 1
        #
        # if button_strength_reduce.collidepoint((mx, my)):
        #     if click:
        #         if strength > 0:
        #             strength -= 1
        #             available_points += 1

        #agility-----------------------
        button_agility_add = pygame.Rect(200, 200, 76, 76)
        button_agility_reduce = pygame.Rect(300, 200, 76, 76)

        make_text(f'Twojr punkty zrecznosci: {agility}', font, black, screen, 400, 200)

        if button_agility_add.collidepoint((mx, my)):
            if click:
                if available_points > 0:
                    available_points -= 1
                    agility += 1

        if button_agility_reduce.collidepoint((mx, my)):
            if click:
                if agility > 0:
                    agility -= 1
                    available_points += 1

        #intelligence ----------------------
        button_intelligence_add = pygame.Rect(200, 300, 50, 50)
        button_intelligence_reduce = pygame.Rect(300, 300, 50, 50)

        make_text(f'Twojr punkty inteligencji: {intelligence}', font, black, screen, 400, 300)

        if button_intelligence_add.collidepoint((mx, my)):
            if click:
                if available_points > 0:
                    available_points -= 1
                    intelligence += 1

        if button_intelligence_reduce.collidepoint((mx, my)):
            if click:
                if intelligence > 0:
                    intelligence -= 1
                    available_points += 1

        #endurance ----------------------
        button_endurance_add = pygame.Rect(200, 400, 50, 50)
        button_endurance_reduce = pygame.Rect(300, 400, 50, 50)

        make_text(f'Twojr punkty wytrzymalosci: {endurance}', font, black, screen, 400, 400)

        if button_endurance_add.collidepoint((mx, my)):
            if click:
                if available_points > 0:
                    available_points -= 1
                    endurance += 1

        if button_endurance_reduce.collidepoint((mx, my)):
            if click:
                if endurance > 0:
                    endurance -= 1
                    available_points += 1


        #luck ----------------------
        button_luck_add = pygame.Rect(200, 500, 50, 50)
        button_luck_reduce = pygame.Rect(300, 500, 50, 50)

        make_text(f'Twojr punkty szczęścia: {luck}', font, black, screen, 400, 500)

        if button_luck_add.collidepoint((mx, my)):
            if click:
                if available_points > 0:
                    available_points -= 1
                    luck += 1

        if button_luck_reduce.collidepoint((mx, my)):
            if click:
                if luck > 0:
                    luck -= 1
                    available_points += 1

        #charisma ----------------------
        button_charisma_add = pygame.Rect(200, 600, 50, 50)
        button_charisma_reduce = pygame.Rect(300, 600, 50, 50)

        make_text(f'Twojr punkty charyzmy: {charisma}', font, black, screen, 400, 600)

        if button_charisma_add.collidepoint((mx, my)):
            if click:
                if available_points > 0:
                    available_points -= 1
                    charisma += 1

        if button_charisma_reduce.collidepoint((mx, my)):
            if click:
                if charisma > 0:
                    charisma -= 1
                    available_points += 1



        # submit
        button_submit = pygame.Rect(800, 500, 600, 50)
        make_text(f'Wcisnij ten przycisk by zapisac postac', font, black, screen, 800, 400)

        if button_submit.collidepoint((mx, my)):
            if click:
                if available_points == 0:
                    note = open('postacie.txt', 'a')
                    note.write(f'strength:{strength};agility:{agility};intelligence:{intelligence};endurance:{endurance};luck:{luck};charisma:{charisma}\n')
                    note.close()
                    #mp = Character(sxdasdasdasd)
                    # dodac do tablicy

        #generating buttons ------------
        # pygame.draw.rect(screen, green, button_strength_add)
        # pygame.draw.rect(screen, red, button_strength_reduce)
        pygame.draw.rect(screen, aliceblue, button_agility_add)
        pygame.draw.rect(screen, aliceblue, button_agility_reduce)
        pygame.draw.rect(screen, green, button_intelligence_add)
        pygame.draw.rect(screen, red, button_intelligence_reduce)
        pygame.draw.rect(screen, green, button_endurance_add)
        pygame.draw.rect(screen, red, button_endurance_reduce)
        pygame.draw.rect(screen, green, button_luck_add)
        pygame.draw.rect(screen, red, button_luck_reduce)
        pygame.draw.rect(screen, green, button_charisma_add)
        pygame.draw.rect(screen, red, button_charisma_reduce)
        pygame.draw.rect(screen, yellow, button_submit)
        click = False

        screen.blit(minus2, button_agility_add)
        screen.blit(plus2, button_agility_reduce)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


        pygame.display.update()
        mainClock.tick(60)


def hero2():
    running = True
    while running:
        screen.fill(white)
        make_text('Tworzenie postaci 2', font, black, screen, 20, 20)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


class Character():
    def __init__(self, nick='xyz', strength=0, agility=0, intelligence=0, endurance=0, luck=0, charisma=0):
        self.agility = agility
        self.nick = nick
        self.strength = strength
        self.intelligence = intelligence
        self.endurance = endurance
        self.luck = luck
        self.charisma = charisma


main_manu()
