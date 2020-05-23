#!/usr/bin/env Python3

# Start writing code for Koło Naukowe and build first 2D game :D

import pygame
from pygame.locals import *
from grid import *
import player

pygame.init()

screen_width = TILESIZE*MAPHEIGHT
screen_height = TILESIZE*MAPWIDTH

pygame.display.set_caption("Pokemon")

PLAYER = player.Player()

# RENDER GAME GRID
for row in range(MAPHEIGHT):
    for column in range(MAPWIDTH):
        window.blit(TEXTURES[GRID[row][column]], (column*TILESIZE, row*TILESIZE))
        # Dorzucić listę koordinatsów gdzie może się bohater przemieścić


run = True
while(run):
    pygame.time.delay(60)


    # Events are moves of a player
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # DRUGA WERSJA TO Z MOŻLIWYMI RUCHAMI A NIE ZABRONIONYMI

    velocity = PLAYER.VELOCITY
    x = PLAYER.POS[0]
    y = PLAYER.POS[1]

    #Basic moves
    if keys[pygame.K_LEFT] and x > 0:
        # ABS potrzebny bo macierz może zczytywac z ujemnych wartości
        if GRID[y//TILESIZE][abs(x//TILESIZE - 1)] is not WATER: # BLOKADA PRZED WEJŚĆIEM NA WODE
            x -= PLAYER.VELOCITY

    if keys[pygame.K_RIGHT] and x < 1280 - TILESIZE:
        if GRID[y//TILESIZE][x//TILESIZE + 1] is not WATER:  # BLOKADA PRZED WEJŚĆIEM NA WODE
            x += PLAYER.VELOCITY

    if keys[pygame.K_DOWN] and y < 640 - TILESIZE:
        if GRID[y//TILESIZE + 1][x//TILESIZE] is not WATER:  # BLOKADA PRZED WEJŚĆIEM NA WODE
            y += PLAYER.VELOCITY

    if keys[pygame.K_UP] and y > 0:
        if GRID[abs(y//TILESIZE - 1)][x//TILESIZE] is not WATER:  # BLOKADA PRZED WEJŚĆIEM NA WODE
            y -= PLAYER.VELOCITY

    PLAYER.POS[0] = x
    PLAYER.POS[1] = y

    window.fill((0,0,0))

    # RENDER GAME GRID
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            window.blit(TEXTURES[GRID[row][column]], (column*TILESIZE, row*TILESIZE))
   
    window.blit(PLAYER.SPRITE,PLAYER.POS)
    pygame.display.update()


pygame.quit()   # Zamkmnięcie programu z kodem 0