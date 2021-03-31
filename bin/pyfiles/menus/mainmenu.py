import pygame
import sys
from pyfiles.menus.deckcreator import deckBuilder
from pygame.locals import *

import pygame_menu
from pygame_menu.examples import create_example_window

from typing import Tuple, Any

surface = create_example_window('Example - Simple', (600, 400))


menu = pygame_menu.Menu(
    height=400,
    theme=pygame_menu.themes.THEME_BLUE,
    title='Kingdoms',
    width=500
)

menu.add.button('Play')
menu.add.button('Deck Builder', deckBuilder)
menu.add.button('Choose Deck')
menu.add.button('Quit', pygame_menu.events.EXIT)

if __name__ == '__main__':
    menu.mainloop(surface)


