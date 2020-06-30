import pygame as pg
from settings import *
import net

def make_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


#def is_in_DB(nick):
#    return False

screen = pg.display.set_mode((1280, 720))
font = pg.font.Font(None, 32)
font2 = pg.font.Font(None, 64)

pg.display.set_caption('Main Menu')
clock = pg.time.Clock()
pg.init()
click = False


def main_menu():
    # screen = pg.display.set_mode((1280, 720))
    # font = pg.font.Font(None, 32)
    # font2 = pg.font.Font(None, 64)
    #
    # pg.display.set_caption('Main Menu')
    # clock = pg.time.Clock()
    input_box = pg.Rect(520, 300, 140, 32)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False
    nick = ''

    while not done:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                    #active = True
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        nick = text
                        print(text)
                        text = ''
                        print(net.is_in_DB(nick))
                        if net.is_in_DB(nick):
                           #pobiera cechy z DB i tworzy nowa gre tutaj
                           print(net.askForPlayerData(nick))
                           zaladuj_postac = True
                           Otworz_gre = True
                           sdax = 1

                        #funkcja do sprawdzenia czy ten 'nick' jest w DB
                        else:
                            tworz_postac = True
                            print('wchodzi do pentli i ')
                            print(nick)
                            create_champ(nick)


                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)

        make_text('Welcome in our game!', font2, color_inactive, screen, 375, 50)
        make_text('Insert your nickname to start the game', font, color_inactive, screen, 400, 200)
        make_text('Your Nick:', font, color_inactive, screen, 560, 260)
        pg.display.flip()


        clock.tick(30)


def create_champ(nick):
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
        make_text('Creating your champion', font, black, screen, 20, 20)
        mx, my = pygame.mouse.get_pos()
        make_text(f'Remainings available points: {available_points}', font, black, screen, 900, 20)
        # screen.blit(minus2, (200, 100))
        # screen.blit(plus2, (300, 100))

        #strength --------------------
        button_strength_add = pygame.Rect(350, 100, 76, 76)
        button_strength_reduce = pygame.Rect(450, 100, 76, 76)

        make_text(f'Strength points: {strength}', font, black, screen, 20, 125)

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

        #agility-----------------------
        button_agility_add = pygame.Rect(350, 200, 76, 76)
        button_agility_reduce = pygame.Rect(450, 200, 76, 76)

        make_text(f'Agility points: {agility}', font, black, screen, 20, 225)

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
        button_intelligence_add = pygame.Rect(350, 300, 76, 76)
        button_intelligence_reduce = pygame.Rect(450, 300, 76, 76)

        make_text(f'Intelligence points: {intelligence}', font, black, screen, 20, 325)

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
        button_endurance_add = pygame.Rect(350, 400, 76, 76)
        button_endurance_reduce = pygame.Rect(450, 400, 76, 76)

        make_text(f'Endurance points: {endurance}', font, black, screen, 20, 425)

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
        button_luck_add = pygame.Rect(350, 500, 76, 76)
        button_luck_reduce = pygame.Rect(450, 500, 76, 76)

        make_text(f'Luck points: {luck}', font, black, screen, 20, 525)

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
        button_charisma_add = pygame.Rect(350, 600, 76, 76)
        button_charisma_reduce = pygame.Rect(450, 600, 76, 76)

        make_text(f'Charisma points: {charisma}', font, black, screen, 20, 625)

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
        button_submit = pygame.Rect(800, 270, 256, 256)
        #make_text(f'Crate Champion', font, black, screen, 800, 400)



        if button_submit.collidepoint((mx, my)):
            if click:
                if available_points == 0:
                    note = open('postacie.txt', 'a')
                    note.write(f'nick:{nick};strength:{strength};agility:{agility};intelligence:{intelligence};endurance:{endurance};luck:{luck};charisma:{charisma}\n')
                    note.close()
                    #mp = Character(sxdasdasdasd)
                    # dodac do tablicy

                    #TO DO:
                    #stworzyck klase worrior i np dodac do tabliczy gracze
                    #wczesniej zintegruj gracza i playera :)



        #generating buttons ------------
        pygame.draw.rect(screen, lightskyblue3, button_strength_add)
        pygame.draw.rect(screen, lightskyblue3, button_strength_reduce)
        screen.blit(plus2, button_strength_add)
        screen.blit(minus2, button_strength_reduce)

        pygame.draw.rect(screen, lightskyblue3, button_agility_add)
        pygame.draw.rect(screen, lightskyblue3, button_agility_reduce)
        screen.blit(plus2, button_agility_add)
        screen.blit(minus2, button_agility_reduce)

        pygame.draw.rect(screen, lightskyblue3, button_intelligence_add)
        pygame.draw.rect(screen, lightskyblue3, button_intelligence_reduce)
        screen.blit(plus2, button_intelligence_add)
        screen.blit(minus2, button_intelligence_reduce)

        pygame.draw.rect(screen, lightskyblue3, button_endurance_add)
        pygame.draw.rect(screen, lightskyblue3, button_endurance_reduce)
        screen.blit(plus2, button_endurance_add)
        screen.blit(minus2, button_endurance_reduce)

        pygame.draw.rect(screen, lightskyblue3, button_luck_add)
        pygame.draw.rect(screen, lightskyblue3, button_luck_reduce)
        screen.blit(plus2, button_luck_add)
        screen.blit(minus2, button_luck_reduce)

        pygame.draw.rect(screen, lightskyblue3, button_charisma_add)
        pygame.draw.rect(screen, lightskyblue3, button_charisma_reduce)
        screen.blit(plus2, button_charisma_add)
        screen.blit(minus2, button_charisma_reduce)

        pygame.draw.rect(screen, darkgray, button_submit)
        screen.blit(start3, button_submit)

        click = False



        for event in pg.event.get():
            if event.type == pg.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


        pygame.display.update()
        clock.tick(60)


# if __name__ == '__main__':
#     pg.init()
#     main()
#     pg.quit()

main_menu()
