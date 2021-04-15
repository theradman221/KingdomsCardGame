import json as js
import random as rand
import os
# This is so that the load deck logic can be entirely merged to this class instead of being half here and half in kingdoms
from pyfiles.cardclasses.CardConstructor import convert_file_to_card as ftc

save_path = os.getcwd() + "\saves\\"
# This class's purpose is to contain a deck of cards.
class Deck:
    def __init__(self, name):
        self.__name = name
        self.__deck = []
        self.__bastion = None
        self.__royal_1 = None
        self.__royal_2 = None

    def __str__(self):
        msg = ""
        for card in self.__deck:
            msg += str(card)
        return msg

    def add_bastion(self, card):
        self.__bastion = card

    def get_bastion(self):
        return self.__bastion

    def set_royal_1(self, card):
        self.__royal_1 = card

    def get_royal_1(self):
        return self.__royal_1

    def set_royal_2(self, card):
        self.__royal_2 = card

    def get_royal_2(self):
        return self.__royal_2

    def add_card(self, card):
        self.__deck.append(card)

    def shuffle_deck(self):
        rand.shuffle(self.__deck)

    def draw_card(self):
        # By default draws off of the top, or 0 position of the deck
        if len(self.__deck) > 0:
            return self.__deck.pop(0)
        else:
            return None

    # These methods are used by the save/load deck features
    def save_deck(self):
        # Convert the current deck to a json list of the card names and dump it in the save directory.
        js.dump(self.__convert_deck_to_json(), open(save_path + self.__name + ".json", "w"))
        return

    # Retrieves the json for a specified deck from the save location.
    def load_deck(self, name):
        dict = js.load(open(save_path + name + ".json"))
        deck_dict = dict[name]
        self.__deck = []
        for file in deck_dict:
            self.__deck.append(self.__load_cards(deck_dict[file]))

    def __load_cards(self, path):
        return ftc(path)

    # converts the entire deck into a json representation with the name as a key and the file path as the data.
    def __convert_deck_to_json(self):
        inside_dict = {}
        save_dict = {str(self.__name) : inside_dict}
        for card in self.__deck:
            inside_dict[card.get_name()] = card.get_file_path()
        return save_dict

    def get_name(self):
        return self.__name

    def get_copy(self):
        return self.__deck.copy()

    def print_deck(self):
        print("These are the cards contained in " + self.get_name() )
        for card in self.__deck:
            print(card.get_name())

    def print_deck_all_details(self):
        print("These are the cards contained in " + self.get_name() + " With all details")
        for card in self.__deck:
            card.print_all_details()

    # filters the deck and return a list of cards that meet criteria
    def filter_by_color(self, colors):
        filtered = []
        for card in self.__deck:
            if card.get_color() in colors or card.get_color() == "Colorless":
                filtered.append(card)
        return filtered

    def filter_by_unit(self, units):
        filtered = []
        for card in self.__deck:
            if card.get_unit() in units:
                filtered.append(card)
        return filtered