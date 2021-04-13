import os
import json as js
from pyfiles.Deck import Deck
from pyfiles.cardclasses.Lord import Lord
from pyfiles.cardclasses.Bastion import Bastion
from pyfiles.cardclasses.Hero import Hero
from pyfiles.cardclasses.Pawn import Pawn
from pyfiles.cardclasses.Relic import Relic
from pyfiles.cardclasses.Scroll import Scroll
from pyfiles.cardclasses.Supply import Supply
from pyfiles.cardclasses.Terra import Terra
from pyfiles.cardclasses.TerraLandMark import TerraLandMark
from pyfiles.cardclasses.Token import Token
from pyfiles.cardclasses.Trice import Trice
# Used for testing to pause output blocks and such
import time

# Path to card's should bring up all folder's containing the different card types

excluded_files = ["template.txt", "potato.txt", "bastion" ,"effects.txt", "nondemonotworking", "nondemoworking", "Crack.txt", "SpeedScroll.txt", "Pluck.txt"]


def load_all_cards(path):
    if path != "":
        path_to_cards = path
    else:
        path_to_cards = "\..\..\cards"
    # Go through every card's txt file and construct it into a real card object.
    deck = Deck("Master")
    for folder in os.listdir(path_to_cards):
        if not excluded_files.__contains__(folder):
            for file in os.listdir(path_to_cards + "\\" + folder):
                #print(folder + "\\" + file) # This print is good for debugging if a file is causing a crash.
                file_path = path_to_cards + "\\" + folder + "\\" + file
                if not excluded_files.__contains__(file):
                    deck.add_card(convert_file_to_card(file_path))
    time.sleep(6)
    return deck


# Takes in a file that contains a card and opens it and constructs a card object and returns it.
def convert_file_to_card(file):
    file_path = file
    dict = js.load(open(file_path))
    dict = dict["All"]
    # These are the checks where we start making different types of cards
    if dict["Unit"] == "Lord":
        card = create_lord(dict, file_path)

    if dict["Unit"] == "Terra":
        card = create_terra(dict, file_path)

    if dict["Unit"] == "TerraLandmark":
        card = create_terra_landmark(dict, file_path)

    if dict["Unit"] == "Pawn":
        card = create_pawn(dict, file_path)

    if dict["Unit"] == "Bastion":
        card = create_bastion(dict, file_path)

    if dict["Unit"] == "Hero":
        card = create_hero(dict, file_path)

    if dict["Unit"] == "Relic":
        card = create_relic(dict, file_path)

    if dict["Unit"] == "Scroll":
        card = create_scroll(dict, file_path)

    if dict["Unit"] == "Supply":
        card = create_supply(dict, file_path)

    if dict["Unit"] == "Token":
        card = create_token(dict, file_path)

    if dict["Unit"] == "Trice":
        card = create_trice(dict, file_path)

    return card


def create_bastion(dictionary, file_path):
    # not all card's will have all attributes so we will get the dict_keys and make sure that we don't try to add an attribute without a key
    card = Bastion()
    card.set_unit("Bastion")
    # This file path will be useful since the Deck can use it to directly load card's
    card.set_file_path(file_path)
    dict_keys = dictionary.keys()
    add_universal_attributes(dictionary,dict_keys,card)
    return card


def create_hero(dictionary, file_path):
    # not all card's will have all attributes so we will get the dict_keys and make sure that we don't try to add an attribute without a key
    card = Hero()
    card.set_unit("Hero")
    # This file path will be useful since the Deck can use it to directly load card's
    card.set_file_path(file_path)
    dict_keys = dictionary.keys()
    add_universal_attributes(dictionary,dict_keys,card)
    add_attack_card_attributes(dictionary,dict_keys,card)
    return card


def create_relic(dictionary, file_path):
    # not all card's will have all attributes so we will get the dict_keys and make sure that we don't try to add an attribute without a key
    card = Relic()
    card.set_unit("Relic")
    # This file path will be useful since the Deck can use it to directly load card's
    card.set_file_path(file_path)
    dict_keys = dictionary.keys()
    add_universal_attributes(dictionary,dict_keys,card)
    return card


def create_scroll(dictionary, file_path):
    # not all card's will have all attributes so we will get the dict_keys and make sure that we don't try to add an attribute without a key
    card = Scroll()
    card.set_unit("Scroll")
    # This file path will be useful since the Deck can use it to directly load card's
    card.set_file_path(file_path)
    dict_keys = dictionary.keys()
    add_universal_attributes(dictionary,dict_keys,card)
    return card


def create_supply(dictionary, file_path):
    # not all card's will have all attributes so we will get the dict_keys and make sure that we don't try to add an attribute without a key
    card = Supply()
    card.set_unit("Supply")
    # This file path will be useful since the Deck can use it to directly load card's
    card.set_file_path(file_path)
    dict_keys = dictionary.keys()
    add_universal_attributes(dictionary,dict_keys,card)
    return card


def create_token(dictionary, file_path):
    # not all card's will have all attributes so we will get the dict_keys and make sure that we don't try to add an attribute without a key
    card = Token()
    card.set_unit("Token")
    # This file path will be useful since the Deck can use it to directly load card's
    card.set_file_path(file_path)
    dict_keys = dictionary.keys()
    add_universal_attributes(dictionary,dict_keys,card)
    add_attack_card_attributes(dictionary,dict_keys,card)
    return card


def create_trice(dictionary, file_path):
    # not all card's will have all attributes so we will get the dict_keys and make sure that we don't try to add an attribute without a key
    card = Trice()
    card.set_unit("Trice")
    # This file path will be useful since the Deck can use it to directly load card's
    card.set_file_path(file_path)
    dict_keys = dictionary.keys()
    add_universal_attributes(dictionary,dict_keys,card)
    return card


def create_lord(dictionary, file_path):
    # not all card's will have all attributes so we will get the dict_keys and make sure that we don't try to add an attribute without a key
    card = Lord()
    card.set_unit("Lord")
    # This file path will be useful since the Deck can use it to directly load card's
    card.set_file_path(file_path)
    dict_keys = dictionary.keys()
    add_universal_attributes(dictionary,dict_keys,card)
    add_attack_card_attributes(dictionary,dict_keys,card)
    return card


def create_pawn(dictionary, file_path):
    # not all card's will have all attributes so we will get the dict_keys and make sure that we don't try to add an attribute without a key
    card = Pawn()
    card.set_unit("Pawn")
    # This file path will be useful since the Deck can use it to directly load card's
    card.set_file_path(file_path)
    dict_keys = dictionary.keys()
    add_universal_attributes(dictionary,dict_keys,card)
    add_attack_card_attributes(dictionary,dict_keys,card)
    return card


def create_terra(dictionary, file_path):
    # not all card's will have all attributes so we will get the dict_keys and make sure that we don't try to add an attribute without a key
    card = Terra()
    card.set_unit("Terra")
    # This file path will be useful since the Deck can use it to directly load card's
    card.set_file_path(file_path)
    dict_keys = dictionary.keys()
    add_universal_attributes(dictionary,dict_keys,card)
    return card


def create_terra_landmark(dictionary, file_path):
    # not all card's will have all attributes so we will get the dict_keys and make sure that we don't try to add an attribute without a key
    card = TerraLandMark()
    card.set_unit("TerraLandmark")
    # This file path will be useful since the Deck can use it to directly load card's
    card.set_file_path(file_path)
    dict_keys = dictionary.keys()
    add_universal_attributes(dictionary,dict_keys,card)
    return card


def add_attack_card_attributes(dictionary, dict_keys, card):
    if "Health" in dict_keys:
        card.set_default_health(dictionary["Health"])
    if "Attack" in dict_keys:
        card.set_default_attack(dictionary["Attack"])
    else:
        card.set_default_attack(0)
    return card


def add_universal_attributes(dictionary, dict_keys, card):
    # Path from the bin, where kingdoms lives, to the card images, also will need ones for the template, and rarity too
    path_to_img = os.getcwd() +  "\\cardart\\"
    path_to_template = os.getcwd() + "\\cardtemplates\\"
    # To make it easier when actually selecting the type, diving the path to template into, bastion, non-unit, terra, and units
    path_to_bastion = path_to_template + "bastion\\"
    path_to_non_unit = path_to_template + "non-unit\\"
    path_to_terra = path_to_template + "terra\\"
    path_to_unit = path_to_template + "units\\"
    path_to_rarity = os.getcwd() + "\\cardtemplates\\raritys\\"

    # Common things that all cards should have
    if "Name" in dict_keys:
        card.set_name(dictionary["Name"])
    if "Description" in dict_keys:
        card.set_description(dictionary["Description"])

    if "Template" in dict_keys:
        if dictionary["Template"] == "":
            card.set_template(dictionary["Template"])
        else :
            # All unit types that use the unit template
            if dictionary["Unit"] == "Hero" or dictionary["Unit"] == "Pawn" or dictionary["Unit"] == "Lord" or dictionary["Unit"] == "Token":
                card.set_template(path_to_unit + dictionary["Template"])

            # All unit types that use the bastion template
            elif dictionary["Unit"] == "Bastion":
                card.set_template(path_to_bastion + dictionary["Template"])

            # All unit types that use the non-unit template
            elif dictionary["Unit"] == "Relic" or dictionary["Unit"] == "Scroll" or dictionary["Unit"] == "Supply" or dictionary["Unit"] == "Trice":
                card.set_template(path_to_non_unit + dictionary["Template"])

            # All unit types that use the terra template
            elif dictionary["Unit"] == "Terra" or dictionary["Unit"] == "TerraLandMark":
                card.set_template(path_to_terra + dictionary["Template"])

            # If nothing matched just set it to the file name and it'll be handled later
            else:
                print(card.get_name(), "was not categorized! It's unit type is", dictionary["Unit"])
                card.set_template(dictionary["Template"])

            #print(card.get_name(), "is a", card.get_unit() + "! It's file path for the template is", card.get_template())

    if "Img" in dict_keys:
        if dictionary["Img"] == "": # Detect a placeholder
            card.set_image(dictionary["Img"])
        else: # Append the appropriate file path
            print(card.get_name(), "This one is one with a non blank img")
            card.set_image(path_to_img + dictionary["Img"])

    if "Rarity" in dict_keys:
        if dictionary["Rarity"] == "":
            card.set_rarity(dictionary["Rarity"])
        else:
            card.set_rarity(path_to_rarity + dictionary["Rarity"])
            #print(card.get_name(), "is of the", dictionary["Rarity"], "it's template path is", card.get_rarity())

    if "Cost" in dict_keys:
        card.set_cost(dictionary["Cost"])
    if "Color" in dict_keys:
        card.set_color(dictionary["Color"])
    if "Unit-Label" in dict_keys:
        card.set_label(dictionary["Unit-Label"])

    if "Effects" in dict_keys:
        effect_dict = dictionary["Effects"]
        card.add_effect(effect_dict)

    if "Activated-Effect" in dict_keys:
        activated_dict = dictionary["Activated-Effect"]
        card.add_activated_effect(activated_dict)
    return card
