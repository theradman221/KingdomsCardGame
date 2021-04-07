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

class AttackProcessor:
    def __init__(self, card1, card2):
        self.__card1 = card1
        self.__card2 = card2
        return

    # Begin processing an attack between 2 cards
    def processAttack(self):
        print("Processing attack between " + self.__card1.get_name(), "and", self.__card2.get_name())
        self.__card1.print_all_details()
        print()
        self.__card2.print_all_details()
        # first we need to convert the activated - effects and effects into something python can actually use.
        if self.__card1.get_effects() == []:
            print("card 1 has no effects")

        if self.__card2.get_effects() == []:
            print("Card 2 has no effects")

        if self.__card1.get_activated_effects() == []:
            print("card 1 has no activated effects")

        if self.__card2.get_activated_effects() == []:
            print("Card 2 has no activated effects")
