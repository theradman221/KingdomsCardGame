import pygame
import sys
import os
from pyfiles.Deck import Deck
from pyfiles.Visualizer import Visualizer
from pyfiles.cardclasses.Card import Card

class Gameboard:

    def __init__(self):

        self.WIDTH, self.HEIGHT = 1800,1000
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Gameboard")
        self.FPS = 60

        self.backGround_Image = pygame.image.load(os.getcwd() + '\pyfiles\menus\gameboard\gameboard.jpg')
        self.backGround_Image = pygame.transform.scale(self.backGround_Image, (1500, 1000))
        self.kingdom_text = pygame.image.load(os.getcwd()+ '\pyfiles\menus\gameboard\_Kingdom_.png')
        self.kingdom_text = pygame.transform.scale(self.kingdom_text,(500, 80))
        self.relics_text = pygame.image.load(os.getcwd()+ '\pyfiles\menus\gameboard\_Relics_.png')
        self.relics_text = pygame.transform.scale(self.relics_text,(450,60))
        self.terra_text = pygame.image.load(os.getcwd()+ '\pyfiles\menus\gameboard\_Terra_.png')
        self.terra_text = pygame.transform.scale(self.terra_text, (450,60))
        self.separator = pygame.image.load(os.getcwd()+ '\pyfiles\menus\gameboard\icons.jpg')
        self.separator = pygame.transform.scale(self.separator,(900, 30))
        # self.kingdom_zone = pygame.Rect()

    def blit_board(self): # anything that will be drawn on the board will need to be called within this function
        self.WIN.blit(self.backGround_Image, (200, 0))
        self.WIN.blit(self.kingdom_text, (780, 700))
        self.WIN.blit(self.separator, (570, 800))
        self.WIN.blit(self.relics_text,(780,855))
        self.WIN.blit(self.separator, (570, 950))
        self.WIN.blit(self.terra_text,(780, 1000))

    def draw_board(self):
        pygame.display.update()

    def blit_card(self, visualizer):
        viscard = visualizer.get_card()
        if viscard.get_is_rested():
            visualizer.visualizer(False)
        else:
            visualizer.visualizer(True)

    def blit_card_big(self, visualizer):
        visualizer.scale_card_up(False)

    def bg(self, test: bool) -> None: # this is the pygame loop and where the logic of the game will run
        self.clock = pygame.time.Clock()
        run = True
        while run:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.blit_board()
            self.draw_board()
    pygame.quit()


def game_board_loop(test: bool = False) -> 'Gameboard':
    board = Gameboard()
    board.bg(test)
    return Gameboard


if __name__ == '__main__':
    game_board_loop()


