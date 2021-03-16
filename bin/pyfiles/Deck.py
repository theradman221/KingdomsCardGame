import json as js
import random as rand
import os


save_path = os.getcwd() + "\saves\\"
# This class's purpose is to contain a deck of cards.
class Deck:
    def __init__(self, name):
        self.__name = name
        self.__deck = []

    def __str__(self):
        msg = ""
        for card in self.__deck:
            msg += str(card)
        return msg

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

    def load_deck(self, name):
        dict = js.load(open(save_path + name + ".json"))
        return dict


    def __convert_deck_to_json(self):
        inside_dict = {}
        save_dict = {str(self.__name) : inside_dict}
        for card in self.__deck:
            inside_dict[card.get_name()] = card.get_file_path()
        return save_dict

    def get_name(self):
        return self.__name