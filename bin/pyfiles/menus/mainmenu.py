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
from pyfiles.cardclasses.CardConstructor import load_all_cards
import sys
from pygame.locals import *
import pygame_menu
import pygame
from pygame_menu.examples import create_example_window
import math
from typing import Dict, Any, Tuple, Optional
import os
from pyfiles.Deck import Deck
from pyfiles.cardclasses.Card import Card


class MenuSystem(object):
    """
    The Following Object will create the entire menu system
    """
    image_widget: 'pygame_menu.widgets.Image'
    item_description_widget: 'pygame_menu.widgets.Label'
    main_menu: 'pygame_menu.Menu'
    settings_menu: 'pygame_menu.Menu'
    pickcolor_menu: 'pygame_menu.Menu'
    deckcreatoryellow_menu: 'pygame_menu.Menu'
    deckcreatorblue_menu: 'pygame_menu.Menu'
    play_button: 'pygame_menu.widgets.Button'
    settings_button: 'pygame_menu.widgets.Button'
    deckselector_button: 'pygame_menu.widgets.Button'
    deckcreator_button: 'pygame_menu.widgets.Button'
    quit_button: 'pygame_menu.widgets.Button'
    surface: 'pygame.Surface'
    sound: 'pygame_menu.sound.Sound'


    def __init__(self, master_deck) -> None:
        """
        Constructor.
        """

        # -------------------------------------------------------------------------
        # Create window
        # -------------------------------------------------------------------------

        self.FPS = 60
        self.WINDOW_SIZE = (900, 900)
        self.surface = create_example_window('KINGDOMS', (self.WINDOW_SIZE))
        self.clock = pygame.time.Clock()


        '''
        Setting the Theme
        '''
        main_menu_theme = pygame_menu.themes.THEME_GREEN
        main_menu_theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
        main_menu_theme.widget_font_color = (75, 75, 75)
        main_menu_theme.title_offset = (5, 0)
        main_menu_theme.widget_alignment = pygame_menu.locals.ALIGN_CENTER
        main_menu_theme.title_font = pygame_menu.font.FONT_8BIT
        main_menu_theme.widget_font = pygame_menu.font.FONT_BEBAS
        main_menu_theme.widget_font_size = (30)
        # -------------------------------------------------------------------------
        # Create menus: Settings
        # -------------------------------------------------------------------------
        self.settings_menu = pygame_menu.Menu(
            height=self.WINDOW_SIZE[1] * 1,
            theme=main_menu_theme,
            title='Settings',
            width=self.WINDOW_SIZE[1] * 1
            )

        # The update_menu_soundn is breaking everything :( will need to ask the team if they know what is goingn on with that
        # the sounds are nice but not vital to bug hunt day
        self.settings_menu.add.selector('Menu sounds ',
                                   [('Off', False), ('On', True)],
                                   onchange=self.update_menu_sound)
        self.settings_menu.add.button('back', pygame_menu.events.BACK)
        # -------------------------------------------------------------------------
        # Create menus: Deck Creator blue
        # -------------------------------------------------------------------------

        self.deckcreatorblue_menu = pygame_menu.Menu(
            height=self.WINDOW_SIZE[1] * 1,
            theme=main_menu_theme,
            title='Settings',
            width=self.WINDOW_SIZE[1] * 1
            )

        # THESE ARE HARD CODED FOR BUG TEST DAY THE FUNCTION THAT CALLS THE CARDS + INFO NEEDS TO BE ADDED
        cardinfo = "This is where the information for each picked card will be added"

        bluecardlist = master_deck.filter_by_color(["Blue"])


        for i in bluecardlist:
            submenu = pygame_menu.Menu(i.get_name(), 850, 850, theme=main_menu_theme,
                                       mouse_motion_selection=True, center_content=False)
            submenu.add.vertical_margin(75)
            submenu.add.label(i.get_name(), align=pygame_menu.locals.ALIGN_LEFT,
                              font_name=pygame_menu.font.FONT_OPEN_SANS_BOLD,
                              margin=(5, 10))
            submenu.add.label(i.get_description(), max_char=70,
                                      align=pygame_menu.locals.ALIGN_LEFT,
                                      margin=(29, 1), font_size=20,
                                      font_name=pygame_menu.font.FONT_PT_SERIF,
                                      font_color=(0, 0, 0), padding=0)
            self.deckcreatorblue_menu.add.button(i, submenu)
            submenu.add.vertical_margin(40)  # Bottom margin
            # THIS ADDS THE BUTTON
            submenu.add.button("Add " + i.get_name() + " to Deck"#I NEED TO ADD A FUNCTION HERE THAT ADDS THE SPECIFIC ITERATION TO THE DECK LIST.
            )

        self.deckcreatorblue_menu.add.button('back', pygame_menu.events.BACK)
        # -------------------------------------------------------------------------
        # Create menus: Deck Creator Yellow
        # -------------------------------------------------------------------------

        self.deckcreatoryellow_menu = pygame_menu.Menu(
            height=self.WINDOW_SIZE[1] * 1,
            theme=main_menu_theme,
            title='Create Yellow Deck',
            width=self.WINDOW_SIZE[1] * 1
            )

        # THESE ARE HARD CODED FOR BUG TEST DAY We just need to add the
        carddescription='Card Description'
        cardinfo = "This is where the information for each picked card will be added"
        cardimage = "the card image could go here once we figure that all out, and then we just need to draw it in the submenu which is easy enough"

        yellowcardlist = master_deck.filter_by_color(["Yellow"])

        def yellowdeckappend():
            yellowdeck.append(i)
            print(i+"Added to deck")
            return


        yellowdeck = []
        yellowtest = []


        def a(self, i) -> None:
            print(i)

#BUGHUNT DAY PLEASE HELP US SOLVE THE BUG IN THIS FOR LOOP!
        for i in yellowcardlist:

            #Creating a Submenu for every card in the Yellow Card List
            submenu = pygame_menu.Menu(i.get_name(), 750, 750, theme=main_menu_theme,
                                       mouse_motion_selection=True)
            submenu.add.vertical_margin(75)
            #adding description Title to submenu
            submenu.add.label(i.get_name(), align=pygame_menu.locals.ALIGN_LEFT,
                              font_name=pygame_menu.font.FONT_OPEN_SANS_BOLD,
                              margin=(5, 10))
            #adddescription
            submenu.add.label(i.get_description(), max_char=70,
                                      align=pygame_menu.locals.ALIGN_LEFT,
                                      margin=(29, 1), font_size=20,
                                      font_name=pygame_menu.font.FONT_PT_SERIF,
                                      font_color=(0, 0, 0), padding=0)
            self.deckcreatoryellow_menu.add.button(i, submenu)
            submenu.add.vertical_margin(40)  # Bottom margin

            submenu.add.button(i.get_name(), yellowdeckappend) #THIS BUTTON IS SUPPOSED TO APPEND THE SELECTED CARD TO THE DECK, HOWEVER IT IS ONLY APPENDING THE LAST ITERATION OF I TO THE DECK
            submenu.add.button("Back", pygame_menu.events.BACK)

        def showyellowdeck():
            print('yellow deck: ', yellowdeck)

        self.deckcreatoryellow_menu.add.button("Current Deck", showyellowdeck)
        self.deckcreatoryellow_menu.add.button('back', pygame_menu.events.BACK)

        # -------------------------------------------------------------------------
        # Create menus: pick color
        # -------------------------------------------------------------------------

        self.pickcolor_menu = pygame_menu.Menu(
            height=self.WINDOW_SIZE[1] * 1,
            theme=main_menu_theme,
            title='Select the Deck Color',
            width=self.WINDOW_SIZE[1] * 1
            )
        self.pickcolor_menu.add.button('Blue', self.deckcreatorblue_menu)
        self.pickcolor_menu.add.button('Yellow', self.deckcreatoryellow_menu)
        self.pickcolor_menu.add.button('back', pygame_menu.events.BACK)

        # -------------------------------------------------------------------------
        # Create menus: Deck Selector
        # -------------------------------------------------------------------------

        self.deckselector_menu = pygame_menu.Menu(
            height=self.WINDOW_SIZE[1] * 1,
            onclose=pygame_menu.events.EXIT,  # User press ESC button
            theme=main_menu_theme,
            title='Deck Selector',
            width=self.WINDOW_SIZE[1] * 1
        )
        # Selectable items
        items = [("Blue", "Avren the Spellsword", "Argon The Telekinetic", "Magi Tower", "Ward Magi", "Ethereal Shield",
                        "Pyro Magi Warrior", "Elder Magi", "Magi Freshman", "Island", "Hired Pirate", "Hired Assassin",
                        "Lucid Mind", "Pluck",
                        "Crack", "The Bigger They Are", "Counter", "Lotus Shrine", "The Rock", "Shrine of Greed"),
                 ('yellow', "Aries Lord of Battle", "Heath The Prideful", "Dwarven Kingdom", "Big Shield Dwarf",
                          "Dwarven Scholar", "Relaxed Dwarf", "Catapult Squad", "Dwarven Champion", "Hired Pirate",
                          "Hired Assassin", "Speed Scroll", "Dirty Contracts", "Lost Armory",
                          "Crystal Projector", "After the Storm", "Lotus Shrine", "The Rock", "Shrine Of Greed")]

        self.deckselector_menu.add.dropselect(
            'Select a Deck',
            items,

            dropselect_id='deck_drop',
            max_selected=1,
            selection_box_height=6

        )

        self.deckselector_menu.add.button('save selection', self.data_fun)
        self.deckselector_menu.add.button('back', pygame_menu.events.BACK)
        # -------------------------------------------------------------------------
        # MAIN MENU
        # -------------------------------------------------------------------------

        self.main_menu = pygame_menu.Menu(
            height= self.WINDOW_SIZE[1] * 1,
            onclose=pygame_menu.events.EXIT,  # User press ESC button
            theme=main_menu_theme,
            title='Main menu',
            width=self.WINDOW_SIZE[1] * 1
        )

        self.play_button = self.main_menu.add.button('Play')
        self.deckcreator_button = self.main_menu.add.button('Deck Creator', self.pickcolor_menu)
        self.deckselector_button = self.main_menu.add.button('Deck Selector', self.deckselector_menu)
        self.settings_button = self.main_menu.add.button('Settings', self.settings_menu)
        self.quit_button = self.main_menu.add.button('Quit', pygame_menu.events.EXIT)

    def data_fun(self) -> None:
        """
        Print data of the menu.
        :return: None
             """
        print('Deck Data:')
        data = self.deckselector_menu.get_input_data()
        for k in data.keys():
            print(u'\t{0}\t=>\t{1}'.format(k, data[k]))

    def update_menu_sound(self,value: Tuple, enabled: bool) -> None:
        """
        Update menu sound.
        :param value: Value of the selector (Label and index)
        :param enabled: Parameter of the selector, (True/False)
        :return: None
        """
        sound = pygame_menu.sound.Sound()
        sound.load_example_sounds()
        sound.set_sound(pygame_menu.sound.SOUND_TYPE_ERROR, None)
        assert isinstance(value, tuple)
        if enabled:
            self.main_menu.set_sound(sound, recursive=True)
            print('Menu sounds were enabled')
        else:
            self.main_menu.set_sound(None, recursive=True)
            print('Menu sounds were disabled')

    def mainloop(self, test: bool) -> None:
        """
        APP MAIN LOOP

        :param test:
        :return:
        """
        self.clock.tick(self.FPS)
        self.main_menu.mainloop(self.surface, disable_loop=test)


def main_menu(test: bool = False) -> 'MenuSystem':
    """
    MAIN FUNCTION
    :param test: Indicate function is being tested
    :return: App Object
    """
    mainmenu = MenuSystem()
    mainmenu.mainloop(test)
    return MenuSystem


if __name__ == '__main__':
    main_menu()




