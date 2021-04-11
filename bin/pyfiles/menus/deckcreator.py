import pygame
import sys
from tkinter import *

from pygame.locals import *
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

from typing import Any
from functools import partial

FPS = 30
WINDOW_SIZE = (800, 600)


def on_button_click(value: str, text: Any = None) -> None:
    """
    Button event on menus.
    :param value: Button value
    :param text: Button text
    :return: None
    """
    if not text:
        print('Hello from {}'.format(value))
    else:
        print('Hello from {} with {}'.format(text, value))


def paint_background(surface: 'pygame.Surface') -> None:
    """
    Paints a given surface with background color.
    :param surface: Pygame surface
    :return: None
    """
    surface.fill((128, 230, 198))


def make_long_menu() -> 'pygame_menu.Menu':
    """
    Create a long scrolling menu.
    :return: Menu
    """
    theme_menu = pygame_menu.themes.THEME_BLUE.copy()
    theme_menu.scrollbar_cursor = pygame_menu.locals.CURSOR_HAND

    # Main menu, pauses execution of the application
    menu = pygame_menu.Menu(
        height=400,
        onclose=pygame_menu.events.EXIT,
        theme=theme_menu,
        title='Main Menu',
        width=600
    )

    menu_sub = pygame_menu.Menu(
        columns=4,
        height=400,
        onclose=pygame_menu.events.EXIT,
        rows=3,
        theme=pygame_menu.themes.THEME_GREEN,
        title='Menu with columns',
        width=600
    )

    menu_contributors = pygame_menu.Menu(
        height=400,
        onclose=pygame_menu.events.EXIT,
        theme=pygame_menu.themes.THEME_SOLARIZED,
        title='Contributors',
        width=600
    )

    # Add table to contributors
    table_contrib = menu_contributors.add.table()
    table_contrib.default_cell_padding = 5
    table_contrib.default_row_background_color = 'white'
    bold_font = pygame_menu.font.FONT_OPEN_SANS_BOLD
    table_contrib.add_row(['N°', 'Github User'], cell_font=bold_font)
    for i in range(len(pygame_menu.__contributors__)):
        table_contrib.add_row([i + 1, pygame_menu.__contributors__[i]],
                              cell_font=bold_font if i == 0 else None)

    table_contrib.update_cell_style(-1, -1, font_size=15)  # Update all column/row
    table_contrib.update_cell_style(1, [2, -1], font=pygame_menu.font.FONT_OPEN_SANS_ITALIC)

    menu_text = pygame_menu.Menu(
        height=400,
        onclose=pygame_menu.events.EXIT,
        theme=pygame_menu.themes.THEME_DARK,
        title='Text with scroll',
        width=600
    )

    menu.add.button('Rows and Columns', menu_sub)
    menu.add.button('Text scrolled', menu_text)
    menu.add.button('Pygame-menu contributors', menu_contributors)
    menu.add.vertical_margin(20)  # Adds margin

    label1 = 'Button n°{}'
    label2 = 'Text n°{}: '
    for i in range(1, 20):
        if i % 2 == 0:
            menu.add.button(label1.format(i),
                            on_button_click,
                            'Button n°{}'.format(i))
        else:
            menu.add.text_input(label2.format(i),
                                onchange=on_button_click,
                                text='Text n°{}'.format(i))
    menu.add.button('Exit', pygame_menu.events.EXIT)

    label = 'Button n°{}'
    for i in range(1, 11):
        # Test large button
        if i == 5:
            txt = 'This is a very long button!'
        else:
            txt = label.format(100 * i)
        menu_sub.add.button(txt, on_button_click, 100 * i)
    menu_sub.add.button('Back', pygame_menu.events.BACK)

    # noinspection SpellCheckingInspection
    menu_text.add.label(
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod '
        'tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim '
        'veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea '
        'commodo consequat. Duis aute irure dolor in reprehenderit in voluptate '
        'velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat '
        'cupidatat non proident, sunt in culpa qui officia deserunt mollit anim '
        'id est laborum.',
        max_char=33,
        align=pygame_menu.locals.ALIGN_LEFT,
        margin=(0, -1)
    )
    return menu


def main(test: bool = False) -> None:
    """
    Main function.
    :param test: Indicate function is being tested
    :return: None
    """
    screen = create_example_window('Example - Scrolling Menu', WINDOW_SIZE)

    clock = pygame.time.Clock()
    menu = make_long_menu()

    # -------------------------------------------------------------------------
    # Main loop
    # -------------------------------------------------------------------------
    while True:

        # Tick
        clock.tick(FPS)

        # Paint background
        paint_background(screen)

        # Execute main from principal menu if is enabled
        menu.mainloop(
            surface=screen,
            bgfun=partial(paint_background, screen),
            disable_loop=test,
            fps_limit=FPS
        )

        # Update surface
        pygame.display.flip()

        # At first loop returns
        if test:
            break


if __name__ == '__main__':
    main()