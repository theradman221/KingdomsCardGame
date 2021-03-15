from bin.pyfiles.cardclasses.AttackCard import AttackCard

class Pawn(AttackCard):
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

        # Attack card specific
        self.__is_briefed = False
        self.__default_health = None
        self.__default_attack = None
        self.__current_health = None
        self.__current_attack = None


    def __str__(self):
        return self.__name

    def print_all_details(self):
        msg = ""
        msg += "Name " + self.__name + "\n"
        msg += "File Path" + self.__file_path + "\n"
        msg += "Cost " + str(self.__cost) + "\n"
        msg += "Rarity " + self.__rarity + "\n"
        msg += "Is Exhausted " + str(self.__is_exhausted) + "\n"
        msg += "Template " + self.__template + "\n"
        msg += "Image " + self.__image + "\n"
        msg += "Label " + self.__label + "\n"
        msg += "Unit " + self.__unit + "\n"
        msg += "Color " + self.__color + "\n"
        msg += "Description " + self.__description + "\n"
        if len(self.__effects) > 0:
            msg += "Effects "
            for key in self.__effects:
                msg += str(key) + "\n"
        if len(self.__activated_effects) > 0:
            msg += "Activated Effects "
            for key in self.__activated_effects:
                msg += str(key) + "\n"

        # attack card specific details
        msg += "Attack Card Stats: \n"
        msg += "Is Briefed " + str(self.__is_briefed) + "\n"
        msg += "Current Health " + str(self.__current_health) + "\n"
        msg += "Default Health " + str(self.__default_health) + "\n"
        msg += "Current Attack " + str(self.__current_attack) + "\n"
        msg += "Default Attack " + str(self.__default_attack) + "\n"
        print(msg)

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

    def get_effects(self):
        return self.__effects

    def add_effect(self, effect):
        self.__effects.append(effect)

    def get_activated_effects(self):
        return self.__activated_effects

    def add_activated_effect(self, effect):
        self.__activated_effects.append(effect)

        # attack card specific

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

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description