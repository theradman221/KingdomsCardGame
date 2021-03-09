from bin.pyfiles.cardclasses.Card import Card

# This class encompasses all cards that can attack/defend in the game
class AttackCard(Card):
    def __init__(self, name, power, rarity, default_health, default_attack):
        self.__name = name
        self.__power = power
        self.__rarity = rarity
        self.__is_exhausted = False
        self.__is_briefed = False
        self.__default_health = default_health
        self.__default_attack = default_attack
