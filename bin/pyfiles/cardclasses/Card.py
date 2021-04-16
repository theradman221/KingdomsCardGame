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
        self.__activated_effects = []
        self.__description = ""
        self.__zone = None

    def print_all_details(self):
        msg = ""
        msg += "Name " + self.get_name() + "\n"
        msg += "File Path" + self.get_file_path() + "\n"
        msg += "Cost " + str(self.get_cost()) + "\n"
        msg += "Rarity " + self.get_rarity() + "\n"
        msg += "Is Exhausted " + str(self.get_is_exhausted()) + "\n"
        msg += "Template " + self.get_template() + "\n"
        msg += "Image " + self.get_image() + "\n"
        msg += "Label " + self.get_label() + "\n"
        msg += "Unit " + self.get_unit() + "\n"
        msg += "Color " + self.get_color() + "\n"
        msg += "Description " + self.get_description() + "\n"
        if len(self.get_effects()) > 0:
            msg += "Effects "
            for key in self.get_effects():
                msg += str(key) + "\n"
        if len(self.get_activated_effects()) > 0:
            msg += "Activated Effects "
            for key in self.get_activated_effects():
                msg += str(key) + "\n"

        print(msg)


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
        return self.__rarity

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

    def get_effects(self):
        return self.__effects

    def add_effect(self, effect):
        self.__effects.append(effect)

    def get_activated_effects(self):
        return self.__activated_effects

    def add_activated_effect(self, effect):
        self.__activated_effects.append(effect)

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_zone(self):
        return self.__zone

    def set_zone(self, zone):
        self.__zone = zone