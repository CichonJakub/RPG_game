import pygame as pg
from settings import *

def make_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def is_in_DB(nick):
    return False

def main():
    screen = pg.display.set_mode((1280, 720))
    font = pg.font.Font(None, 32)
    font2 = pg.font.Font(None, 64)

    pg.display.set_caption('Main Menu')
    clock = pg.time.Clock()
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
                        if is_in_DB(nick):
                           #pobiera cechy z DB i tworzy nowa gre tutaj
                           zaladuj_postac = True
                           Otworz_gre = True
                           sdax = 1

                        #funkcja do sprawdzenia czy ten 'nick' jest w DB
                        else:
                            tworz_postac = True



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


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()