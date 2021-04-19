# Required imports, pygame, PyOpenGl (OpenGL is the name of the class in the package), eventually steamworkspy (not yet)
# Using os.system to install required modules
import os
# Install the required packages
os.system("py -m pip install pygame")
os.system("py -m pip install pyopengl")
os.system("py -m pip install pygame-menu")


import logging
import datetime
import time
import pygame
from pygame.locals import *
import sys
# This must be run for pygame to function
pygame.init()

# Erase the previous log
try:
    file = open("log\kingdoms_log.log", "r+")
    file.truncate(0)
    file.close()
except FileNotFoundError: # If it fails just move on since it would mean that's the first time running
    pass

# Setup the logging file
logging.basicConfig(filename="log\kingdoms_log.log", level=logging.INFO)
# Different logging types
logging.info('starting at ' + str(datetime.datetime.now()))
# logging.error('your text goes here')
# logging.debug('your text goes here')


# typical OpenGL functions
from OpenGL.GL import *
# More advanced ones
from OpenGL.GLU import *

# # SteamworksPy, Disabled for bughunt day as it's integration is not even started
# import os
# os.add_dll_directory(os.getcwd())
#
# from steamworks import STEAMWORKS
#
# steamworks = STEAMWORKS()
# steamworks.initialize()
# logging.info('Steam was initialized')
#
# my_steam64 = steamworks.Users.GetSteamID()
# my_steam_level = steamworks.Users.GetPlayerSteamLevel()
# logging.info("The user is Logged in : " + str(steamworks.Users.LoggedOn()))
# steamworks.Friends.ActivateGameOverlay("friends")
#
# logging.info(f'Logged on as {my_steam64}, level: {my_steam_level}')
# logging.info('Is subscribed to current app? ' + str(steamworks.Apps.IsSubscribed()))



# other imports
from pyfiles.Deck import Deck
from pyfiles.guielements.Background import Background
from pyfiles.gameclasses.gameloop import *
from pyfiles.menus.mainmenu import MenuSystem, main_menu
from pyfiles.Visualizer2 import Visualizer

# Testing creating a pygame window and putting a few boxes on it, (500,500) is the size
# screen = pygame.display.set_mode((500,500), DOUBLEBUF|OPENGL) # Use openGL to do the rendering so that we can have the steam overlay (not implimented yet)
screen = pygame.display.set_mode((1800,900))
#
# # The caption Display is  what it says at the top so to say Kingdoms would just use this command with Kingdoms
# pygame.display.set_caption("First Game")
# Anything below here is probably going to be in a loop
# time delay so that main loop doesn't run literally as fast as possible, in ms
# pygame.time.delay(100)
# # This checks for events, anything that happens from the user is an event, stored in pygame.event.get(), running this in a for loop is the best idea




# Testing imports for decks and cards

from pyfiles.cardclasses.Card import Card
from pyfiles.cardclasses.NonAttackCard import NonAttackCard
import pyfiles.cardclasses.CardConstructor as cc
from pyfiles.AttackProcessor import AttackProcessor



def main():

    logging.info(os.getcwd() +  " is the current working directory for the root")
    logging.info("Creating the master deck")
    master_deck = Deck("Master")
    cc.load_all_cards(os.getcwd() + "\cards", master_deck)
    master_deck_full = Deck("Master-Full")
    master_deck_full_list = master_deck.get_copy()
    master_deck_full.set_deck(master_deck_full_list)
    master_deck.save_deck()
    master_copy_deck = Deck("Master")
    master_copy_deck.load_deck()
    master_copy_deck.set_name("Master-Copy")
    master_copy_deck.save_deck()
    # print("Successfully copied it!")
    master_copy_deck.print_deck()
    ap = AttackProcessor(master_deck.draw_card(), master_deck.draw_card())

    # New test deck for testing the bastions and royals
    test_deck = Deck("Testing")
    test_deck.set_deck(master_deck.get_copy())
    test_deck.add_bastion(master_deck.draw_card())
    test_deck.set_royal_1(master_deck.draw_card())
    test_deck.set_royal_2(master_deck.draw_card())
    test_deck.save_deck()
    # print("This is the test deck's bastion", test_deck.get_bastion())
    # print("This is the test deck's Royal1", test_deck.get_royal_1())
    # print("This is the test deck's Royal2", test_deck.get_royal_2())
    test_load = Deck("Testing")
    test_load.load_deck()
    # print("testing loading, the bastion is", test_load.get_bastion())
    # print("testing loading, the first royal is", test_load.get_royal_1())
    # print("testing loading, the second royal is", test_load.get_royal_2())

    all_units = master_deck.filter_by_unit_inverted(["Terra", "Terra-Landmark"])
    all_units_deck = Deck("Units")
    all_units_deck.set_deck(all_units)
    bastions = master_copy_deck.filter_by_unit(["Bastion"])
    hero = master_copy_deck.filter_by_unit(["Hero"])
    all_units_deck.add_bastion(bastions[0])
    all_units_deck.set_royal_1(hero[0])
    all_units_deck.set_royal_2(hero[1])

    visualizer = Visualizer(hero[1], screen)

    visualizer2 = Visualizer(master_deck_full_list[12], screen)
    visualizer2.set_master_x(visualizer2.get_master_x() + 500)
    visualizer3 = Visualizer(bastions[0], screen)
    visualizer3.set_master_x(visualizer3.get_master_x() + 1000)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # screen.fill((155, 155, 155))
        # visualizer3.visualizer()
        # visualizer.visualizer()
        # visualizer2.visualizer()
        # pygame.display.update()

    # DISABLE THIS TO NOT SEE EVERY CARD EVERY TIME YOU CLOSE THE 3 CARDS ON ONE SCREEN EXAMPLE!
    visualize_all_cards(master_deck_full_list)
    pygame.quit()

    for card in all_units_deck.get_copy():
        all_units_deck.add_card(card)
        if all_units_deck.deck_size() >= 40:
            break

    all_units_deck.save_deck()
    print(all_units_deck)

    # Test emptying the full deck with .remove(card)
    # for card in master_deck_full.get_copy():
    #     print(card, end=" ")
    # print("\n\n")
    # for card in master_deck_full.get_copy():
    #     master_deck_full.remove_card(card)
    #     print(card)
    #     print(master_deck_full)


    #create_basic_terra_decks(master_deck)
    main2 = MenuSystem(master_deck_full)
    main2.mainloop(False)
    #ap.processAttack()
    saved_decks = load_saved_decks()
    run_game(saved_decks)

def load_saved_decks():
    save_file_path = os.getcwd() + "\saves"
    decks = []
    for deck_name in os.listdir(save_file_path):
        deck_name = deck_name.split(".json")
        deck_name = deck_name[0] # We only care about the name, not anything after .json
        deck = Deck(deck_name)
        deck.load_deck()
        #print(deck.get_name(), "is", len(deck.get_copy()), "cards long")
        decks.append(deck)
    return decks

def delete_saved_deck(deck):
    deck.delete_deck()

# Does not work right now, I think it's the background class breaking it
# def game_loop():
#     run = True
#     print(os.getcwd() + "\menubackgrounds\\" + 'background.jpg')
#     backround = Background(os.getcwd() + "\menubackgrounds\\" + "background.png", [0, 0])
#     while run:
#         screen.fill([255, 255, 255])
#         screen.blit(backround.image, backround.rect)
#         for event in pygame.event.get():
#             # this one's pretty important, this checks if the user hits the red button on the corner
#             if event.type == pygame.QUIT:
#                 # this will close the window
#                 run = False
#                 pygame.quit()
#         print("Finished the game loop once")
#         pygame.time.delay(1000)
#     pygame.quit()

def visualize_all_cards(deck):
    for card in deck:
        visualizer = Visualizer(card, screen)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            visualizer.visualizer()
            pygame.display.update()


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

#game_loop() # Doesn't work at all for some reason
#test_loop()

# This is merely to keep the code around in case someone needs to make a terra deck of all 1 kind, this is faster than editing json
def create_basic_terra_decks(master_deck):
    # Create the 2 decks with 20 cards of the Mountain and Island terra
    terra_island = Deck("Terra-Island")
    terra_mountain = Deck("Terra-Mountain")
    island_card = None
    mountain_card = None
    search_deck = master_deck.get_copy()
    for card in search_deck:
        if card.get_name() == "Island":
            island_card = card
        if card.get_name() == "Mountain":
            mountain_card = card

    for i in range(0, 20):
        terra_island.add_card(island_card)
        terra_mountain.add_card(mountain_card)
    terra_island.save_deck()
    terra_mountain.save_deck()

# Adding one good suggestion from bug hunt day
if __name__ == '__main__':
    main()