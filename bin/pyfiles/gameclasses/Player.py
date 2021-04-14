
import os
from pyfiles.Deck import Deck
from pyfiles.cardclasses.Card import Card
from pyfiles.cardclasses.AttackCard import AttackCard

# This class is designed to keep track of information for each player that is required for the game to run correctly
class Player:
    def __init__(self, name):
        self.__name = name

        # These are the main decks, all other decks (or zones) will be populated with cards from these 2 decks (except tokens, they are weird)
        self.__main_deck = None
        self.__terra_deck = None

        # Each player must have a bastion, and 2 royals in the throne room before the game can start
        self.__bastion = None
        self.__throne_1 = None
        self.__throne_1_counter = 0
        self.__throne_2 = None
        self.__throne_2_counter = 0

        # Zones, each player can have certain cards in certain zones
        self.__battlefield = []
        self.__kingdom = []
        self.__player_hand = [] # If the size of this is greater than 7 cards must be discarded at the end of a turn
        self.__relic_zone = []
        self.__terra_zone = []
        self.__graveyard = []
        self.__exiled = []


    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def is_throne_1_occupied(self):
        if self.__throne_1 is None:
            return False
        else:
            return True

    def is_throne_2_occupied(self):
        if self.__throne_2 is None:
            return False
        else:
            return True

    def set_throne_1_beginning(self, card):
        card.set_royal(True)
        self.__throne_1 = card

    def set_throne_2_beginning(self, card):
        card.set_royal(True)
        self.__throne_2 = card


