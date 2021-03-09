from  bin.pyfiles.Deck import Deck
from bin.pyfiles.cardclasses.Card import Card

for i in range(100):
    print(i)

deck = Deck("Testing")
card = Card("Bobby!", "cardlane.text", "Super", "Potato")
deck.add_card(card)
deck.save_deck()
input("What is the name of mexico?")
