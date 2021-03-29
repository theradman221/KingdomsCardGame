import pygame
import sys

mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Kingdoms_Main_Menu')
screen = pygame.display.set_mode((500,500), 0,32)

font = pygame.font.SysFont(None, 20)


def menu_draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)


click = False


def main_menu():
    while True:

        screen.fill((100,100,100))
        menu_draw_text('Main Menu', pygame.font.SysFont('Corbel',35), (255,255,255), screen, 170, 20)

        mx, my = pygame.mouse.get_pos()

        button_play = pygame.Rect(50, 100, 200, 50)
        button_deck = pygame.Rect(50, 100, 200, 50)
        button_quit = pygame.Rect(50, 100, 200, 50)

        if button_play.collidepoint((mx,my)):
            if click:
                pass
        if button_deck.collidepoint((mx,my)):
            if click:
                pass
        if button_quit.collidepoint((mx,my)):
            if click:
                pass

        pygame.draw.rect(screen, (255,255,255), button_play)
        pygame.draw.rect(screen, (255,255,255), button_deck)
        pygame.draw.rect(screen, (255,255,255), button_quit)


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


main_menu()



