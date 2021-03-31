import pygame
import sys
from pyfiles.menus.deckcreator import deckBuilder
from pygame.locals import *
import pygame_menu
from pygame_menu.examples import create_example_window
from typing import Tuple, Optional
__all__ = ['main']

# -----------------------------------------------------------------------------
# Constants and global variables
# -----------------------------------------------------------------------------
FPS = 60
WINDOW_SIZE = (900, 900)

sound: Optional['pygame_menu.sound.Sound'] = None
surface: Optional['pygame.Surface'] = None
main_menu: Optional['pygame_menu.Menu'] = None
# -----------------------------------------------------------------------------
# Methods
# -----------------------------------------------------------------------------
def main_background() -> None:
    """
    Background color of the main menu, on this function user can plot
    images, play sounds, etc.
    :return: None
    """
    surface.fill((40, 40, 40))

def update_menu_sound(value: Tuple, enabled: bool) -> None:
    """
    Update menu sound.
    :param value: Value of the selector (Label and index)
    :param enabled: Parameter of the selector, (True/False)
    :return: None
    """
    assert isinstance(value, tuple)
    if enabled:
        main_menu.set_sound(sound, recursive=True)
        print('Menu sounds were enabled')
    else:
        main_menu.set_sound(None, recursive=True)
        print('Menu sounds were disabled')


def main(test: bool = False) -> None:
    """
    Main program.
    :param test: Indicate function is being tested
    :return: None
    """

    # -------------------------------------------------------------------------
    # Globals
    # -------------------------------------------------------------------------
    global main_menu
    global sound
    global surface

    # -------------------------------------------------------------------------
    # Create window
    # -------------------------------------------------------------------------
    surface = create_example_window('KINGDOMS', WINDOW_SIZE)
    clock = pygame.time.Clock()

    # -------------------------------------------------------------------------
    # Set sounds
    # -------------------------------------------------------------------------
    sound = pygame_menu.sound.Sound()

    # Load example sounds
    sound.load_example_sounds()

    # Disable a sound
    sound.set_sound(pygame_menu.sound.SOUND_TYPE_ERROR, None)
    # -------------------------------------------------------------------------
    # Create menus: Settings
    # -------------------------------------------------------------------------

    settings_menu_theme = pygame_menu.themes.THEME_SOLARIZED.copy()
    settings_menu_theme.widget_font_color = (75,75,75)
    settings_menu_theme.title_offset = (5, 0)
    settings_menu_theme.widget_alignment = pygame_menu.locals.ALIGN_CENTER
    settings_menu_theme.widget_font = pygame_menu.font.FONT_8BIT
    settings_menu_theme.title_font = pygame_menu.font.FONT_8BIT
    settings_menu_theme.widget_font_size = 20

    settings_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 1,
        theme=settings_menu_theme,
        title='Settings',
        width=WINDOW_SIZE[0] * 1
    )
    settings_menu.add.selector('Menu sounds ',
                           [('Off', False), ('On', True)],
                           onchange=update_menu_sound)
    settings_menu.add.button('back', pygame_menu.events.BACK)

    # -------------------------------------------------------------------------
    # Create menus: Deck Creator
    # -------------------------------------------------------------------------
    Deck_Creator_Theme = pygame_menu.themes.THEME_SOLARIZED.copy()
    Deck_Creator_Theme.widget_font_color = (75,75,75)
    Deck_Creator_Theme.title_offset = (5, 0)
    Deck_Creator_Theme.widget_alignment = pygame_menu.locals.ALIGN_CENTER
    Deck_Creator_Theme.widget_font = pygame_menu.font.FONT_8BIT
    Deck_Creator_Theme.title_font = pygame_menu.font.FONT_8BIT
    Deck_Creator_Theme.widget_font_size = 20

    deck_Creator = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 1,
        theme=Deck_Creator_Theme,
        title='Deck Creator',
        width=WINDOW_SIZE[0] * 1
    )
    deck_Creator.add.button('back', pygame_menu.events.BACK)
    # -------------------------------------------------------------------------
    # Create menus: Deck Creator
    # -------------------------------------------------------------------------
    Deck_Selector_Theme = pygame_menu.themes.THEME_SOLARIZED.copy()
    Deck_Selector_Theme.widget_font_color = (75,75,75)
    Deck_Selector_Theme.title_offset = (5, 0)
    Deck_Selector_Theme.widget_alignment = pygame_menu.locals.ALIGN_CENTER
    Deck_Selector_Theme.widget_font = pygame_menu.font.FONT_8BIT
    Deck_Selector_Theme.title_font = pygame_menu.font.FONT_8BIT
    Deck_Selector_Theme.widget_font_size = 20

    deck_Selector = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 1,
        theme=Deck_Creator_Theme,
        title='Deck Selector',
        width=WINDOW_SIZE[0] * 1
    )

    # Selectable items
    items = [('blue', 'FAKE BLUE DECK'),
             ('red', 'FAKE RED DECK'),
             ('yellow', 'FAKE YELLOW DECK')]

    deck_Selector.add.dropselect(
        'Select a Deck',
        items,

        dropselect_id='deck_drop'
    )
    deck_Selector.add.dropselect_multiple(
        title='Pick 3 colors',
        items=[('Black', (0, 0, 0)),
               ('Blue', (0, 0, 255)),
               ('Cyan', (0, 255, 255)),
               ('Fuchsia', (255, 0, 255)),
               ('Green', (0, 255, 0)),
               ('Red', (255, 0, 0)),
               ('White', (255, 255, 255)),
               ('Yellow', (255, 255, 0))],
        dropselect_multiple_id='pickcolors',
        max_selected=3,
        open_middle=True,
        selection_box_height=6  # How many options show if opened
    )

    deck_Selector.add.button('back', pygame_menu.events.BACK)
    # -------------------------------------------------------------------------
    # Create menus: Main menu
    # -------------------------------------------------------------------------
    main_menu_theme = pygame_menu.themes.THEME_SOLARIZED.copy()
    main_menu_theme.widget_font_color = (75,75,75)
    main_menu_theme.title_font = pygame_menu.font.FONT_8BIT
    main_menu_theme.widget_font = pygame_menu.font.FONT_8BIT
    main_menu_theme.widget_font_size = 30

    main_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 1,
        onclose=pygame_menu.events.EXIT,  # User press ESC button
        theme=main_menu_theme,
        title='Main menu',
        width=WINDOW_SIZE[0] * 1
    )

    main_menu.add.button('Play')
    main_menu.add.button('Deck Creator', deck_Creator)
    main_menu.add.button('Deck Selector', deck_Selector)
    main_menu.add.button('Settings', settings_menu)
    main_menu.add.button('Quit', pygame_menu.events.EXIT)


    # -------------------------------------------------------------------------
    # Main loop
    # -------------------------------------------------------------------------
    while True:

        # Tick
        clock.tick(FPS)

        # Paint background
        main_background()

        # Main menu
        main_menu.mainloop(surface, main_background, disable_loop=test, fps_limit=FPS)

        # Flip surface
        pygame.display.flip()

        # At first loop returns
        if test:
            break


if __name__ == '__main__':
    main()