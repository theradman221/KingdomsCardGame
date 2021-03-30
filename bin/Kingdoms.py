# Required imports, pygame, PyOpenGl (OpenGL is the name of the class in the package), eventually steamworkspy (not yet)
# Pygame
import pygame
from pygame.locals import *
import sys
# This must be run for pygame to function
pygame.init()


# typical OpenGL functions
from OpenGL.GL import *
# More advanced ones
from OpenGL.GLU import *

# # SteamworksPy
import os
os.add_dll_directory(os.getcwd())

from steamworks import STEAMWORKS

steamworks = STEAMWORKS()
steamworks.initialize()

my_steam64 = steamworks.Users.GetSteamID()
my_steam_level = steamworks.Users.GetPlayerSteamLevel()

print(f'Logged on as {my_steam64}, level: {my_steam_level}')
print('Is subscribed to current app?', steamworks.Apps.IsSubscribed())

# other imports
import os
from pyfiles.Deck import Deck
from pyfiles.guielements.Background import Background

# Testing creating a pygame window and putting a few boxes on it, (500,500) is the size
screen = pygame.display.set_mode((500,500))
# The caption Display is  what it says at the top so to say Kingdoms would just use this command with Kingdoms
pygame.display.set_caption("First Game")
# Anything below here is probably going to be in a loop
# time delay so that main loop doesn't run literally as fast as possible, in ms
# pygame.time.delay(100)
# # This checks for events, anything that happens from the user is an event, stored in pygame.event.get(), running this in a for loop is the best idea




# Testing imports for decks and cards

from pyfiles.cardclasses.Card import Card
from pyfiles.cardclasses.NonAttackCard import NonAttackCard
import pyfiles.cardclasses.CardConstructor as cc

def main():
    print(os.getcwd())
    master_deck = cc.load_all_cards(os.getcwd() + "\cards")
    master_deck.save_deck()
    card2 = master_deck.draw_card()
    while card2 != None:
        print("Details about " + str(card2))
        #card2.print_all_details()
        card2 = master_deck.draw_card()
    master_copy = master_deck.load_deck("Master")
    master_copy_deck = load_deck("Master", cc)
    print_deck(master_copy_deck)

    #pygame.quit()

def load_deck(name2, cc):
    deck = Deck(name2)
    dict = deck.load_deck(name2)
    master_dict = dict[name2]
    for key in master_dict:
        new = cc.convert_file_to_card(master_dict[key])
        deck.add_card(new)
    return deck

def print_deck(deck):
    print("These are the cards contained in " + deck.get_name())
    card = deck.draw_card()
    while card != None:
        print(card)
        card = deck.draw_card()

def game_loop():
    run = True
    print(os.getcwd() + "\menubackgrounds\\" + 'background.jpg')
    backround = Background(os.getcwd() + "\menubackgrounds\\" + "background.png", [0, 0])
    while run:
        screen.fill([255, 255, 255])
        screen.blit(backround.image, backround.rect)
        for event in pygame.event.get():
            # this one's pretty important, this checks if the user hits the red button on the corner
            if event.type == pygame.QUIT:
                # this will close the window
                run = False
                pygame.quit()
        print("Finished the game loop once")
        pygame.time.delay(1000)
    pygame.quit()

def test_loop():
    bif = "bluebastiontemplate.jpg"
    mif = "bg.png"

    pygame.init()
    screen = pygame.display.set_mode((1220, 980), 0, 32)

    backround = pygame.image.load(bif).convert()
    mouse_c = pygame.image.load(mif).convert_alpha()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(backround, (0, 0))

        x, y = pygame.mouse.get_pos()
        x -= mouse_c.get_width() / 2
        y - + mouse_c.get_height() / 2

        screen.blit(mouse_c, (x, y))

        pygame.display.update()

main()
#game_loop() # Doesn't work at all for some reason
test_loop()
