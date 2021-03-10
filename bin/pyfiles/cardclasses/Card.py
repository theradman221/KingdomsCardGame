# This is the class that all other card's inherit from
class Card:
    def __init__(self):
        self.__name = ""
        self.__file_path = ""
        self.__cost = None
        self.__rarity = None
        self.__is_exhausted = False

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_file_path(self):
        return self.__file_path

    def set_file_path(self, file_path):
        self.__file_path = file_path

    def get_cost(self):
        return self.__cost

    def set_cost(self, cost):
        self.__cost = cost

    def get_rarity(self):
        return self.__cost

    def set_rarity(self, rarity):
        self.__rarity = rarity

    def get_is_exhausted(self):
        return self.__is_exhausted

    def set_is_exhausted(self, exhausted):
        self.__is_exhausted = exhausted

