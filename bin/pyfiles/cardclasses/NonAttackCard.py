from bin.pyfiles.cardclasses.Card import Card

# This class encompasses all non attack card's, classified as card's without health or attack.
class NonAttackCard(Card):
    def __init__(self, name, power, rarity):
        self.__name = name
        self.__power = power
        self.__rarity = rarity
        self.__is_exhausted = False
