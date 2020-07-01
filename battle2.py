from worrior import *
from map import *
from worrior import *
from time import sleep
import random
from pip._vendor.distlib.compat import raw_input



class Battle2:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH_BATTLE, HEIGHT_BATTLE))
        pygame.display.set_caption("Battle!")

    def quit(self):
        # Quit game
        pygame.quit()

    def create_map(self, hero, enemy):
        self.GRID = Map(MAP_BATTLE)
        self.update_map(hero, enemy)

    def update_map(self, hero, enemy):
        for row in range(5):
            for column in range(5):
                self.window.blit(TEXTURES[self.GRID.data[row + self.GRID.vertical_move][column + self.GRID.horizontal_move]],(column * TILESIZE, row * TILESIZE))

        self.window.blit(hero.sprite, (hero.position_x, hero.position_y))
        self.window.blit(enemy.sprite, (enemy.position_x, enemy.position_y))

        enemy_hp = font2.render(f'HP: {enemy.hp}', True, green)
        enemy_hpRect = enemy_hp.get_rect()
        enemy_hpRect.center = (50, 40)
        self.window.blit(enemy_hp, enemy_hpRect)

        hero_hp = font2.render(f'HP: {hero.hp}', True, green)
        hero_hpRect = hero_hp.get_rect()
        hero_hpRect.center = (50, 290)
        self.window.blit(hero_hp, hero_hpRect)

        hero_pa = font2.render(f'PA: {hero.pa}', True, yellow)
        hero_paRect = hero_pa.get_rect()
        hero_paRect.center = (250, 290)
        self.window.blit(hero_pa, hero_paRect)
        pygame.display.update()

    def make_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)


    def new(self, hero, enemy): # chyba chce tutaj dac woja i monsterka :)
        self.create_map(hero, enemy)
        #funkcja na rozgrywke
        self.play = True
        while self.play:
            pygame.time.delay(FPS)
            # sleep(2)
            # self.make_move(enemy, 50)
            # self.update_map(hero, enemy)
            # # self.make_text('atakuje!!', pygame.font.SysFont(None, 20), black, self.window, 10, 10)
            # sleep(2)
            # self.make_move(enemy, -50)
            # self.update_map(enemy, hero)
            # sleep(2)

            # self.enemy_attack(enemy, hero)
            # self.hero_attack(hero, enemy)

            # self.play = False
            self.fight(hero, enemy)



            # self.fight(hero, enemy)

    # def enemy_attack(self, enemy, hero):
    #     self.make_move(enemy, 50)
    #     self.update_map(hero, enemy)
    #     sleep(2)
    #     self.make_move(enemy, -50)
    #     self.update_map(hero, enemy)
    #     sleep(2)
    #
    # def hero_attack(self, hero, enemy):
    #     self.make_move(hero, -50)
    #     self.update_map(hero, enemy)
    #     sleep(2)
    #     self.make_move(hero, 50)
    #     self.update_map(hero, enemy)
    #     sleep(2)

    def enemy_attack1(self, enemy, hero):
        self.make_move(enemy, 50)
        self.update_map(hero, enemy)
        sleep(1)

    def enemy_attack2(self, enemy, hero):
        self.make_move(enemy, -50)
        self.update_map(hero, enemy)
        sleep(1)

    def hero_attack1(self, hero, enemy):
        self.make_move(hero, -50)
        self.update_map(hero, enemy)
        sleep(1)

    def hero_attack2(self, hero, enemy):
        self.make_move(hero, 50)
        self.update_map(hero, enemy)
        sleep(1)

    #funckja rozgrywki
    def fight(self,hero, monster):
        round_num = 1

        while hero.is_alive() and monster.is_alive():  # zwraca true tylko kiedy oba warunki sa prawdziwe => jeden umiera i loop sie konczy
            print(f"It is: {round_num} round!")
            self.show_stats(hero, monster)

            if round_num % 2 == 1:
                #self.update_map(hero, monster)
                self.duel2(hero, monster)  # 1 parametr atakuje 2
                #self.update_map(hero, monster)
            else:
                #self.update_map(hero, monster)
                self.duel(monster, hero)
                #self.update_map(hero, monster)
            print('\n')

            sleep(2)
            round_num += 1

        if hero.is_alive():
            print('Hero won')
            self.play = False
        else:
            print('Monster won')
            self.play = False

    def duel(self, x, y):
        print(f'{x} has attaced {y}')
        dmg = x.attack() - y.defence()
        if dmg < 0:
            dmg = 0
        self.enemy_attack1(x, y)
        print(f'{y} lost {dmg} health point(s)')
        y.lost_hp(dmg)
        self.enemy_attack2(x, y)



    def duel2(self, x, y):
        print(f'{x} has attaced {y}')
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        dmg = x.attack() - y.defence()
                        if dmg < 0:
                            dmg = 0
                        x.pa += 2
                        self.hero_attack1(x, y)
                        y.lost_hp(dmg)
                        print(f'{y} lost {dmg} health point(s)')
                        self.hero_attack2(x, y)
                        waiting = False

                    if event.key == pygame.K_2:
                        if x.pa >= 5:
                            dmg = 2 * (x.attack() - y.defence())
                            if dmg < 0:
                                dmg = 0
                            x.pa -= 5
                            self.hero_attack1(x, y)
                            y.lost_hp(dmg)
                            print(f'{y} lost {dmg} health point(s)')
                            self.hero_attack2(x, y)
                            waiting = False
                        else:
                            print(f"You don't have enough PA to do strong attack, now you have {x.pa} PA")



    def show_stats(self, x, y):
        for i in (x, y):
            print(f"{i} has {i.hp} health point(s)")

    #ruch enemy, ruch hero
    def make_move(self, enemy, distance):
        enemy.position_y += distance
        # self.update_map()







#hero1 = Worrior('Mime','textures/characters/MIME.png', 120, 250, random.randint(100, 300), random.randint(50, 100), random.randint(5, 10))
#monster1 = Worrior('Snorlax','textures/characters/SNORLAX.png', 120, 10, random.randint(100, 300), random.randint(50, 100), random.randint(5, 10))


#battle = Battle2()
#battle.new(hero1, monster1)