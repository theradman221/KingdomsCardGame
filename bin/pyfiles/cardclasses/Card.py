# This is the class that all other card's inherit from
class Card:
    def __init__(self):
        self.__name = ""
        self.__file_path = ""
        self.__cost = None
        self.__rarity = ""
        self.__is_rested = False
        self.__template = ""
        self.__image = ""
        self.__label = ""
        self.__unit = ""
        self.__color = ""
        self.__effects = []
        self.__activated_effects = []
        self.__description = ""
        self.__zone = None

        # These variables are to help make processing effects and effect-affects easier
        self.__entrance_effect = None
        self.__has_entrance_effect = False
        self.__fringe_effect = None
        self.__has_fringe_effect = False
        self.__has_urgency = False
        self.__has_level_up = False # This needs to be paired with something in either the player or gameloop that tracks the total number of cards played and what type they were.
        self.__has_ranged = False
        self.__ranged_damage = 0
        self.__has_reckless = False
        self.__has_guard = False
        self.__has_reflex = False
        self.__is_experienced = False
        self.__has_siege = False
        self.__siege_damage = 0
        self.__has_sneak = False
        self.__is_poisoned = False
        self.__is_exhausted = False # This effect makes it so a card cannot be rested
        self.__last_stand_effect = None
        self.__has_last_stand = False
        self.__is_restless = False
        self.__speed = 1
        self.__triggers = []
        self.__has_triggers = False


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

    def process_effects(self):
        pass

    def process_activated_effects(self):
        pass

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

    def get_is_rested(self):
        return self.__is_rested

    def set_is_rested(self, exhausted):
        self.__is_rested = exhausted

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

    # Getters and Setters for the various effects
    def get_entrance_effect(self):
        return self.__entrance_effect

    def set_entrance_effect(self, effect):
        self.__entrance_effect = effect
        self.__has_entrance_effect = True

    def remove_entrance_effect(self):
        self.__entrance_effect = None
        self.__has_entrance_effect = False

    def has_entrance_effect(self):
        return self.__has_entrance_effect


    def get_fringe_effect(self):
        return self.__fringe_effect

    def set_fringe_effect(self, effect):
        self.__fringe_effect = effect
        self.__has_fringe_effect = True

    def remove_fringe_effect(self):
        self.__fringe_effect = None
        self.__has_fringe_effect = False

    def has_fringe_effect(self):
        return self.__has_fringe_effect

    def has_urgency(self):
        return self.__has_urgency

    def set_urgency(self, state):
        self.__has_urgency = state

    def has_level_up(self):
        return self.__has_level_up

    def set_level_up(self, state):
        self.__has_level_up = state

    def has_ranged(self):
        return self.__has_ranged

    def set_ranged(self, state):
        self.__has_ranged = state

    def get_ranged_damage(self):
        return self.__ranged_damage

    def set_ranged_damage(self, damage):
        self.__ranged_damage = damage

    def has_reckless(self):
        return self.__has_reckless

    def set_reckless(self, state):
        self.__has_reckless = state

    def has_guard(self):
        return self.__has_guard

    def set_guard(self, state):
        self.__has_guard = state

    def has_reflex(self):
        return self.__has_guard

    def set_reflex(self, state):
        self.__has_reflex = state

    def is_experienced(self):
        return self.__is_experienced

    def set_experienced(self, state):
        self.__is_experienced = state

    def has_siege(self):
        return self.__has_siege

    def set_siege(self, state):
        self.__has_siege = state

    def get_siege_damage(self):
        return self.__siege_damage

    def set_siege_damage(self, damage):
        self.__siege_damage = damage

    def has_sneak(self):
        return self.__has_sneak

    def set_sneak(self, state):
        self.__has_sneak = state

    def is_poisoned(self):
        return self.__is_poisoned

    def set_poisoned(self, state):
        self.__is_poisoned = state

    def is_exhausted(self):
        return self.__is_exhausted

    def set_exhausted(self, state):
        self.__is_exhausted = state

    def get_last_stand_effect(self):
        return self.__last_stand_effect

    def set_last_stand_effect(self, effect):
        self.__last_stand_effect = effect
        self.__has_last_stand = True

    def remove_last_stand_effect(self):
        self.__last_stand_effect = None
        self.__has_last_stand = False

    def has_last_stand(self):
        return self.__has_last_stand

    def is_restless(self):
        return self.__is_restless

    def set_restless(self, state):
        self.__is_restless = state

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed

    def get_triggers(self):
        return self.__triggers

    def add_trigger(self, trigger):
        self.__triggers.append(trigger)
        self.__has_triggers = True

    def remove_trigger(self, trigger):
        self.__triggers.remove(trigger)
        if len(self.__triggers) == 0:
            self.__has_triggers = False

    def has_triggers(self):
        return self.__has_triggers