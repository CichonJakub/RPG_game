#!/usr/bin/env Python3

# Start writing code for Koło Naukowe and build first 2D game :D

import pygame
from pygame.locals import *
import time
from settings import *
from map import *
import player
import locations
import npc
import net


class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption(TITLE)
        self.font = pygame.font.Font('freesansbold.ttf', 32) 
        server = net.Net()
        server.connectToServer()

    def load_map(self):
        self.GRID = Map(MAP)
        self.PREV_GRID = []

    def obj_on_curr_map(self):
        self.activeLoc = []
        self.activeNPC = []

        for self.location in self.LOC:
            if self.location.map == self.GRID.name:
                self.activeLoc.append(self.location)

        for self.character in self.NPC:
            if self.character.map == self.GRID.name:
                self.activeNPC.append(self.character)

    def new(self):
        # Create objects
        self.PLAYER = player.Player()
        self.NPC = npc.importNpc(self)
        self.LOC = locations.importLocations(self)
        self.load_map()
        self.obj_on_curr_map()



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

        for location in self.activeLoc:
            if location.map == self.GRID.name:
                self.window.blit(location.sprite,(location.position[0]-(self.GRID.horizontal_move*TILESIZE), location.position[1]-(self.GRID.vertical_move*TILESIZE) ))

        for character in self.activeNPC:
            if character.map == self.GRID.name:
                self.window.blit(character.sprite,(character.position[0]-(self.GRID.horizontal_move*TILESIZE), character.position[1]-(self.GRID.vertical_move*TILESIZE) ))

        self.window.blit(self.PLAYER.SPRITE,self.PLAYER.POS)
        pygame.display.update()


    def events(self):
        # Events on the map
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

        keys = pygame.key.get_pressed()
        x = self.PLAYER.POS[0]
        y = self.PLAYER.POS[1]

        player_X = x + (self.GRID.horizontal_move * TILESIZE)
        player_Y = y + (self.GRID.vertical_move * TILESIZE)

        # Move in Left and Up directions is still a little bit bugged but works just fine for now :)
        if keys[pygame.K_LEFT] and x > 0:
          # ABS potrzebny bo macierz może zczytywac z ujemnych wartości
            if self.GRID.data[y//TILESIZE + self.GRID.vertical_move][abs(x//TILESIZE + self.GRID.horizontal_move - 1)] not in LOCKED_TILES: # BLOKADA PRZED WEJŚĆIEM NA WODE
                x -= self.PLAYER.VELOCITY
                if x % TILESIZE == 0 and self.GRID.horizontal_move > self.GRID.MARGIN_LEFT:
                    self.GRID.horizontal_move -= 1

        if keys[pygame.K_RIGHT] and x < WIDTH - TILESIZE:
            if self.GRID.data[y//TILESIZE + self.GRID.vertical_move][x//TILESIZE + self.GRID.horizontal_move + 1] not in LOCKED_TILES:  # BLOKADA PRZED WEJŚĆIEM NA WODE
                x += self.PLAYER.VELOCITY
                if x % TILESIZE == 0 and self.GRID.horizontal_move < self.GRID.MARGIN_RIGHT:
                    self.GRID.horizontal_move += 1

        if keys[pygame.K_DOWN] and y < HEIGHT - TILESIZE:
            if self.GRID.data[y//TILESIZE + self.GRID.vertical_move + 1][x//TILESIZE + self.GRID.horizontal_move] not in LOCKED_TILES:  # BLOKADA PRZED WEJŚĆIEM NA WODE
                y += self.PLAYER.VELOCITY
                if y % TILESIZE == 0 and self.GRID.vertical_move < self.GRID.MARGIN_BOTTOM:
                    self.GRID.vertical_move += 1

        if keys[pygame.K_UP] and y > 0:
            if self.GRID.data[abs( (y//TILESIZE) + self.GRID.vertical_move - 1)][x//TILESIZE + self.GRID.horizontal_move] not in LOCKED_TILES:  # BLOKADA PRZED WEJŚĆIEM NA WODE
                y -= self.PLAYER.VELOCITY
                if y % TILESIZE == 0 and self.GRID.vertical_move > self.GRID.MARGIN_UP:
                    self.GRID.vertical_move -= 1

        # aby wejsc w interakcje z NPC wciskamy 'F' w jego okolicy
        # dialogi wciąż nie chodzą, ale mam nadzieje że da sie to elegancko ogarnac, beda mniej wiecej wyswietlac sie jak w obecnej formie jeszcze dorzuce zczytywanie z klawiatury i wtedy przerzucanie tekxtów
        # problem jeszcze z dialogami dla innych bo w zamku MIME nic nie mówi a powinien bo na konsoli jest
        # chwilowo więcej nie zrobię bo jutro idę na komunie kuzyna, na szczescie ostatnia w tym sezonie heh
        for npcInteract in self.activeNPC:
            if keys[pygame.K_f] and npcInteract.isCollision(player_X, player_Y):
                print("COLLISION!!!")
                self.activeNext = True
                for dialogue in npcInteract.dialogues:
                    print(dialogue.text)
                    try:
                        self.dialNext = dialogue.next[0]
                    except:
                        print("BRAK NEXT")
                        self.activeNext = False

                    if dialogue.player == "True":
                        self.playerDialogue(dialogue.text, player_X, player_Y)   
                    else:
                        print("SIEMA")
                        self.npcDialogue(dialogue.text, npcInteract.position[0], npcInteract.position[1])

                    while self.activeNext:
                        if self.dialNext.player == "True":
                            self.playerDialogue(self.dialNext.text, player_X, player_Y)    
                        else:
                            self.npcDialogue(self.dialNext.text, npcInteract.position[0], npcInteract.position[1])
                        try:
                            self.dialNext = self.dialNext.next[0]
                        except:
                            self.activeNext = False


        for locInteract in self.activeLoc:
            if locInteract.checkInteraction(player_X, player_Y):
                self.old_map_coordinates = [x, y]
                self.PREV_GRID.append(self.GRID)
                self.GRID = Map(locInteract.next_map)
                self.obj_on_curr_map()
                x = WIDTH//2
                y = HEIGHT - 2*TILESIZE
                self.GRID.vertical_move += self.GRID.MARGIN_BOTTOM

        if self.GRID.data[ (y//TILESIZE) + self.GRID.vertical_move ][x//TILESIZE + self.GRID.horizontal_move] in ENTRANCE:
            x = self.old_map_coordinates[0] + self.PLAYER.VELOCITY
            y = self.old_map_coordinates[1] + self.PLAYER.VELOCITY
            self.GRID = self.PREV_GRID[-1]
            self.PREV_GRID.pop()
            self.obj_on_curr_map()


        self.PLAYER.POS[0] = x
        self.PLAYER.POS[1] = y

        self.window.fill((0,0,0))
        self.updateMap()

    def playerDialogue(self, message, player_X, player_Y):
        self.dial_text = self.font.render(message, True, black, white)
        self.textRect = self.dial_text.get_rect()
        self.textRect.center = (player_X-5*TILESIZE, player_Y) 
        self.window.blit(self.dial_text, self.textRect)
        pygame.display.update()
        time.sleep(1)

    def npcDialogue(self, message, npc_X, npc_Y):
        print("NO ELO")
        self.dial_text = self.font.render(message, True, black, white)
        self.textRect = self.dial_text.get_rect()
        self.textRect.center = (npc_X+5*TILESIZE, npc_Y) 
        #self.textRect.center = (256, 896) 
        self.window.blit(self.dial_text, self.textRect)
        pygame.display.update()
        time.sleep(1)

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
