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
            msg += str(card) + " "
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

    def is_empty(self):
        if len(self.__deck > 0):
            return False
        else:
            return True

    def remove_card(self, card):
        for card2 in self.__deck:
            if card2.get_name() == card.get_name():
                self.__deck.remove(card)
                return True
        return False

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

    # Deletes the deck save that shares the name of this deck
    def delete_deck(self):
        delete_path = save_path + self.__name + ".json"
        if os.path.exists(delete_path):
            os.remove(delete_path)
            return True
        else:
            return False

    # Retrieves the json for a specified deck from the save location.
    def load_deck(self):
        name = self.__name
        dict = js.load(open(save_path + name + ".json"))
        deck_dict = dict[name]
        self.__deck = []
        # Num is named that way because originally it was only numbers, but now we save bastion and royals too to make checking correctness easier
        for num in deck_dict:
            for card in deck_dict[num]:
                if num == "Bastion":
                    self.add_bastion(self.__load_cards(deck_dict[num][card]))
                elif num == "Royal1":
                    self.set_royal_1(self.__load_cards(deck_dict[num][card]))
                elif num == "Royal2":
                    self.set_royal_2(self.__load_cards(deck_dict[num][card]))
                else:
                    self.__deck.append(self.__load_cards(deck_dict[num][card]))

    def __load_cards(self, path):
        return ftc(path)

    # converts the entire deck into a json representation with the name as a key and the file path as the data.
    def __convert_deck_to_json(self):
        outer_dict = {}
        save_dict = {str(self.__name): outer_dict}
        # Check for bastion and throne rooms entries
        if self.__bastion is not None:
            outer_dict["Bastion"] = {self.__bastion.get_name() : self.__bastion.get_file_path()}
        if self.__royal_1 is not None:
            outer_dict["Royal1"] = {self.__bastion.get_name() : self.__royal_1.get_file_path()}
        if self.__royal_2 is not None:
            outer_dict["Royal2"] = {self.__bastion.get_name() : self.__royal_2.get_file_path()}
        # To keep the dictionary from combining on the same cards we need to use a counter as an outer dictionary
        counter = 0
        for card in self.__deck:
            # This was added to fix an issue where cards were only saved once
            inner_dict = {}
            inner_dict[card.get_name()] = card.get_file_path()
            outer_dict[counter] = inner_dict
            counter += 1
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

    # filters the deck and return a list of cards that meet criteria, or are colorless
    def filter_by_color(self, colors):
        filtered = []
        for card in self.__deck:
            if card.get_color() in colors or card.get_color() == "Colorless":
                filtered.append(card)
        return filtered

    # Exactly like filter by color, except that it doesn't give allow colorless if they aren't specified
    def strict_filter_by_color(self, colors):
        filtered = []
        for card in self.__deck:
            if card.get_color() in colors:
                filtered.append(card)
        return filtered

    # Filters the deck and returns a list of cards that meets the criteria
    def filter_by_unit(self, units):
        filtered = []
        for card in self.__deck:
            if card.get_unit() in units:
                filtered.append(card)
        return filtered

    # This is useful if you want to make a copy of a deck from a save since it tries to load by deck name
    def set_name(self, name):
        self.__name = name

    # This is so that if you have a copy of a deck you can easily add it without saving/loading and renaming shenanigans.
    def set_deck(self, deck):
        self.__deck = deck