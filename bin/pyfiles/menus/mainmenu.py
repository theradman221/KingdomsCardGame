"""
-------------------------------------------------------------------------------
The MIT License (MIT)
Copyright 2017-2021 Pablo Pizarro R. @ppizarror
Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software
is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
-------------------------------------------------------------------------------
"""
import pygame
import sys
from pygame.locals import *
import pygame_menu
from pygame_menu.examples import create_example_window
from typing import Tuple, Optional
import json

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
    settings_menu_theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
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
    deck_Creator_Theme = pygame_menu.themes.THEME_SOLARIZED.copy()
    deck_Creator_Theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
    deck_Creator_Theme.widget_font_color = (75,75,75)
    deck_Creator_Theme.title_offset = (5, 0)
    deck_Creator_Theme.widget_alignment = pygame_menu.locals.ALIGN_CENTER
    deck_Creator_Theme.widget_font = pygame_menu.font.FONT_8BIT
    deck_Creator_Theme.title_font = pygame_menu.font.FONT_8BIT
    deck_Creator_Theme.widget_font_size = 20

    deck_Creator = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 1,
        theme=deck_Creator_Theme,
        title='Deck Creator',
        width=WINDOW_SIZE[0] * 1
    )
# I know this isnt the correct way to do this, just for testing purposes for now.
    bastionlist = [("Dwarven Kingdom", ""), ("Magi Tower", "")]
    herolist = [("Argon The Telekinetic", "Blue"), ("Avren The Spellsword", "Blue"), ("Heath The Prideful", "Yellow")]
    lordlist = [("Ares Lord of Battle", "Red")]
    pawnlist = [("Big Shield Dwarf", ""),("Catapult Squad", ""), ("Dwarven Champion", ""), ("Dwarven Scholar", ""), ("Elder Magi", ""), ("Etherial Shield", ""), ("Hired Assassin", "")]
    reliclist = [("Crystal Projector", ""), ("Lotus Shrine", ""), ("Shrine of Greed", ""), ("The Lost Armory", ""), ("The Rock", "")]
    scrolllist = [("Crack", ""), ("Lucid Mind", ""), ("Speed Scroll", "")]
    supplylist = [("Dirty Contracts", "")]
    terralist = [("Island", ""), ("Mountain", "")]
    tokenlist = [("", "")]
    tricelist = [("After the Storm", ""), ("Counter", ""), ("Pluck", ""), ("The Bigger They Are", "")]


# I have hard coded these lists, and will need to be changed for the NON DEMO version.
    yellowcardlist = ["Aries Lord of Battle", "Heath The Prideful", "Dwarven Kingdom", "Big Shield Dwarf", "Dwarven Scholar", "Relaxed Dwarf", "Catapult Squad", "Dwarven Champion", "Hired Pirate", "Hired Assassin", "Speed Scroll", "Dirty Contracts", "Lost Armory",
                      "Crystal Projector", "After the Storm", "Lotus Shrine", "The Rock", "Shrine Of Greed"]

    bluecardlist = ["Avren the Spellsword", "Argon The Telekinetic", "Magi Tower", "Ward Magi", "Ethereal Shield", "Pyro Magi Warrior", "Elder Magi", "Magi Freshman", "Island", "Hired Pirate", "Hired Assassin", "Lucid Mind", "Pluck",
                    "Crack", "The Bigger They Are", "Counter", "Lotus Shrine", "The Rock", "Shrine of Greed"]

    deck_Creator.add.dropselect(
        'Bastion',
        bastionlist,

        dropselect_id='deck_drop',
        max_selected=1,
        selection_box_height=6
    )
    deck_Creator.add.dropselect(
        'Hero',
        herolist,

        dropselect_id='Hero_Drop',
        selection_box_height=6
    )
    deck_Creator.add.dropselect(
        'Lord',
        lordlist,

        dropselect_id='lord_Drop',
        selection_box_height=6
    )
    deck_Creator.add.dropselect_multiple(
        'Pawn',
        pawnlist,

        dropselect_multiple_id='pawn_Drop',
        max_selected=3,
        open_middle=True,
        selection_box_height=6
    )
    deck_Creator.add.dropselect_multiple(
        'Relic',
        reliclist,

        dropselect_multiple_id='relic_Drop',
        max_selected=3,
        open_middle=True,
        selection_box_height=6
    )
    deck_Creator.add.dropselect_multiple(
        'Scroll',
        scrolllist,

        dropselect_multiple_id='scroll_Drop',
        max_selected=3,
        open_middle=True,
        selection_box_height=6
    )
    deck_Creator.add.dropselect_multiple(
        'supply',
        supplylist,

        dropselect_multiple_id='supply_Drop',
        max_selected=3,
        open_middle=True,
        selection_box_height=6
    )
    deck_Creator.add.dropselect_multiple(
        'terra',
        terralist,

        dropselect_multiple_id='terra_Drop',
        max_selected=3,
        open_middle=True,
        selection_box_height=6
    )
    deck_Creator.add.dropselect_multiple(
        'Token',
        tokenlist,

        dropselect_multiple_id='token_Drop',
        max_selected=3,
        open_middle=True,
        selection_box_height=6
    )
    deck_Creator.add.dropselect_multiple(
        'Trice',
        items=tricelist,

        dropselect_multiple_id='trice_Drop',
        max_selected=3,
        open_middle=True,
        selection_box_height=6
    )
    deck_Creator.add.dropselect_multiple(
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
    deck_Creator.add.text_input(
        'Deck Name: ',
        maxlength=19,
        textinput_id='long_text'
    )

    # This is a placeholder function, it needs to be updated to append cards to the deck somehow, so that multiple of the same cards can be selected
    def data_fun() -> None:
        """
        Print data of the menu.
        :return: None
        """
        print('Deck Data:')
        data = deck_Creator.get_input_data()
        for k in data.keys():
            print(u'\t{0}\t=>\t{1}'.format(k, data[k]))

    deck_Creator.add.button('Append Cards', data_fun)  # Call function

    deck_Creator.add.button('back', pygame_menu.events.BACK)

    # -------------------------------------------------------------------------
    # Create menus: Deck Creator Red
    # -------------------------------------------------------------------------
    deck_Creator_Yellow_Theme = pygame_menu.themes.THEME_SOLARIZED.copy()
    deck_Creator_Yellow_Theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
    deck_Creator_Yellow_Theme.widget_font_color = (75, 75, 75)
    deck_Creator_Yellow_Theme.title_offset = (5, 0)
    deck_Creator_Yellow_Theme.widget_alignment = pygame_menu.locals.ALIGN_CENTER
    deck_Creator_Yellow_Theme.widget_font = pygame_menu.font.FONT_8BIT
    deck_Creator_Yellow_Theme.title_font = pygame_menu.font.FONT_8BIT
    deck_Creator_Yellow_Theme.widget_font_size = 20


    deck_Creator_Yellow = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 1,
        theme=deck_Creator_Theme,
        title='Yellow Deck Creator',
        width=WINDOW_SIZE[0] * 1
    )
    #this needs to be changed so that it pulls the description from each card
    cardinfo = "This is where the information for each picked card will be added"
    for i in yellowcardlist:
        submenu = pygame_menu.Menu(i + ' Info', 750, 750, theme=deck_Creator_Theme,
                                           mouse_motion_selection=True, center_content=False)
        submenu.add.vertical_margin(75)
        submenu.add.label('Description', align=pygame_menu.locals.ALIGN_LEFT,
                          font_name=pygame_menu.font.FONT_OPEN_SANS_BOLD,
                          margin=(5, 10))
        label = submenu.add.label(cardinfo, max_char=70,
                                  align=pygame_menu.locals.ALIGN_LEFT,
                                  margin=(29, 1), font_size=20,
                                  font_name=pygame_menu.font.FONT_PT_SERIF,
                                  font_color=(0,0,0), padding=0)
        submenu.add.button("Add "+ i +" to Deck" )

        submenu.add.vertical_margin(40)  # Bottom margin

        deck_Creator_Yellow.add.button(i, submenu)




    # -------------------------------------------------------------------------
    # Create menus: Deck Color
    # -------------------------------------------------------------------------
    deck_C_Theme = pygame_menu.themes.THEME_SOLARIZED.copy()
    deck_C_Theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
    deck_C_Theme.widget_font_color = (75,75,75)
    deck_C_Theme.title_offset = (5, 0)
    deck_C_Theme.widget_alignment = pygame_menu.locals.ALIGN_CENTER
    deck_C_Theme.widget_font = pygame_menu.font.FONT_8BIT
    deck_C_Theme.title_font = pygame_menu.font.FONT_8BIT
    deck_C_Theme.widget_font_size = 20

    deck_C = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 1,
        theme=deck_C_Theme,
        title='Select the Deck Color',
        width=WINDOW_SIZE[0] * 1
    )
    deck_C.add.button('Blue', deck_Creator)
    deck_C.add.button('Yellow', deck_Creator_Yellow)

    # -------------------------------------------------------------------------
    # Create menus: Deck Selector
    # -------------------------------------------------------------------------
    Deck_Selector_Theme = pygame_menu.themes.THEME_SOLARIZED.copy()
    Deck_Selector_Theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
    Deck_Selector_Theme.widget_font_color = (75,75,75)
    Deck_Selector_Theme.title_offset = (5, 0)
    Deck_Selector_Theme.widget_alignment = pygame_menu.locals.ALIGN_CENTER
    Deck_Selector_Theme.widget_font = pygame_menu.font.FONT_8BIT
    Deck_Selector_Theme.title_font = pygame_menu.font.FONT_8BIT
    Deck_Selector_Theme.widget_font_size = 20

    deck_Selector = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 1,
        theme=deck_Creator_Theme,
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
    main_menu_theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
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
    main_menu.add.button('Deck Creator', deck_C)
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