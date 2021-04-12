import pygame
import sys

#
#
# def func():
#     print("Button is clicked")
#
# def delete1():
#     my_listbox.delete(ANCHOR)
#
#
# def delete2():
#     my_listbox2.delete(ANCHOR)
#
# def select():
#     my_label.config(text=my_listbox.get(ANCHOR))
#
# def deckBuilder():
#
#     root = Tk()
#     root.title('ListTesting')
#     root.geometry("800x800")
#
#     my_listbox = Listbox(root, height=25 )
#     my_listbox.pack(side=LEFT,padx=25)
#
#     my_listbox2 = Listbox(root, height=25)
#     my_listbox2.pack(side=RIGHT,padx=25)
#
#
#     for i in range(0,51):
#         my_listbox2.insert(END,"Card "+str( i))
#
#     #add items to the list box
#
#     my_listbox.insert(END, "This is an item")
#     my_listbox.insert(END, "This is an item")
#     my_listbox.insert(END, "This is an item")
#     #adding a list of items
#     my_list=["One", "Two", "Three"]
#
#     for i in my_list:
#         my_listbox.insert(END, i)
#
#     my_listbox.insert(2, "A new thing")
#
#     my_button = Button(root, text="Delete", command=delete1)
#     my_button.pack(side=BOTTOM,pady=10)
#
#     my_button2 = Button(root, text="Select", command=select)
#     my_button2.pack(side=BOTTOM, pady=10)
#
#     my_label = Label(root, text='')
#     my_label.pack(side=BOTTOM,pady=5)
#
#
#     root.mainloop()
# deckBuilder()


__all__ = ['main']

import pygame
import pygame_menu
from pygame_menu.examples import create_example_window
import math
from typing import Dict, Any
import os
from pyfiles.menus.mainmenu import update_menu_sound


class MenuSystem(object):
    """
    The Following Object will create the entire menu system
    """
    image_widget: 'pygame_menu.widgets.Image'
    item_description_widget: 'pygame_menu.widgets.Label'
    main_menu: 'pygame_menu.Menu'
    settings_menu: 'pygame_menu.Menu'
    deckcreatoryellow_menu: 'pygame_menu.Menu'
    deckcreatorblue_menu: 'pygame_menu.Menu'
    pickcolor_menu: 'pygame_menu.Menu'
    play_button: 'pygame_menu.widgets.Button'
    settings_button: 'pygame_menu.widgets.Button'
    deckselector_button: 'pygame_menu.widgets.Button'
    deckcreator_button: 'pygame_menu.widgets.Button'
    quit_button: 'pygame_menu.widgets.Button'
    surface: 'pygame.Surface'
    sound: 'pygame_menu.sound.Sound' = None


    def __init__(self) -> None:
        """
        Constructor.
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

        self.WINDOW_SIZE = (900, 900)
        self.surface = create_example_window('KINGDOMS', (self.WINDOW_SIZE))
        self.clock = pygame.time.Clock()

        '''
        Setting the Theme
        '''
        main_menu_theme = pygame_menu.themes.THEME_SOLARIZED.copy()
        main_menu_theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE
        main_menu_theme.widget_font_color = (75, 75, 75)
        main_menu_theme.title_font = pygame_menu.font.FONT_8BIT
        main_menu_theme.widget_font = pygame_menu.font.FONT_8BIT
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
        #The update_menu_soundn is breaking everything :( will need to ask the team if they know what is goingn on with that

        # self.settings_menu.add.selector('Menu sounds ',
        #                            [('Off', False), ('On', True)],
        #                            onchange=update_menu_sound)
        self.settings_menu.add.button('back', pygame_menu.events.BACK)
        # -------------------------------------------------------------------------
        # Create menus: Deck Creator Yellow
        # -------------------------------------------------------------------------

        self.deckcreatorblue_menu = pygame_menu.Menu(
            height=self.WINDOW_SIZE[1] * 1,
            theme=main_menu_theme,
            title='Settings',
            width=self.WINDOW_SIZE[1] * 1
            )
        # this needs to be changed so that it pulls the description from each card
        cardinfo = "This is where the information for each picked card will be added"
        bluecardlist = ["Avren the Spellsword", "Argon The Telekinetic", "Magi Tower", "Ward Magi", "Ethereal Shield",
                        "Pyro Magi Warrior", "Elder Magi", "Magi Freshman", "Island", "Hired Pirate", "Hired Assassin",
                        "Lucid Mind", "Pluck",
                        "Crack", "The Bigger They Are", "Counter", "Lotus Shrine", "The Rock", "Shrine of Greed"]



        for i in bluecardlist:
            submenu = pygame_menu.Menu(i, 750, 750, theme=main_menu_theme,
                                       mouse_motion_selection=True, center_content=False)
            submenu.add.vertical_margin(75)
            submenu.add.label('Description', align=pygame_menu.locals.ALIGN_LEFT,
                              font_name=pygame_menu.font.FONT_OPEN_SANS_BOLD,
                              margin=(5, 10))
            label = submenu.add.label(cardinfo, max_char=70,
                                      align=pygame_menu.locals.ALIGN_LEFT,
                                      margin=(29, 1), font_size=20,
                                      font_name=pygame_menu.font.FONT_PT_SERIF,
                                      font_color=(0, 0, 0), padding=0)
            self.deckcreatorblue_menu.add.button(i, submenu)
            submenu.add.vertical_margin(40)  # Bottom margin

            submenu.add.button("Add " + i + " to Deck")


        # -------------------------------------------------------------------------
        # Create menus: Deck Creator Yellow
        # -------------------------------------------------------------------------

        self.deckcreatoryellow_menu = pygame_menu.Menu(
            height=self.WINDOW_SIZE[1] * 1,
            theme=main_menu_theme,
            title='Settings',
            width=self.WINDOW_SIZE[1] * 1
            )
        # this needs to be changed so that it pulls the description from each card
        cardinfo = "This is where the information for each picked card will be added"
        yellowcardlist = ["Aries Lord of Battle", "Heath The Prideful", "Dwarven Kingdom", "Big Shield Dwarf",
                          "Dwarven Scholar", "Relaxed Dwarf", "Catapult Squad", "Dwarven Champion", "Hired Pirate",
                          "Hired Assassin", "Speed Scroll", "Dirty Contracts", "Lost Armory",
                          "Crystal Projector", "After the Storm", "Lotus Shrine", "The Rock", "Shrine Of Greed"]



        for i in yellowcardlist:
            submenu = pygame_menu.Menu(i, 750, 750, theme=main_menu_theme,
                                       mouse_motion_selection=True, center_content=False)
            submenu.add.vertical_margin(75)
            submenu.add.label('Description', align=pygame_menu.locals.ALIGN_LEFT,
                              font_name=pygame_menu.font.FONT_OPEN_SANS_BOLD,
                              margin=(5, 10))
            label = submenu.add.label(cardinfo, max_char=70,
                                      align=pygame_menu.locals.ALIGN_LEFT,
                                      margin=(29, 1), font_size=20,
                                      font_name=pygame_menu.font.FONT_PT_SERIF,
                                      font_color=(0, 0, 0), padding=0)
            self.deckcreatoryellow_menu.add.button(i, submenu)
            submenu.add.vertical_margin(40)  # Bottom margin

            submenu.add.button("Add " + i + " to Deck")

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
        self.deckselector_button = self.main_menu.add.button('Deck Selector')
        self.settings_button = self.main_menu.add.button('Settings', self.settings_menu)
        self.quit_button = self.main_menu.add.button('Quit', pygame_menu.events.EXIT)




    def mainloop(self, test: bool) -> None:
        """
        APP MAIN LOOP

        :param test:
        :return:
        """
        self.main_menu.mainloop(self.surface, disable_loop=test)


def main(test: bool = False) -> 'MenuSystem':
    """
    MAIN FUNCTION
    :param test: Indicate function is being tested
    :return: App Object
    """
    mainmenu = MenuSystem()
    mainmenu.mainloop(test)
    return MenuSystem


if __name__ == '__main__':
    main()


