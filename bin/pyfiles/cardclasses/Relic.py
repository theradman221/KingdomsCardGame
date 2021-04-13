from pyfiles.cardclasses.NonAttackCard import NonAttackCard

class Relic(NonAttackCard):
    def __init__(self):
        super().__init__()  # Inherits the methods NOT VARIABLES!
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


