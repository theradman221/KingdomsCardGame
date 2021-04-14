
import os
from pyfiles.Deck import Deck
from pyfiles.cardclasses.Card import Card
from pyfiles.cardclasses.AttackCard import AttackCard

# This class is designed to keep track of information for each player that is required for the game to run correctly
class Player:
    def __init__(self, name):
        self.__throne_cost_increase_increment = 2
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

    # Getters and Setters for name, and the throne room + all related logic for the thron rooms
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

    def set_throne_1(self, card):
        self.__throne_1 = card
        self.__throne_1_counter += self.__throne_cost_increase_increment

    def set_throne_2(self, card):
        self.__throne_2 = card
        self.__throne_2_counter += self.__throne_cost_increase_increment

    def get_throne_1_cost(self):
        return self.__throne_1_counter

    def get_throne_2_cost(self):
        return self.__throne_2_counter

    def get_throne_1(self):
        return self.__throne_1

    def get_throne_2(self):
        return self.__throne_2

    def empty_throne_1(self):
        self.__throne_1 = None

    def empty_throne_2(self):
        self.__throne_2 = None

    def throne_room_empty(self):
        if not self.is_throne_1_occupied() and not self.is_throne_2_occupied():
            return True
        else:
            return False

    # Bastion management logic
    def set_bastion(self, bastion):
        self.__bastion = bastion

    def get_bastion(self):
        return self.__bastion

    def damage_bastion(self, dmg):
        self.__bastion.hit_for(dmg)

    def heal_bastion(self, heal):
        self.__bastion.heal_for(heal)

    def get_bastion_health(self):
        return self.__bastion.get_health()

    # Deck logic for main and terra decks

    # Zone logic
    # Battlefield
    def get_battlefield(self):
        return self.__battlefield

    def remove_from_battlefield(self, card):
        for i in self.__battlefield:
            if self.same_card(i, card):
                self.__battlefield.remove(i)
                return True
        else:
            return False

    def same_card(self, card1, card2):
        card1 = AttackCard()
        card2 = AttackCard()
        if card1.get_unit() != card2.get_unit():
            return False
        elif card1.get_label() != card2.get_label():
            return False
        elif card1.get_name() != card2.get_name():
            return False
        elif card1.get_current_health() != card2.get_current_health():
            return False
        elif card1.get_current_attack() != card2.get_current_attack():
            return False
        else:
            return True

    def update_battlefield(self, battlefield):
        self.__battlefield = battlefield

    def add_to_battlefield(self,card):
        self.__battlefield.append(card)



        # # These are the main decks, all other decks (or zones) will be populated with cards from these 2 decks (except tokens, they are weird)
        # self.__main_deck = None
        # self.__terra_deck = None
        #
        #
        # # Zones, each player can have certain cards in certain zones
        # self.__battlefield = []
        # self.__kingdom = []
        # self.__player_hand = [] # If the size of this is greater than 7 cards must be discarded at the end of a turn
        # self.__relic_zone = []
        # self.__terra_zone = []
        # self.__graveyard = []
        # self.__exiled = []