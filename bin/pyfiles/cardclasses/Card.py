# This is the class that all other card's inherit from
class Card:
    def __init__(self, name, file_path,  power, rarity):
        self.__name = name
        self.__file_path = file_path
        self.__power = power
        self.__rarity = rarity
        self.__is_exhausted = False

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_file_path(self):
        return self.__file_path


