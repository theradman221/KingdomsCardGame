from pyfiles.cardclasses.Card import Card

# This class encompasses all cards that can attack/defend in the game
class AttackCard(Card):
    def __init__(self):
        # The inheritance was not working because someone (Wyatt) forgot how inheritance works in python
        super().__init__() # Inherits the methods NOT VARIABLES!
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


        # Attack card specific variables
        self.__is_briefed = False
        self.__default_health = None
        self.__default_attack = None
        self.__current_health = None
        self.__current_attack = None
        self.__is_royal = False
        # Temp variables for health/attack buffs and debuffs
        self.__health_buff = 0
        self.__attack_buff = 0
        self.__health_debuff = 0
        self.__attack_debuff = 0
        self.__defense = 0

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


        # attack card specific details
        msg += "Attack Card Stats: \n"
        msg += "Is Briefed " + str(self.get_briefed()) + "\n"
        msg += "Current Health " +  str(self.get_current_health()) + "\n"
        msg += "Default Health " + str(self.get_default_health()) + "\n"
        msg += "Current Attack " + str(self.get_current_attack()) + "\n"
        msg += "Default Attack " + str(self.get_default_attack()) + "\n"
        print(msg)

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
        return self.__current_health + self.__health_buff - self.__health_debuff

    def set_health(self, health):
        self.__current_health = health

    def get_attack(self):
        return self.__current_attack + self.__attack_buff - self.__attack_debuff

    def set_attack(self, attack):
        self.__current_attack = attack

    def hit_for(self, damage):
        # Eat the defense before actual health
        if self.__defense > 0:
            rem_defense = self.__defense - damage
            # If we have defense remaining
            if rem_defense > 0:
                # we still have rem_defense defense remaining
                self.__defense = rem_defense
                return
            # If we have exactly 0 defense remaining
            elif rem_defense == 0:
                # Update the value and return
                self.__defense = 0
                return
            # Negative means we did not block it all
            else:
                # Adjust damage value and reset defense to 0
                damage = damage - self.__defense
                self.__defense = 0

        # Eat the health buff before actual health
        if self.__health_buff > 0:
            rem_buff = self.__health_buff - damage
            # If we have defense remaining
            if rem_buff > 0:
                # we still have rem_defense defense remaining
                self.__health_buff = rem_buff
                return
            # If we have exactly 0 defense remaining
            elif rem_buff == 0:
                # Update the value and return
                self.__health_buff = 0
                return
            # Negative means we did not block it all
            else:
                # Adjust damage value and reset defense to 0
                damage = damage - self.__health_buff
                self.__health_buff = 0

        self.__current_health -= damage

    def heal_for(self, hitpoints):
        self.__current_health += hitpoints

    def is_royal(self):
        return self.__is_royal

    def set_royal(self, royal):
        self.__is_royal = royal


