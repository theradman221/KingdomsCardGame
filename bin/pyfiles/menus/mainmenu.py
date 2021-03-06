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
pygame.init()
from pygame_menu.examples import create_example_window
import math
from typing import Dict, Any, Tuple, Optional
import os
from pyfiles.Deck import Deck
from pyfiles.cardclasses.Card import Card
from pyfiles.menus.gameboard import Gameboard, game_board_loop


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
        self.WINDOW_SIZE = (1920,1000)
        # self.surface = create_example_window('KINGDOMS', (self.WINDOW_SIZE))
        self.surface = pygame.display.set_mode(self.WINDOW_SIZE, RESIZABLE)
        self.clock = pygame.time.Clock()
        self.yellowdeck = Deck("Yellow")
        self.bluedeck = Deck("Blue")
        self.main_menu = None


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
            height=1000, width=1920,
            theme=main_menu_theme,
            title='Settings',

            )

        self.settings_menu.add.selector('Menu sounds ',
                                   [('Off', False), ('On', True)],
                                   onchange=self.update_menu_sound)

        disclaimer = pygame_menu.Menu('Disclaimer', height=1000, width=1920, theme=main_menu_theme,
                                      mouse_motion_selection=True)
        disclaimer.add.label("""Disclaimer:
            This project has been developed as part of a classroom 
            learning experience by students at Utah State University.  
            While efforts are made to ensure copyrights and 
            intellectual property rights have not been violated, 
            it is the responsibility of the organization using any 
            classroom project screated by USU and its students 
            to make sure the materials contained therein do not 
            infringe the property rights (including without 
            limitation rights of privacy and publicity,
            trademark rights, copyrights, patents,
            trade secrets, and licenses) of third parties.""",
                             align=pygame_menu.locals.ALIGN_LEFT,
                             font_name=pygame_menu.font.FONT_PT_SERIF
                             )
        self.settings_menu.add.button('Disclaimer',disclaimer)
        self.settings_menu.add.button('back', pygame_menu.events.BACK)


        # -------------------------------------------------------------------------
        # Create menus: Deck Creator blue
        # -------------------------------------------------------------------------

        self.deckcreatorblue_menu = pygame_menu.Menu(
            height=1000, width=1920,
            theme=main_menu_theme,
            title='Settings',
            )

        bluecardlist = master_deck.filter_by_color(["Blue"])

        # [master_deck.get_royal_1.get_color(), master_deck.get_royal_2.get_color(),]
        # card.get_color()

        def bluedeckappend(card) -> None:
            self.bluedeck.add_card(card)
            print(card.get_name() + " Added to deck")
            return



        for card in bluecardlist:
            # Creating a Submenu for every card in the Yellow Card List
            submenu = pygame_menu.Menu(card.get_name(), height=1000, width=1920, theme=main_menu_theme,
                                       mouse_motion_selection=True)
            submenu.add.vertical_margin(75)
            # image for each card
            submenu.add.image(card.get_image(), angle=10, scale=(0.4, 0.4))

            # adding description Title to submenu
            attack_cards = ["Lord", "Hero", "Pawn", "Token", "Bastion"]
            if card.get_unit() in attack_cards:
                card_health = str(card.get_health())
                if card.get_unit() != "Bastion":
                    card_attack = str(card.get_attack())
                else:
                    card_attack = None
            else:
                card_attack = None
                card_health = None
            if card_health is None or card_attack is None:
                submenu.add.label(card.get_name() + "\n" + card.get_unit() + " Cost: " + str(card.get_cost()),
                                  align=pygame_menu.locals.ALIGN_LEFT,
                                  font_name=pygame_menu.font.FONT_OPEN_SANS_BOLD,
                                  margin=(5, 10))
            else:
                submenu.add.label(card.get_name() + "\n" + card.get_unit() + " Cost: " + str(
                    card.get_cost()) + " Health: " + card_health + " Attack: " + card_attack,
                                  align=pygame_menu.locals.ALIGN_LEFT,
                                  font_name=pygame_menu.font.FONT_OPEN_SANS_BOLD,
                                  margin=(5, 10))
            # adddescription
            submenu.add.label(card.get_description(), max_char=70,
                              align=pygame_menu.locals.ALIGN_LEFT,
                              margin=(29, 1), font_size=20,
                              font_name=pygame_menu.font.FONT_PT_SERIF,
                              font_color=(0, 0, 0), padding=0)
            self.deckcreatorblue_menu.add.button(card,
                                                   submenu)  # adding button for every card that calls the submenu for that card
            submenu.add.vertical_margin(40)  # Bottom margin

            submenu.add.button("add   " + card.get_name(), bluedeckappend, card)
            submenu.add.button("Back", pygame_menu.events.BACK)

        submenu_blue = pygame_menu.Menu("Cards In Deck", height=1000, width=1920, theme=main_menu_theme,
                                    mouse_motion_selection=True)
        submenu_blue.add.vertical_margin(40)  # Bottom margin


        self.deckcreatorblue_menu.add.button("Show Cards in Deck", submenu_blue)

        def showcardsblue():
            for card in self.bluedeck.get_copy():
                submenu_blue.add.label(card)

        submenu_blue.add.button('Populate chosen cards', showcardsblue)
        submenu_blue.add.button('Save Current Deck', self.save_blue)  # THIS NEEDS A FUNCTION THAT WILL SAVE THE CARDS CONTAINED IN THE DECK CURRENTLY BEING BUILT
        submenu_blue.add.button('Back', pygame_menu.events.BACK)


            # for card in bluedeck:
            #     print(card.get_name(), end=" ")


        # self.deckcreatorblue_menu.add.button("Current Deck", showbluedeck)
        self.deckcreatorblue_menu.add.button('back', pygame_menu.events.BACK)
        # -------------------------------------------------------------------------
        # Create menus: Deck Creator Yellow
        # -------------------------------------------------------------------------

        self.deckcreatoryellow_menu = pygame_menu.Menu(
            height=1000, width=1920,
            theme=main_menu_theme,
            title='Create Yellow Deck',

            )

        # [master_deck.get_royal_1.get_color(), master_deck.get_royal_2.get_color(),]
        # card.get_color()
        yellowcardlist = master_deck.filter_by_color(["Yellow"])

        def yellowdeckappend(card) -> None:
            self.yellowdeck.add_card(card)
            print(card.get_name() + " Added to deck")
            return



        for card in yellowcardlist:

            #Creating a Submenu for every card in the Yellow Card List
            submenu = pygame_menu.Menu(card.get_name(), height=1000, width=1920, theme=main_menu_theme,
                                       mouse_motion_selection=True)

            submenu.add.vertical_margin(75)
            #image for each card
            submenu.add.image(card.get_image(), angle=10,scale=(0.4, 0.4))

            #adding description Title to submenu
            attack_cards = ["Lord", "Hero", "Pawn", "Token", "Bastion"]
            if card.get_unit() in attack_cards:
                card_health = str(card.get_health())
                if card.get_unit() != "Bastion":
                    card_attack = str(card.get_attack())
                else:
                    card_attack = None
            else :
                card_attack = None
                card_health = None
            if card_health is None or card_attack is None:
                submenu.add.label(card.get_name() + "\n" + card.get_unit() + " Cost: " + str(card.get_cost()),
                                  align=pygame_menu.locals.ALIGN_LEFT,
                                  font_name=pygame_menu.font.FONT_OPEN_SANS_BOLD,
                                  margin=(5, 10))
            else:
                submenu.add.label(card.get_name() + "\n" + card.get_unit() + " Cost: " + str(card.get_cost()) + " Health: "+ card_health + " Attack: " + card_attack, align=pygame_menu.locals.ALIGN_LEFT,
                              font_name=pygame_menu.font.FONT_OPEN_SANS_BOLD,
                              margin=(5, 10))
            #adddescription
            submenu.add.label(card.get_description(),  max_char=70,
                                      align=pygame_menu.locals.ALIGN_LEFT,
                                      margin=(29, 1), font_size=20,
                                      font_name=pygame_menu.font.FONT_PT_SERIF,
                                      font_color=(0, 0, 0), padding=0)
            self.deckcreatoryellow_menu.add.button(card, submenu) #adding button for every card that calls the submenu for that card

            submenu.add.button("add   " + card.get_name(), yellowdeckappend, card) 
            submenu.add.button("Back", pygame_menu.events.BACK)

        #The code below is the very jank 'show cards in my deck' screen
        submenu_yellow = pygame_menu.Menu("Cards In Deck", height=1000, width=1920, theme=main_menu_theme,
                                    mouse_motion_selection=True)
        submenu_yellow.add.vertical_margin(40)  # Bottom margin

        self.deckcreatoryellow_menu.add.button("Show Cards in Deck", submenu_yellow)

        def showcardsyellow():
            for card in self.yellowdeck.get_copy():
                submenu_yellow.add.label(card)


        submenu_yellow.add.button('Populate chosen cards',showcardsyellow)
        submenu_yellow.add.button('Save Current Deck', self.save_yellow)
        submenu_yellow.add.button('Back', pygame_menu.events.BACK)




        # for card in yellowdeck:
        #     print('yellow deck: ')


        #print(card.get_name(), end=" ")
        # self.deckcreatoryellow_menu.add.button("Current Deck", self.yellowdeckcontains_menu)
        self.deckcreatoryellow_menu.add.button('back', pygame_menu.events.BACK)

        # -------------------------------------------------------------------------
        # Create menus: Naming Blue Menu
        # -------------------------------------------------------------------------

        self.nameblue_menu = pygame_menu.Menu(
            height=1000, width=1920,
            theme=main_menu_theme,
            title='Name Deck',

            )

        self.nameblue_menu.add.text_input('Deck Name: ', maxchar=10, onreturn=self.name_blue)
        self.nameblue_menu.add.button('Press enter to save, then Continue', self.deckcreatorblue_menu)
        self.nameblue_menu.add.button('back', pygame_menu.events.BACK)

        # -------------------------------------------------------------------------
        # Create menus: Naming Yellow Menu
        # -------------------------------------------------------------------------

        self.nameyellow_menu = pygame_menu.Menu(
            height=1000, width=1920,
            theme=main_menu_theme,
            title='Name Deck',
            )

        self.nameyellow_menu.add.text_input('Deck Name: ', maxchar=10, onreturn=self.name_yellow)
        self.nameyellow_menu.add.button('Press enter to save, then Continue', self.deckcreatoryellow_menu)
        self.nameyellow_menu.add.button('back', pygame_menu.events.BACK)

        # -------------------------------------------------------------------------
        # Create menus: pick color
        # -------------------------------------------------------------------------

        self.pickcolor_menu = pygame_menu.Menu(
            height=1000, width=1920,
            theme=main_menu_theme,
            title='Select the Deck Color',

            )
        self.pickcolor_menu.add.button('Blue', self.nameblue_menu)
        self.pickcolor_menu.add.button('Yellow', self.nameyellow_menu)
        self.pickcolor_menu.add.button('back', pygame_menu.events.BACK)

        # -------------------------------------------------------------------------
        # Create menus: Deck Selector
        # -------------------------------------------------------------------------

        self.deckselector_menu = pygame_menu.Menu(
            height=1000, width=1920,
            onclose=pygame_menu.events.EXIT,  # User press ESC button
            theme=main_menu_theme,
            title='Deck Selector',

        )
        # Selectable items
        items = [(self.get_blue_name(), self.save_blue), (self.get_yellow_name(), self.save_yellow)]

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
            height=1000, width=1920,
            onclose=pygame_menu.events.EXIT,  # User press ESC button
            theme=main_menu_theme,
            title='Main menu',

        )


        self.play_button = self.main_menu.add.button('Play', self.main_menu.disable) #This is where the gameboard is being called
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

        self.clock.tick(self.FPS)
        self.main_menu.mainloop(self.surface, disable_loop=test)

    def name_blue(self, value):
        print("Renamed the blue deck to", value)
        self.bluedeck.set_name(value)

    def name_yellow(self, value):
        print("Renamed the yellow deck to", value)
        self.yellowdeck.set_name(value)

    def check_blue(self):
        if self.bluedeck.get_name() == "Blue":
            # Prompt them to hit enter
            print("Need to redirect")
            pass
        else:
            print("Trying to render")
            self.deckcreatorblue_menu

    def save_blue(self):
        self.bluedeck.save_deck()

    def save_yellow(self):
        self.yellowdeck.save_deck()

    def get_yellow_name(self):
        return self.yellowdeck.get_name()

    def get_blue_name(self):
        return self.bluedeck.get_name()

def main_menu(test: bool = False) -> 'MenuSystem':

    mainmenu = MenuSystem()
    mainmenu.mainloop(test)
    return MenuSystem


if __name__ == '__main__':
    main_menu()




