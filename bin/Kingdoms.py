# Required imports, pygame, PyOpenGl (OpenGL is the name of the class in the package), eventually steamworkspy (not yet)
# Pygame
import pygame
from pygame.locals import *
# This must be run for pygame to function
pygame.init()

# typical OpenGL functions
from OpenGL.GL import *
# More advanced ones
from OpenGL.GLU import *

# SteamworksPy

# other imports
import os


# Testing creating a pygame window and putting a few boxes on it, (500,500) is the size
#window = pygame.display.set_mode((500,500))
# The caption Display is  what it says at the top so to say Kingdoms would just use this command with Kingdoms
#pygame.display.set_caption("First Game")
# Anything below here is probably going to be in a loop
# time delay so that main loop doesn't run literally as fast as possible, in ms
# pygame.time.delay(100)
# # This checks for events, anything that happens from the user is an event, stored in pygame.event.get(), running this in a for loop is the best idea
# for event in pygame.event.get():
#     # this one's pretty important, this checks if the user hits the red button on the corner
#     if event.type == pygame.QUIT:
#         # this will close the window
#         pygame.quit()


# Testing imports for decks and cards
from bin.pyfiles.Deck import Deck
from bin.pyfiles.cardclasses.Card import Card
from bin.pyfiles.cardclasses.NonAttackCard import NonAttackCard
import bin.pyfiles.cardclasses.CardConstructor as cc
print(os.getcwd())
master_deck = cc.load_all_cards(os.getcwd() + "\cards")
card2 = master_deck.draw_card()
while card2 != None:
    print("Details about " + str(card2))
    card2.print_all_details()
    card2 = master_deck.draw_card()
deck = Deck("Testing")
card = Card()
deck.add_card(card)
deck.save_deck()

pygame.quit()