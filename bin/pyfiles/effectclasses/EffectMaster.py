class EffectMaster():
    def __init__(self):
        self.__effects = []
        self.__triggers = []

    def get_effects(self):
        return self.__effects

    def add_effect(self, effect):
        self.__effects.append(effect)

    def get_triggers(self):
        return self.__triggers

    def add_trigger(self, trigger):
        self.__triggers.append(trigger)
