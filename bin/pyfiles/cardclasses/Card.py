# This is the class that all other card's inherit from
class Card:
    def __init__(self):
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

    def __str__(self):
        return self.__name

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

    def get_template(self):
        return self.__template

    def set_template(self, template):
        self.__template = template

    def get_image(self):
        return self.__image

    def set_image(self, image):
        self.__image = image

    def get_label(self):
        return self.__label

    def set_label(self, label):
        self.__label = label

    def get_unit(self):
        return self.__unit

    def set_unit(self, unit):
        self.__unit = unit

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def add_effect(self, effect):
        self.__effects.append(effect)


