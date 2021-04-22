# Required imports, pygame, PyOpenGl (OpenGL is the name of the class in the package), eventually steamworkspy (not yet)
# Using os.system to install required modules
import os
# Install the required packages
os.system("py -m pip install pygame")
# os.system("py -m pip install pyopengl")
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

# Disabled because OpenGL needs to be there for steam and we are not using steam right now
# # typical OpenGL functions
# from OpenGL.GL import *
# # More advanced ones
# from OpenGL.GLU import *

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
# screen = pygame.display.set_mode((500,500), DOUBLEBUF|OPENGL) # Use openGL to do the rendering so that we can have the steam overlay (not implimented yet)



# other imports
from pyfiles.Deck import Deck
from pyfiles.gameclasses.gameloop import *
from pyfiles.menus.mainmenu import MenuSystem, main_menu
from pyfiles.menus.gameboard import Gameboard
from pyfiles.Visualizer import Visualizer
# this is Logan testing visualizer stuff




import pyfiles.cardclasses.CardConstructor as cc

screen = pygame.display.set_mode((1800,900), RESIZABLE)
pygame.display.set_caption("Kingdoms")

def main():
    logging.info(os.getcwd() +  " is the current working directory for the root")
    logging.info("Creating the master deck")
    master_deck = Deck("Master")
    cc.load_all_cards(os.getcwd() + "\cards", master_deck)
    master_deck.save_deck()

    # Testing the effect processor
    for card in master_deck.get_copy():
        if card.get_effects():
            print(card.get_name(), "contains the effects:", card.get_effects())
            card.process_effects()
        if card.get_activated_effects():
            print(card.get_name(), "contains the activated effects:", card.get_activated_effects())

    # Creates 20 mountains and 20 islands in separate decks
    #create_basic_terra_decks(master_deck)

    main2 = MenuSystem(master_deck)
    main2.mainloop(False)


    saved_decks = load_saved_decks()
    run_game(saved_decks, screen)

def load_saved_decks():
    save_file_path = os.getcwd() + "\saves"
    dont_load = ["supreme-potato.txt"]
    decks = []
    for deck_name in os.listdir(save_file_path):
        if deck_name not in dont_load:
            deck_name = deck_name.split(".json")
            deck_name = deck_name[0] # We only care about the name, not anything after .json
            deck = Deck(deck_name)
            deck.load_deck()
            #print(deck.get_name(), "is", len(deck.get_copy()), "cards long")
            decks.append(deck)
    return decks

def delete_saved_deck(deck):
    deck.delete_deck()

# Visualizer test code
    # visualizerTesting = TestVisualizer(master_deck_full_list[12], screen)
    # visualizerTesting2 = TestVisualizer(master_deck_full_list[15], screen)
    # visualizerTesting2.set_master_x(visualizerTesting2.get_master_x() + 500)
    # visualizerTesting3 = TestVisualizer(master_deck_full_list[7], screen)
    # visualizerTesting3.set_master_x(visualizerTesting3.get_master_x() + 1000)
    # # visualizer3 = Visualizer(bastions[0], screen)
    # # visualizer3.set_master_x(visualizer3.get_master_x() + 1000)
    # running = True
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    #
    #     screen.fill((155, 155, 155))
    #     # True/False determines whether or not the card should be rotated
    #     visualizerTesting.visualizer(False)
    #     visualizerTesting2.scale_card_up(False)
    #     visualizerTesting3.scale_card_up(True)
    #     # visualizer3.visualizer()
    #     pygame.display.update()

    # DISABLE THIS TO NOT SEE EVERY CARD EVERY TIME YOU CLOSE THE 3 CARDS ON ONE SCREEN EXAMPLE!
    # visualize_all_cards(master_deck_full_list)
    # pygame.quit()

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