import pygame as pg
from settings import *
import net
from worrior import *




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
done = False
hero = Worrior()

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
    # hero = Worrior()



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
                            done = True



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
    health = 0
    armor = 0
    action = 0


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

        #health-----------------------
        button_health_add = pygame.Rect(350, 200, 76, 76)
        button_health_reduce = pygame.Rect(450, 200, 76, 76)

        make_text(f'Health points: {health}', font, black, screen, 20, 225)

        if button_health_add.collidepoint((mx, my)):
            if click:
                if available_points > 0:
                    available_points -= 1
                    health += 1

        if button_health_reduce.collidepoint((mx, my)):
            if click:
                if health > 0:
                    health -= 1
                    available_points += 1

        #armor ----------------------
        button_armor_add = pygame.Rect(350, 300, 76, 76)
        button_armor_reduce = pygame.Rect(450, 300, 76, 76)

        make_text(f'Armor points: {armor}', font, black, screen, 20, 325)

        if button_armor_add.collidepoint((mx, my)):
            if click:
                if available_points > 0:
                    available_points -= 1
                    armor += 1

        if button_armor_reduce.collidepoint((mx, my)):
            if click:
                if armor > 0:
                    armor -= 1
                    available_points += 1

        #action ----------------------
        button_action_add = pygame.Rect(350, 400, 76, 76)
        button_action_reduce = pygame.Rect(450, 400, 76, 76)

        make_text(f'Action points: {action}', font, black, screen, 20, 425)

        if button_action_add.collidepoint((mx, my)):
            if click:
                if available_points > 0:
                    available_points -= 1
                    action += 1

        if button_action_reduce.collidepoint((mx, my)):
            if click:
                if action > 0:
                    action -= 1
                    available_points += 1



        # submit
        button_submit = pygame.Rect(800, 270, 256, 256)
        #make_text(f'Crate Champion', font, black, screen, 800, 400)



        if button_submit.collidepoint((mx, my)):
            global hero, done
            if click:
                if available_points == 0:
                    action += 5
                    print("zmieniam hirka")
                    hero = Worrior(name=nick, sprite='./BULBA64.png', position_x = 0, position_y = 0, hp = health, ad = strength, arm = armor, pa = action)
                    done = True
                    running = False
                    return hero

                    # pygame.quit()
                    # sys.exit()
                    # #pass
                    # note = open('postacie.txt', 'a')
            #                     # note.write(f'nick:{nick};strength:{strength};agility:{agility};intelligence:{intelligence};endurance:{endurance};luck:{luck};charisma:{charisma}\n')
            #                     # note.close()
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

        pygame.draw.rect(screen, lightskyblue3, button_health_add)
        pygame.draw.rect(screen, lightskyblue3, button_health_reduce)
        screen.blit(plus2, button_health_add)
        screen.blit(minus2, button_health_reduce)

        pygame.draw.rect(screen, lightskyblue3, button_armor_add)
        pygame.draw.rect(screen, lightskyblue3, button_armor_reduce)
        screen.blit(plus2, button_armor_add)
        screen.blit(minus2, button_armor_reduce)

        pygame.draw.rect(screen, lightskyblue3, button_action_add)
        pygame.draw.rect(screen, lightskyblue3, button_action_reduce)
        screen.blit(plus2, button_action_add)
        screen.blit(minus2, button_action_reduce)



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

def get_hero():
    global hero
    return hero

# if __name__ == '__main__':
#     pg.init()
#     main()
#     pg.quit()

# main_menu()
