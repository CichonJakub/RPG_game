#!/usr/bin/env Python3

# Start writing code for Koło Naukowe and build first 2D game :D

import pygame
from pygame.locals import *
import time
from settings import *
from map import *
import worrior
import locations
import quests
import npc
import net
import battle2
import random


class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption(TITLE)
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.server = net.Net()
        self.server.connectToServer()

    def load_map(self):
        self.GRID = Map(self.PLAYER.map)
        #self.GRID = Map(MAP)
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
        self.PLAYER = worrior.Worrior(name='xyz', sprite='./BULBA64.png',position_x=0, position_y=0, hp=100, ad=0, arm=0, pa=10)
        #def __init__(self, name='xyz', sprite='./BULBA64.png',position_x=0, position_y=0, hp=100, ad=0, arm=0, pa=10):
        self.server.putPlayer(self.PLAYER)
        print("My name is... " + str(self.PLAYER.name))
        self.NPC = npc.importNpc(self)
        self.LOC = locations.importLocations(self)
        self.QUEST = quests.importQuests(self)
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

        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        # print obecnej tablicy innych graczy
        print(self.server.getOtherPlayers)

        for otherPlayer in self.server.getOtherPlayers:
            print(self.PLAYER.map)
            print(otherPlayer['map'])
            if otherPlayer['map'] == self.PLAYER.map:
                self.window.blit(pygame.image.load(otherPlayer['sprite']),(otherPlayer['posX']-(self.GRID.horizontal_move*TILESIZE), otherPlayer['posY']-(self.GRID.vertical_move*TILESIZE) ))

        for character in self.activeNPC:
            if character.map == self.GRID.name:
                self.window.blit(character.sprite,(character.position_x-(self.GRID.horizontal_move*TILESIZE), character.position_y-(self.GRID.vertical_move*TILESIZE) ))

        self.window.blit(self.PLAYER.sprite, (self.PLAYER.position_x, self.PLAYER.position_y) )

        pygame.display.update()


    def events(self):
        # Events on the map
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

        keys = pygame.key.get_pressed()
        x = self.PLAYER.position_x
        y = self.PLAYER.position_y

        player_X = x + (self.GRID.horizontal_move * TILESIZE)
        player_Y = y + (self.GRID.vertical_move * TILESIZE)

        # Movement
        if keys[pygame.K_LEFT] and x > 0:
          # ABS potrzebny bo macierz może zczytywac z ujemnych wartości
            if self.GRID.data[y//TILESIZE + self.GRID.vertical_move][abs(x//TILESIZE + self.GRID.horizontal_move - 1)] not in LOCKED_TILES: # BLOKADA PRZED WEJŚĆIEM NA WODE
                x -= self.PLAYER.velocity
                if x % TILESIZE == 0 and self.GRID.horizontal_move > self.GRID.MARGIN_LEFT:
                    self.GRID.horizontal_move -= 1

        if keys[pygame.K_RIGHT] and x < WIDTH - TILESIZE:
            if self.GRID.data[y//TILESIZE + self.GRID.vertical_move][x//TILESIZE + self.GRID.horizontal_move + 1] not in LOCKED_TILES:  # BLOKADA PRZED WEJŚĆIEM NA WODE
                x += self.PLAYER.velocity
                if x % TILESIZE == 0 and self.GRID.horizontal_move < self.GRID.MARGIN_RIGHT:
                    self.GRID.horizontal_move += 1

        if keys[pygame.K_DOWN] and y < HEIGHT - TILESIZE:
            if self.GRID.data[y//TILESIZE + self.GRID.vertical_move + 1][x//TILESIZE + self.GRID.horizontal_move] not in LOCKED_TILES:  # BLOKADA PRZED WEJŚĆIEM NA WODE
                y += self.PLAYER.velocity
                if y % TILESIZE == 0 and self.GRID.vertical_move < self.GRID.MARGIN_BOTTOM:
                    self.GRID.vertical_move += 1

        if keys[pygame.K_UP] and y > 0:
            if self.GRID.data[abs( (y//TILESIZE) + self.GRID.vertical_move - 1)][x//TILESIZE + self.GRID.horizontal_move] not in LOCKED_TILES:  # BLOKADA PRZED WEJŚĆIEM NA WODE
                y -= self.PLAYER.velocity
                if y % TILESIZE == 0 and self.GRID.vertical_move > self.GRID.MARGIN_UP:
                    self.GRID.vertical_move -= 1

        # interactions with NPCs
        for npcInteract in self.activeNPC:
            if keys[pygame.K_f] and npcInteract.isCollision(player_X, player_Y):
                print("COLLISION!!!")
                for dialogue in npcInteract.dialogues:
                    # check for enabling new dialogues depanding on a quest
                    if (dialogue.questId, dialogue.stage) in self.PLAYER.curr_quests.items():
                           if dialogue.npc == npcInteract.npc_id:
                                dialogue.currentStage = "True"
                                print(dialogue.text)

                    if dialogue.currentStage == "True":
                        self.dialogue_choice = 1
                        self.dialogue_root = dialogue
                        self.activeNext = True
                        while self.activeNext:

                            if dialogue.interact == "True":
                                self.displayDialogue(dialogue.text)
                                if dialogue.option >= 1.0:
                                    self.playerChoice(dialogue, npcInteract)
                                else:
                                    self.wait()
                            else:
                                self.displayDialogue(dialogue.text)
                                self.wait()
                            try:
                                for choice in range(self.dialogue_choice):
                                    dialogue = dialogue.next[0]
                                print(dialogue.choice)
                                if dialogue.choice != self.dialogue_choice:
                                    while dialogue.choice != self.dialogue_choice:
                                        dialogue = dialogue.next[0]
                                self.dialogue_choice = 1
                            except:
                                self.activeNext = False

        # Enter the location
        for locInteract in self.activeLoc:
            if locInteract.checkInteraction(player_X, player_Y):
                self.PLAYER.prev_pos.append([x, y])
                #self.PREV_GRID.append(self.GRID)
                self.PLAYER.prev_map.append(self.GRID.name)
                self.GRID = Map(locInteract.next_map)
                self.PLAYER.map = self.GRID.name
                self.obj_on_curr_map()
                x = WIDTH//2
                y = HEIGHT - 2*TILESIZE
                self.GRID.vertical_move += self.GRID.MARGIN_BOTTOM

        # Leave the location
        if self.GRID.data[ (y//TILESIZE) + self.GRID.vertical_move ][x//TILESIZE + self.GRID.horizontal_move] in ENTRANCE:
            x = self.PLAYER.prev_pos[-1][0]
            y = self.PLAYER.prev_pos[-1][1] + TILESIZE
            self.PLAYER.prev_pos.pop()
            #self.GRID = self.PREV_GRID[-1]
            self.GRID = Map(self.PLAYER.prev_map[-1])
            self.PLAYER.map = self.GRID.name
            #self.PREV_GRID.pop()
            self.PLAYER.prev_map.pop()
            self.obj_on_curr_map()


        #updates
        self.PLAYER.position_x = x
        self.PLAYER.position_y = y
        self.window.fill((0,0,0))
        self.server.sendMove(self.PLAYER)
        self.updateMap()
        self.checkQuests()

    def displayDialogue(self, message):
        new_message = ""
        for letter in message:

            new_message += letter
            self.dial_text = self.font.render(new_message, True, black, white)
            self.textRect = self.dial_text.get_rect()
            self.textRect.center = (WIDTH//2, HEIGHT-0.25*TILESIZE)
            self.textRect.width = WIDTH
            self.window.blit(self.dial_text, self.textRect)
            pygame.display.update()
            time.sleep(subtitles_speed)

    def playerChoice(self, dialogue, npcInteract):
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_1 and dialogue.option >= 1:
                    if dialogue.next[0].text == '':
                        pass
                    else:
                        self.dialogue_choice = 1
                        self.updateMap()
                        self.PLAYER.curr_quests[dialogue.questId] = dialogue.stage + 1.0
                        print("Current quests: ")
                        print(self.PLAYER.curr_quests)
                        npcInteract.dialogues.remove(self.dialogue_root)
                        try:
                            npcInteract.dialogues[0].currentStage = "True"
                        except:
                            pass
                        return
                elif event.type == KEYDOWN and event.key == K_2 and dialogue.option >= 2:
                    self.dialogue_choice = 2
                    tmpDialogue = dialogue.next[0].next[0]
                    if tmpDialogue.delDial == 'True':
                        print("RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRROZNYYYYYYYYYYYYYYYYYYYYYY")
                        self.PLAYER.curr_quests[dialogue.questId] = dialogue.stage + 1.0
                        print("Current quests: ")
                        print(self.PLAYER.curr_quests)
                        npcInteract.dialogues.remove(self.dialogue_root)
                        try:
                            npcInteract.dialogues[0].currentStage = "True"
                        except:
                            pass
                    self.updateMap()
                    return
                elif event.type == KEYDOWN and event.key == K_3 and dialogue.option >= 3:
                    # Fight init
                    # Sprawdzenie czy dialog na ktory wskazuje nastepna opcja to fight jeśli tak to inincjujemy walkę
                    # Przyznawanie jakiś nagród za pokonanie przeciwnika ??? Jak na razie walka tylko przykładowa i powrót do gry po wygranej walce
                    # Pytanie jak rozpatrujemy przegraną walkę ? Wyświetlenie Game Over i usunięcie z DB ?
                    self.dialogue_choice = 3
                    self.fight(dialogue, npcInteract)
                    self.updateMap()
                    return

    def wait(self):
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_n:
                    self.updateMap()
                    return

    def checkQuests(self):
        isCompleted = False
        for quest, stage in self.PLAYER.curr_quests.items():
            for mission in self.QUEST:
                if quest == mission.questID:
                    if stage == mission.endStage:
                        self.PLAYER.quests_completed.append(quest)
                        self.PLAYER.gold += mission.gold
                        self.PLAYER.exp += mission.exp
                        isCompleted = True
                if quest < mission.questID:
                    # There is no point of checking more quests id's if current quest id is smaller because there will be no match XD
                    break
        if isCompleted:
            self.PLAYER.curr_quests.pop(self.PLAYER.quests_completed[-1], None)
            print(self.PLAYER.curr_quests)
            print(self.PLAYER.exp)
            print(self.PLAYER.gold)

    def fight(self, dialogue, npcInteract):
        battle = battle2.Battle2()

        hero = worrior.Worrior(self.PLAYER.name,'textures/characters/MIME.png', 120, 250, random.randint(100, 300), random.randint(50, 100), random.randint(5, 10))
        monster = worrior.Worrior('Blastoise','textures/characters/BLASTOISE.png', 120, 10, random.randint(100, 300), random.randint(50, 100), random.randint(5, 10))

        battle.new(hero, monster)
        self.window = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption(TITLE)

        if hero.is_alive():
            print("Hero won!!!!")
            self.PLAYER.gold += 100
            self.PLAYER.exp += 50
            self.PLAYER.curr_quests[dialogue.questId] = dialogue.stage + 1.0
            print("Current quests: ")
            print(self.PLAYER.curr_quests)
            npcInteract.dialogues.remove(self.dialogue_root)
            try:
                npcInteract.dialogues[0].currentStage = "True"
            except:
                pass
            self.activeNPC.remove(npcInteract)
            self.NPC.remove(npcInteract)



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
