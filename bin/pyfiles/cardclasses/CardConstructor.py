import os
import json as js
from bin.pyfiles.Deck import Deck
from bin.pyfiles.cardclasses.Lord import Lord
from bin.pyfiles.cardclasses.Bastion import Bastion
from bin.pyfiles.cardclasses.Hero import Hero
from bin.pyfiles.cardclasses.Pawn import Pawn
from bin.pyfiles.cardclasses.Relic import Relic
from bin.pyfiles.cardclasses.Scroll import Scroll
from bin.pyfiles.cardclasses.Supply import Supply
from bin.pyfiles.cardclasses.Terra import Terra
from bin.pyfiles.cardclasses.TerraLandMark import TerraLandMark
from bin.pyfiles.cardclasses.Token import Token
from bin.pyfiles.cardclasses.Trice import Trice

# Path to card's should bring up all folder's containing the different card types

excluded_files = ["template.txt", "potato.txt"]

def load_all_cards(path):
    if path != "":
        print(path + " This is a path that is not blank")
        path_to_cards = path
    else:
        path_to_cards = "\..\..\cards"
    # Go through every card's txt file and construct it into a real card object.
    deck = Deck("Master")
    for folder in os.listdir(path_to_cards):
        if not excluded_files.__contains__(folder):
            print(folder)
            for file in os.listdir(path_to_cards + "\\"+ folder):
                file_path = path_to_cards + "\\"+ folder + "\\" + file
                print(file)
                if not excluded_files.__contains__(file):
                    convert_file_to_card(file_path, deck)
    return deck

# Takes in a file that contains a card and opens it and constructs a card object and returns it.
def convert_file_to_card(file, deck):
    file_path = file
    dict = js.load(open(file_path))
    dict = dict["All"]
    # These are the checks where we start making different types of cards
    if dict["Unit"] == "Lord":
        card = create_lord(dict, file_path)
        deck.add_card(card)

    return

def create_lord(dictionary, file_path):
    # not all card's will have all attributes so we will get the dict_keys and make sure that we don't try to add an attribute without a key
    card = Lord()
    # This file path will be useful since the Deck can use it to directly load card's
    card.set_file_path(file_path)
    card.set_unit("Lord")
    dict_keys = dictionary.keys()
    print(dict_keys)
    # Common things that all cards should have
    if "Name" in dict_keys:
        card.set_name(dictionary["Name"])
    if "Template" in dict_keys:
        card.set_template(dictionary["Template"])
    if "Img" in dict_keys:
        card.set_image(dictionary["Img"])
    if "Rarity" in dict_keys:
        card.set_rarity(dictionary["Rarity"])
    if "Cost" in dict_keys:
        card.set_cost(dictionary["Cost"])
    if "Color" in dict_keys:
        card.set_color(dictionary["Color"])
    if "Unit-Label" in dict_keys:
        card.set_label(dictionary["Unit-Label"])

    # Effects, not all cards will have these
    if "Effects" in dict_keys:
        effect_dict = dictionary["Effects"]
        for key in effect_dict:
            card.add_effect(key) # NEED TO ADD EFFECT



    # Health and attack, only some cards will have these
    if "Health" in dict_keys:
        card.set_default_health(dictionary["Health"])
    if "Attack" in dict_keys:
        card.set_default_attack(dictionary["Attack"])
    else:
        card.set_default_attack(0)

    return card