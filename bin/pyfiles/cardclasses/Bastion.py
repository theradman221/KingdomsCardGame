from pyfiles.cardclasses.NonAttackCard import NonAttackCard


class Bastion(NonAttackCard):
    def __init__(self):
        # The inheritance was not working because someone (Wyatt) forgot how inheritance works in python
        super().__init__()
        self.__name = ""
        self.__file_path = ""
        self.__cost = None
        self.__rarity = ""
        self.__is_exhausted = False
        self.__template = ""
        self.__image = ""
        self.__label = ""
        self.__unit = ""
        self.__color = ""
        self.__effects = []
        self.__activated_effects = []
        self.__description = ""
        self.__default_health = None
        self.__current_health = None



# Bastion health things
    def get_default_health(self):
        return self.__default_health

    def set_default_health(self, health):
        self.__default_health = health
        self.__current_health = health

    def get_health(self):
        return self.__current_health

    def set_health(self, health):
        self.__current_health = health

    def hit_for(self, damage):
        self.__current_health -= damage

    def heal_for(self, hitpoints):
        self.__current_health += hitpoints
