from random import randrange
import pygame
import pygame_menu
from pygame_menu.examples import create_example_window

from random import randrange
from typing import Tuple, Any, Optional, List
#
# __all__ = ['main']
#
# import pygame
# import pygame_menu
# from pygame_menu.examples import create_example_window
#
# from typing import Tuple, Optional
#
# # -----------------------------------------------------------------------------
# # Constants and global variables
# # -----------------------------------------------------------------------------
# FPS = 60
# WINDOW_SIZE = (640, 480)
#
# sound: Optional['pygame_menu.sound.Sound'] = None
# surface: Optional['pygame.Surface'] = None
# main_menu: Optional['pygame_menu.Menu'] = None
#
#
# # -----------------------------------------------------------------------------
# # Methods
# # -----------------------------------------------------------------------------
# def main_background() -> None:
#     """
#     Background color of the main menu, on this function user can plot
#     images, play sounds, etc.
#     :return: None
#     """
#     surface.fill((40, 40, 40))
#
#
# def check_name_test(value: str) -> None:
#     """
#     This function tests the text input widget.
#     :param value: The widget value
#     :return: None
#     """
#     print('User name: {0}'.format(value))
#
#
# def update_menu_sound(value: Tuple, enabled: bool) -> None:
#     """
#     Update menu sound.
#     :param value: Value of the selector (Label and index)
#     :param enabled: Parameter of the selector, (True/False)
#     :return: None
#     """
#     assert isinstance(value, tuple)
#     if enabled:
#         main_menu.set_sound(sound, recursive=True)
#         print('Menu sounds were enabled')
#     else:
#         main_menu.set_sound(None, recursive=True)
#         print('Menu sounds were disabled')
#
#
# def main(test: bool = False) -> None:
#     """
#     Main program.
#     :param test: Indicate function is being tested
#     :return: None
#     """
#
#     # -------------------------------------------------------------------------
#     # Globals
#     # -------------------------------------------------------------------------
#     global main_menu
#     global sound
#     global surface
#
#     # -------------------------------------------------------------------------
#     # Create window
#     # -------------------------------------------------------------------------
#     surface = create_example_window('Example - Multi Input', WINDOW_SIZE)
#     clock = pygame.time.Clock()
#
#     # -------------------------------------------------------------------------
#     # Set sounds
#     # -------------------------------------------------------------------------
#     sound = pygame_menu.sound.Sound()
#
#     # Load example sounds
#     sound.load_example_sounds()
#
#     # Disable a sound
#     sound.set_sound(pygame_menu.sound.SOUND_TYPE_ERROR, None)
#
#     # -------------------------------------------------------------------------
#     # Create menus: Settings
#     # -------------------------------------------------------------------------
#     settings_menu_theme = pygame_menu.themes.THEME_DARK.copy()
#     settings_menu_theme.title_offset = (5, -2)
#     settings_menu_theme.widget_alignment = pygame_menu.locals.ALIGN_LEFT
#     settings_menu_theme.widget_font = pygame_menu.font.FONT_OPEN_SANS_LIGHT
#     settings_menu_theme.widget_font_size = 20
#
#     settings_menu = pygame_menu.Menu(
#         height=WINDOW_SIZE[1] * 0.85,
#         theme=settings_menu_theme,
#         title='Settings',
#         width=WINDOW_SIZE[0] * 0.9
#     )
#
#     # Add text inputs with different configurations
#     settings_menu.add.text_input(
#         'First name: ',
#         default='John',
#         onreturn=check_name_test,
#         textinput_id='first_name'
#     )
#     settings_menu.add.text_input(
#         'Last name: ',
#         default='Rambo',
#         maxchar=10,
#         textinput_id='last_name',
#         input_underline='.'
#     )
#     settings_menu.add.text_input(
#         'Your age: ',
#         default=25,
#         maxchar=3,
#         maxwidth=3,
#         textinput_id='age',
#         input_type=pygame_menu.locals.INPUT_INT,
#         cursor_selection_enable=False
#     )
#     settings_menu.add.text_input(
#         'Some long text: ',
#         maxwidth=19,
#         textinput_id='long_text',
#         input_underline='_'
#     )
#     settings_menu.add.text_input(
#         'Password: ',
#         maxchar=6,
#         password=True,
#         textinput_id='pass',
#         input_underline='_'
#     )
#
#     # Selectable items
#     items = [('Easy', 'EASY'),
#              ('Medium', 'MEDIUM'),
#              ('Hard', 'HARD')]
#
#     # Create selector with 3 difficulty options
#     settings_menu.add.selector(
#         'Select difficulty:\t',
#         items,
#         selector_id='difficulty',
#         default=1
#     )
#     settings_menu.add.selector(
#         'Select difficulty fancy',
#         items,
#         selector_id='difficulty_fancy',
#         default=1,
#         style='fancy'
#     )
#     settings_menu.add.dropselect(
#         'Select difficulty (drop)',
#         items,
#         default=1,
#         dropselect_id='difficulty_drop'
#     )
#     settings_menu.add.dropselect_multiple(
#         title='Pick 3 colors',
#         items=[('Black', (0, 0, 0)),
#                ('Blue', (0, 0, 255)),
#                ('Cyan', (0, 255, 255)),
#                ('Fuchsia', (255, 0, 255)),
#                ('Green', (0, 255, 0)),
#                ('Red', (255, 0, 0)),
#                ('White', (255, 255, 255)),
#                ('Yellow', (255, 255, 0))],
#         dropselect_multiple_id='pickcolors',
#         max_selected=3,
#         open_middle=True,
#         selection_box_height=6  # How many options show if opened
#     )
#
#     # Create switch
#     settings_menu.add.toggle_switch('First Switch', False,
#                                     toggleswitch_id='first_switch')
#     settings_menu.add.toggle_switch('Other Switch', True,
#                                     toggleswitch_id='second_switch',
#                                     state_text=('Apagado', 'Encencido'))
#
#     def data_fun() -> None:
#         """
#         Print data of the menu.
#         :return: None
#         """
#         print('Settings data:')
#         data = settings_menu.get_input_data()
#         for k in data.keys():
#             print(u'\t{0}\t=>\t{1}'.format(k, data[k]))
#
#     settings_menu.add.clock(clock_format='%Y/%m/%d %H:%M', title_format='Clock: {0}')
#     settings_menu.add.button('Store data', data_fun)  # Call function
#     settings_menu.add.button('Restore original values', settings_menu.reset_value)
#     settings_menu.add.button('Return to main menu', pygame_menu.events.BACK,
#                              align=pygame_menu.locals.ALIGN_CENTER)
#
#     # -------------------------------------------------------------------------
#     # Create menus: More settings
#     # -------------------------------------------------------------------------
#     more_settings_menu = pygame_menu.Menu(
#         height=WINDOW_SIZE[1] * 0.85,
#         theme=settings_menu_theme,
#         title='More Settings',
#         width=WINDOW_SIZE[0] * 0.9
#     )
#
#     more_settings_menu.add.image(
#         pygame_menu.baseimage.IMAGE_EXAMPLE_PYGAME_MENU,
#         scale=(0.25, 0.25),
#         align=pygame_menu.locals.ALIGN_CENTER
#     )
#     more_settings_menu.add.color_input(
#         'Color 1 RGB: ',
#         color_type='rgb'
#     )
#     more_settings_menu.add.color_input(
#         'Color 2 RGB: ',
#         color_type='rgb',
#         default=(255, 0, 0),
#         input_separator='-'
#     )
#
#     def print_color(color: Tuple) -> None:
#         """
#         Test onchange/onreturn.
#         :param color: Color tuple
#         :return: None
#         """
#         print('Returned color: ', color)
#
#     more_settings_menu.add.color_input(
#         'Color in Hex: ',
#         color_type='hex',
#         hex_format='lower',
#         onreturn=print_color
#     )
#
#     more_settings_menu.add.vertical_margin(25)
#     more_settings_menu.add.button(
#         'Return to main menu',
#         pygame_menu.events.BACK,
#         align=pygame_menu.locals.ALIGN_CENTER
#     )
#
#     # -------------------------------------------------------------------------
#     # Create menus: Column buttons
#     # -------------------------------------------------------------------------
#     button_column_menu_theme = pygame_menu.themes.THEME_ORANGE.copy()
#     button_column_menu_theme.background_color = pygame_menu.BaseImage(
#         image_path=pygame_menu.baseimage.IMAGE_EXAMPLE_GRAY_LINES,
#         drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY
#     )
#     button_column_menu_theme.widget_font_size = 25
#
#     button_column_menu = pygame_menu.Menu(
#         columns=2,
#         height=WINDOW_SIZE[1] * 0.45,
#         rows=3,
#         theme=button_column_menu_theme,
#         title='Textures+Columns',
#         width=WINDOW_SIZE[0] * 0.9
#     )
#     for i in range(4):
#         button_column_menu.add.button('Button {0}'.format(i), pygame_menu.events.BACK)
#     button_column_menu.add.button(
#         'Return to main menu', pygame_menu.events.BACK,
#         background_color=pygame_menu.BaseImage(
#             image_path=pygame_menu.baseimage.IMAGE_EXAMPLE_METAL
#         )
#     ).background_inflate_to_selection_effect()
#
#     # -------------------------------------------------------------------------
#     # Create menus: Main menu
#     # -------------------------------------------------------------------------
#     main_menu_theme = pygame_menu.themes.THEME_DARK.copy()
#     main_menu_theme.title_font = pygame_menu.font.FONT_COMIC_NEUE
#     main_menu_theme.widget_font = pygame_menu.font.FONT_COMIC_NEUE
#     main_menu_theme.widget_font_size = 30
#
#     main_menu = pygame_menu.Menu(
#         height=WINDOW_SIZE[1] * 0.7,
#         onclose=pygame_menu.events.EXIT,  # User press ESC button
#         theme=main_menu_theme,
#         title='Main menu',
#         width=WINDOW_SIZE[0] * 0.8
#     )
#
#     main_menu.add.button('Settings', settings_menu)
#     main_menu.add.button('More Settings', more_settings_menu)
#     main_menu.add.button('Menu in textures and columns', button_column_menu)
#     main_menu.add.selector('Menu sounds ',
#                            [('Off', False), ('On', True)],
#                            onchange=update_menu_sound)
#     main_menu.add.button('Quit', pygame_menu.events.EXIT)
#
#     # -------------------------------------------------------------------------
#     # Main loop
#     # -------------------------------------------------------------------------
#     while True:
#
#         # Tick
#         clock.tick(FPS)
#
#         # Paint background
#         main_background()
#
#         # Main menu
#         main_menu.mainloop(surface, main_background, disable_loop=test, fps_limit=FPS)
#
#         # Flip surface
#         pygame.display.flip()
#
#         # At first loop returns
#         if test:
#             break
#
#
# if __name__ == '__main__':
#     main()


__all__ = ['main']

import pygame
import pygame_menu
from pygame_menu.examples import create_example_window

import math
from typing import Dict, Any


class App(object):
    """
    The following object creates the whole app.
    """
    image_widget: 'pygame_menu.widgets.Image'
    item_description_widget: 'pygame_menu.widgets.Label'
    menu: 'pygame_menu.Menu'
    modes: Dict[int, Dict[str, Any]]
    quit_button: 'pygame_menu.widgets.Button'
    quit_button_fake: 'pygame_menu.widgets.Button'
    selector_widget: 'pygame_menu.widgets.Selector'
    surface: 'pygame.Surface'

    def __init__(self) -> None:
        """
        Constructor.
        """
        self.surface = create_example_window('Example - Dynamic Widget Update',
                                             (640, 480), flags=pygame.NOFRAME)

        # Load image
        default_image = pygame_menu.BaseImage(
            image_path=pygame_menu.baseimage.IMAGE_EXAMPLE_PYGAME_MENU
        ).scale(0.2, 0.2)

        # Set theme
        theme = pygame_menu.themes.THEME_DEFAULT.copy()
        theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_UNDERLINE_TITLE
        theme.title_close_button_cursor = pygame_menu.locals.CURSOR_HAND
        theme.title_font_color = (35, 35, 35)

        # This dict stores the values of the widgets to be changed dynamically
        self.modes = {
            1: {
                'image': default_image.copy(),
                'label': {
                    'color': theme.widget_font_color,
                    'size': theme.widget_font_size,
                    'text': 'The first one is very epic'
                }
            },
            2: {
                'image': default_image.copy().to_bw(),
                'label': {
                    'color': (0, 0, 0),
                    'size': 20,
                    'text': 'This other one is also epic, but fancy'
                }
            },
            3: {
                'image': default_image.copy().flip(False, True).pick_channels('r'),
                'label': {
                    'color': (255, 0, 0),
                    'size': 45,
                    'text': 'YOU D I E D'
                }
            }
        }

        # Create menus
        self.menu = pygame_menu.Menu(
            height=480,
            onclose=pygame_menu.events.CLOSE,
            theme=theme,
            title='Everything is dynamic now',
            width=640
        )

        self.selector_widget = self.menu.add.selector(
            title='Pick one option: ',
            items=[('The first', 1),
                   ('The second', 2),
                   ('The final mode', 3)],
            onchange=self._on_selector_change
        )

        self.image_widget = self.menu.add.image(
            image_path=self.modes[1]['image'],
            padding=(25, 0, 0, 0)  # top, right, bottom, left
        )

        self.item_description_widget = self.menu.add.label(title='')

        self.quit_button = self.menu.add.button('Quit', pygame_menu.events.EXIT)

        self.quit_button_fake = self.menu.add.button('You cannot quit', self.fake_quit,
                                                     font_color=(255, 255, 255))
        self.quit_button_fake.add_draw_callback(self.animate_quit_button)

        # Update the widgets based on selected value from selector get_value
        # returns selected item tuple and index, so [0][1] means the second object
        # from ('The first', 1) tuple
        self._update_from_selection(int(self.selector_widget.get_value()[0][1]))

    def animate_quit_button(
            self,
            widget: 'pygame_menu.widgets.Widget',
            menu: 'pygame_menu.Menu'
    ) -> None:
        """
        Animate widgets if the last option is selected.
        :param widget: Widget to be updated
        :param menu: Menu
        :return: None
        """
        if self.current == 3:
            t = widget.get_counter_attribute('t', menu.get_clock().get_time() * 0.0075, math.pi)
            widget.set_padding(10 * (1 + math.sin(t)))  # Oscillating padding
            widget.set_background_color((int(125 * (1 + math.sin(t))), 0, 0), None)
            c = int(127 * (1 + math.cos(t)))
            widget.update_font({'color': (c, c, c)})  # Widget font now is in grayscale
            # widget.translate(10 * math.cos(t), 10 * math.sin(t))
            widget.rotate(5 * t)

    @staticmethod
    def fake_quit() -> None:
        """
        Function executed by fake quit button.
        :return: None
        """
        print('I said that you cannot quit')

    def _update_from_selection(self, index: int) -> None:
        """
        Change widgets depending on index.
        :param index: Index
        :return: None
        """
        self.current = index
        self.image_widget.set_image(self.modes[index]['image'])
        self.item_description_widget.set_title(self.modes[index]['label']['text'])
        self.item_description_widget.update_font(
            {'color': self.modes[index]['label']['color'],
             'size': self.modes[index]['label']['size']}
        )
        # Swap buttons using hide/show
        if index == 3:
            self.quit_button.hide()
            self.quit_button_fake.show()
        else:
            self.quit_button.show()
            self.quit_button_fake.hide()

    def _on_selector_change(self, selected: Any, value: int) -> None:
        """
        Function executed if selector changes.
        :param selected: Selector data containing text and index
        :param value: Value from the selected option
        :return: None
        """
        print('Selected data:', selected)
        self._update_from_selection(value)

    def mainloop(self, test: bool) -> None:
        """
        App mainloop.
        :param test: Test status
        """
        self.menu.mainloop(self.surface, disable_loop=test)


def main(test: bool = False) -> 'App':
    """
    Main function.
    :param test: Indicate function is being tested
    :return: App object
    """
    app = App()
    app.mainloop(test)
    return app


if __name__ == '__main__':
    main()