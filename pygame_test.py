#!/usr/bin/env Python3

# Start writing code for Koło Naukowe and build first 2D game :D

import pygame
from pygame.locals import *
#from new_grid import *
from settings import *
from map import *
import player

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption(TITLE)
        self.load_map()

    def load_map(self):
        self.GRID = Map(MAP)

    def new(self):
        # Create objects
        self.PLAYER = player.Player()

    def run(self):
        ### GAME LOOP
        self.play = True
        while self.play:
            pygame.time.delay(FPS)
            self.events()
            self.updateMap()

    def quit(self):
        # Quit game
        pygame.quit()
    
    def updateMap(self):
        # what's gonna be updated with time
        for row in range(MAPHEIGHT):
            for column in range(MAPWIDTH):
                self.window.blit( TEXTURES[self.GRID.data[row + self.GRID.vertical_move][column + self.GRID.horizontal_move]], (column*TILESIZE, row*TILESIZE) )
   
        self.window.blit(self.PLAYER.SPRITE,self.PLAYER.POS)
        #pygame.display.update()
        pygame.display.flip()


    def events(self):
        # Events on the map
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

        keys = pygame.key.get_pressed()
        x = self.PLAYER.POS[0]
        y = self.PLAYER.POS[1]

        if keys[pygame.K_LEFT] and x > 0:
        # ABS potrzebny bo macierz może zczytywac z ujemnych wartości
            if self.GRID.data[y//TILESIZE][abs(x//TILESIZE - self.GRID.horizontal_move - 1)] != 'WATER': # BLOKADA PRZED WEJŚĆIEM NA WODE
                x -= self.PLAYER.VELOCITY
                if x % TILESIZE == 0 and self.GRID.horizontal_move > self.GRID.MARGIN_LEFT:
                    self.GRID.horizontal_move -= 1
    
        if keys[pygame.K_RIGHT] and x < 1280 - TILESIZE:
            if self.GRID.data[y//TILESIZE][x//TILESIZE + self.GRID.horizontal_move + 1] != 'WATER':  # BLOKADA PRZED WEJŚĆIEM NA WODE
                x += self.PLAYER.VELOCITY
                if x % TILESIZE == 0 and self.GRID.horizontal_move < self.GRID.MARGIN_RIGHT:
                    self.GRID.horizontal_move += 1

        if keys[pygame.K_DOWN] and y < 640 - TILESIZE:
            if self.GRID.data[y//TILESIZE + self.GRID.vertical_move + 1][x//TILESIZE] != 'WATER':  # BLOKADA PRZED WEJŚĆIEM NA WODE
                y += self.PLAYER.VELOCITY
                if y % TILESIZE == 0 and self.GRID.vertical_move < self.GRID.MARGIN_BOTTOM:
                    self.GRID.vertical_move += 1

        if keys[pygame.K_UP] and y > 0:
            if self.GRID.data[abs(y//TILESIZE - self.GRID.vertical_move -1)][x//TILESIZE] != 'WATER':  # BLOKADA PRZED WEJŚĆIEM NA WODE
                y -= self.PLAYER.VELOCITY
                if y % TILESIZE == 0 and self.GRID.vertical_move > self.GRID.MARGIN_UP:
                    self.GRID.vertical_move -= 1

        self.PLAYER.POS[0] = x
        self.PLAYER.POS[1] = y

        self.window.fill((0,0,0))
        self.updateMap()

    def show_start_menu(self):
        # Show starting menu
        pass

    def show_pause_menu(self):
        # Pause game and show some menu
        pass

game = Game()
while True:
    game.new()
    game.run()