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
# THIS MIGHT BE BEING DELETED I'M NOT SURE THE ORIGINAL IDEA FOR THIS IS NECESSARY
class AttackProcessor:
    def __init__(self, card1, card2):
        self.__card1 = card1
        self.__card2 = card2
        self.__card1_effects = None
        self.__card2_effects = None
        self.__card1_activated_effects = None
        self.__card2_activated_effects = None

        # first we need to convert the activated - effects and effects into something python can actually use.
        if self.__card1.get_effects() != []:
            self.__card1_effects = self.__card1.get_effects()

        if self.__card2.get_effects() != []:
            self.__card2_effects = self.__card2.get_effects()

        if self.__card1.get_activated_effects() != []:
            self.__card1_activated_effects = self.__card1.get_activated_effects()

        if self.__card2.get_activated_effects() != []:
            self.__card2_activated_effects = self.__card2.get_activated_effects()



    # Begin processing an attack between 2 cards
    def processAttack(self):
        print("Processing attack between " + self.__card1.get_name(), "and", self.__card2.get_name())
        self.__card1.print_all_details()
        print()
        self.__card2.print_all_details()

        print(self.__card1.get_name(), "\b's effects are:")
        print(self.__card1_effects)
        print(self.__card2.get_name(), "\b's activated effects are:")
        print(self.__card1_activated_effects)
        print(self.__card2.get_name(), "\b's effects are:")
        print(self.__card2_effects)
        print(self.__card2.get_name(), "\b's activated effects are:")
        print(self.__card2_activated_effects)



        # Process the simplest attack possible
        if self.__get_card1_activated_effects() is None and self.__get_card2_activated_effects() is None and self.__get_card1_effects() is None and self.__get_card2_effects() is None:
            if self.__card1.get_attack() != None:
                self.__card2.hit_for(self.__card1.get_attack())
            if self.__card2.get_attack() != None:
                self.__card1.hit_for(self.__card2.get_attack())

        # The effects that actually affect an attack are different so we only need to be concerned if the effects contain,



        self.__card1.print_all_details()
        self.__card2.print_all_details()


    def __get_card1_effects(self):
        return self.__card1_effects

    def __get_card2_effects(self):
        return self.__card2_effects

    def __get_card1_activated_effects(self):
        return self.__card1_activated_effects

    def __get_card2_activated_effects(self):
        return self.__card1_activated_effects