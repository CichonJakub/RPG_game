import pygame
import pygame_gui
import sys

from pygame.locals import *

pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((1280, 720), 0, 32)

background = pygame.Surface((1280, 720))
background.fill(pygame.Color('#000000'))


manager = pygame_gui.UIManager((1280, 720))


hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 100), (200, 50)), text='Create Your Hero', manager=manager)

click = False
#background = (43, 45, 56)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 128, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)



clock = pygame.time.Clock()
is_running = True

def main_menu():
    while True:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == hello_button:
                        print('Hello Word from GUI :)))))')
                        hero()

            manager.process_events(event)

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)

        pygame.display.update()


def hero():
    background2 = pygame.Surface((1280, 720))
    background2.fill(pygame.Color('#FFFFFF'))


    manager2 = pygame_gui.UIManager((1280, 720))
    hello_button2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 300), (200, 50)),
                                                 text='loooool', manager=manager2)
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
        # window_surface.fill(white)
        #make_text('Tworzenie postaci', font, black, screen, 20, 20)
        mx, my = pygame.mouse.get_pos()

        #strength --------------------
        button_strength_add = pygame.Rect(200, 100, 50, 50)
        button_strength_reduce = pygame.Rect(300, 100, 50, 50)

        #make_text(f'Twojr punkty siły: {strength}', font, black, screen, 400, 100)

        if button_strength_add.collidepoint((mx, my)):
            if click:
                if available_points > 0:
                    available_points -= 1
                    strength += 1

        if button_strength_reduce.collidepoint((mx, my)):
            if click:
                if strength > 0:
                    strength -= 1
                    available_points += 1

        # #agility-----------------------
        # button_agility_add = pygame.Rect(200, 200, 50, 50)
        # button_agility_reduce = pygame.Rect(300, 200, 50, 50)
        #
        # make_text(f'Twojr punkty zrecznosci: {agility}', font, black, screen, 400, 200)
        #
        # if button_agility_add.collidepoint((mx, my)):
        #     if click:
        #         if available_points > 0:
        #             available_points -= 1
        #             agility += 1
        #
        # if button_agility_reduce.collidepoint((mx, my)):
        #     if click:
        #         if agility > 0:
        #             agility -= 1
        #             available_points += 1
        #
        # #intelligence ----------------------
        # button_intelligence_add = pygame.Rect(200, 300, 50, 50)
        # button_intelligence_reduce = pygame.Rect(300, 300, 50, 50)
        #
        # make_text(f'Twojr punkty inteligencji: {intelligence}', font, black, screen, 400, 300)
        #
        # if button_intelligence_add.collidepoint((mx, my)):
        #     if click:
        #         if available_points > 0:
        #             available_points -= 1
        #             intelligence += 1
        #
        # if button_intelligence_reduce.collidepoint((mx, my)):
        #     if click:
        #         if intelligence > 0:
        #             intelligence -= 1
        #             available_points += 1
        #
        # #endurance ----------------------
        # button_endurance_add = pygame.Rect(200, 400, 50, 50)
        # button_endurance_reduce = pygame.Rect(300, 400, 50, 50)
        #
        # make_text(f'Twojr punkty wytrzymalosci: {endurance}', font, black, screen, 400, 400)
        #
        # if button_endurance_add.collidepoint((mx, my)):
        #     if click:
        #         if available_points > 0:
        #             available_points -= 1
        #             endurance += 1
        #
        # if button_endurance_reduce.collidepoint((mx, my)):
        #     if click:
        #         if endurance > 0:
        #             endurance -= 1
        #             available_points += 1
        #
        #
        # #luck ----------------------
        # button_luck_add = pygame.Rect(200, 500, 50, 50)
        # button_luck_reduce = pygame.Rect(300, 500, 50, 50)
        #
        # make_text(f'Twojr punkty szczęścia: {luck}', font, black, screen, 400, 500)
        #
        # if button_luck_add.collidepoint((mx, my)):
        #     if click:
        #         if available_points > 0:
        #             available_points -= 1
        #             luck += 1
        #
        # if button_luck_reduce.collidepoint((mx, my)):
        #     if click:
        #         if luck > 0:
        #             luck -= 1
        #             available_points += 1
        #
        # #charisma ----------------------
        # button_charisma_add = pygame.Rect(200, 600, 50, 50)
        # button_charisma_reduce = pygame.Rect(300, 600, 50, 50)
        #
        # make_text(f'Twojr punkty charyzmy: {charisma}', font, black, screen, 400, 600)
        #
        # if button_charisma_add.collidepoint((mx, my)):
        #     if click:
        #         if available_points > 0:
        #             available_points -= 1
        #             charisma += 1
        #
        # if button_charisma_reduce.collidepoint((mx, my)):
        #     if click:
        #         if charisma > 0:
        #             charisma -= 1
        #             available_points += 1
        #
        #
        #
        # # submit
        # button_submit = pygame.Rect(800, 500, 600, 50)
        # make_text(f'Wcisnij ten przycisk by zapisac postac', font, black, screen, 800, 400)
        #
        # if button_submit.collidepoint((mx, my)):
        #     if click:
        #         if available_points == 0:
        #             note = open('postacie.txt', 'a')
        #             note.write(f'strength:{strength};agility:{agility};intelligence:{intelligence};endurance:{endurance};luck:{luck};charisma:{charisma}\n')
        #             note.close()
        #             #mp = Character(sxdasdasdasd)
        #             # dodac do tablicy

        #generating buttons ------------
        pygame.draw.rect(window_surface, green, button_strength_add)
        pygame.draw.rect(window_surface, red, button_strength_reduce)
        # pygame.draw.rect(screen, green, button_agility_add)
        # pygame.draw.rect(screen, red, button_agility_reduce)
        # pygame.draw.rect(screen, green, button_intelligence_add)
        # pygame.draw.rect(screen, red, button_intelligence_reduce)
        # pygame.draw.rect(screen, green, button_endurance_add)
        # pygame.draw.rect(screen, red, button_endurance_reduce)
        # pygame.draw.rect(screen, green, button_luck_add)
        # pygame.draw.rect(screen, red, button_luck_reduce)
        # pygame.draw.rect(screen, green, button_charisma_add)
        # pygame.draw.rect(screen, red, button_charisma_reduce)
        # pygame.draw.rect(screen, yellow, button_submit)
        click = False

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

        window_surface.blit(background2, (0, 0))
        manager2.draw_ui(window_surface)
        # pygame.display.update()
        # mainClock.tick(60)


main_menu()