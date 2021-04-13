from pyfiles.cardclasses.Card import Card

# This class encompasses all non attack card's, classified as card's without health or attack.
class NonAttackCard(Card):
    def __init__(self):
        # The inheritance was not working because someone (Wyatt) forgot how inheritance works in python
        super().__init__() # Inherits the methods NOT VARIABLES!



