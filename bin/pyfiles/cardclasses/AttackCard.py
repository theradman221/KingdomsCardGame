from bin.pyfiles.cardclasses.Card import Card

# This class encompasses all cards that can attack/defend in the game
class AttackCard(Card):
    def __init__(self):
        self.__is_briefed = False
        self.__default_health = None
        self.__default_attack = None
        self.__current_health = None
        self.__current_attack = None

    def get_briefed(self):
        return self.__is_briefed

    def set_briefed(self, briefed):
        self.__is_briefed = briefed

    def get_default_health(self):
        return self.__default_health

    def set_default_health(self, health):
        self.__default_health = health
        self.__current_health = health

    def get_default_attack(self):
        return self.__default_attack

    def set_default_attack(self, attack):
        self.__default_attack = attack
        self.__current_attack = attack

    def get_health(self):
        return self.__current_health

    def set_health(self, health):
        self.__current_health = health

    def get_attack(self):
        return self.__current_attack

    def set_attack(self, attack):
        self.__current_attack = attack

    def hit_for(self, damage):
        self.__current_health -= damage

    def heal_for(self, hitpoints):
        self.__current_health += hitpoints

