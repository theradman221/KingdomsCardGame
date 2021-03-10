import os
import json as js
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
path_to_cards = "\..\..\cards"
excluded_files = ["template.txt", "potato.txt"]
print("Starting")
def load_all_cards():
    # Go through every card's txt file and construct it into a real card object.
    for folder in os.listdir(os.getcwd() +path_to_cards):
        if not excluded_files.__contains__(folder):
            print(folder)
            for file in os.listdir(os.getcwd() + path_to_cards + "\\"+ folder):
                print(file)
                if not excluded_files.__contains__(file):
                    convert_file_to_card(folder + "\\" + file)
                # These are now the specific files each card lives in


   #with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in readonly mode

      # do your stuff
    print("Done")

# Takes in a file that contains a card and opens it and constructs a card object and returns it.
def convert_file_to_card(file):
    dict = js.load(open(os.getcwd() + path_to_cards +  "\\" + file))
    dict = dict["All"]
    # These are the checks where we start making different types of cards
    if (dict["Unit"] == "Lord"):
        print("This card is a lord")
        card = create_lord(dict)
        print(card.get_name())

    print(dict)
    return

def create_lord(dictionary):
    # not all card's will have all attributes so we will get the dict_keys and make sure that we don't try to add an attribute without a key
    card = Lord()
    dict_keys = dictionary.keys()
    print(dict_keys)
    if "Name" in dict_keys:
        card.set_name(dictionary["Name"])
    return card


load_all_cards()
convert_file_to_card("lord\AresLordOfBattle.txt")