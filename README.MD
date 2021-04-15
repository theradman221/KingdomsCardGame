# KingomsCardGame
This is the testing software for the Kingdom's card game. 
It will simulate the game online for testing purposes. 
It is designed to be run from kingdoms.py in the configuration settings.
The game has a GUI interface that will be utilized to improve the user experience. 

Software required to run Kingdoms
Python
Pygame
Pygame-menu
PyOpenGL

Kingdoms: The Official Rules 
A Brief Intro: Kingdoms is a trading card game where the major three factions, Kaebur, Furisso and Aceus are all battling each other in a deadly civil war to expand their borders and gain control over powerful relics. Fight for your faction with Heroes, Lords, pawns, and powerful magic! Build your army and destroy your enemy's bastion to win! 
Setup: Your Main deck must have exactly 40 non terra cards and your terra deck must have exactly 20 terra cards. You can have up to 3 copies of the same card in a deck. You must choose 2 "Royals" to sit in your throne room. These royals can be any 2 Hero's/Lord's you choose. The color of your "Royals" decides what color cards you may play in your deck(s). You must also have one bastion. Your bastion and throne room are separate from your main deck and do not count toward its total capacity. 
Starting a Duel: To begin, each player chooses a deck and places their royals in "The throne room" and their bastion in the zone next to "The Throne Room". You then place your main deck in your deck zone (Card pile symbol) and your terra deck in your terra deck zone (tree symbol). Now each player draws 5 cards from the top of their main deck. Then each player may decide to return any cards they don't like to their respective decks, shuffle, and draw cards equal to the number they returned. Now choose who goes first by whatever means all players deem acceptable. The loser of a best 2 out of 3 match always chooses who goes first. Now players take their turns in phases, starting with the player who has been decided to go first 
The Phases of a Turn 
***IF YOU HAVE QUESTIONS JUST KEEP READING AND ALL WILL BE EXPLAINED FURTHER IN THE DOCUMENT*** 
Rest phase: During this phase permanents you control regain their energy, becoming "Rested" and returning to their original upright position. This step happens even if you control no permanents 
Draw Phase: During this phase you draw a total of two cards! You may draw from either your main deck or your terra deck to accomplish this. The player who goes first may only draw once total. Also, whenever a card says to draw (or study) you may draw (or study) from either of your decks! 
Upkeep Phase: Some cards require payment each turn to remain on the field, this is typically when you pay it. Some other effects trigger during this phase as well. 
Main Phase: You may play any card from your hand if you can gather enough power to pay its cost(s) (TOP LEFT NUMBER = Cost) and/or move units 
Attack Phase: During this phase, each unit that is rested and has been briefed can choose 1 legal attack target each. A legal attack target is any permanent with health. To declare the attack, you must exhaust the unit. Then the 2 cards battle and they each lose Health(bottom right number) = to the other cards Attack(bottom left number). This happens to both units simultaneously. This is known as damage calculation. Targets with no Attack and targets that are exhausted do not deal damage back. P.S Health does not regenerate automatically and to keep track there are scripted health buttons on each card
Main Phase 2: This is an added main phase for strategizing etc. You cannot enter this phase if you do not enter your attack phase 
End Phase: Declare that you are entering your end phase and if you have more than seven cards in your hand discard down to seven, all players also have one last chance to respond with a speed 2 effect of some kind. The next player then declares that they will begin their turn 
Basic Rules 
The Throne Room: The Royals in your throne room can be played as if they were in your hand from the beginning of the duel. Any time a Royal you own would be removed from play you may place them in an empty slot in the throne room instead and place two counters on that slot. When you play a Royal from the throne room you must pay its original cost plus 1 for each counter on that slot 
Moving Units: Units can move from the battlefield to the kingdom or vice versa, once a turn, if they have been briefed and are not exhausted 
Kingdoms & The Battlefield: Permanents with Health can be played in your kingdom or on the battlefield. Other permanents are played in your kingdom. Permanents in your kingdom can only be targeted for attacks if you have no units on the battlefield/all the units you have on the battlefield are exhausted. Units in your kingdom cannot declare attacks 
Searching the Deck: Whenever a player searches their deck they must shuffle it afterwards and their opponent can ask to cut the deck or shuffle it themselves as well. Additionally, you must reveal any cards you are adding from your deck to your hand. Cards will say when you can break this rule and not have to reveal the card(s) to your opponent 
Important Terms 
Exhaust: Some cards may ask that you pay a cost of exhausting the card which just means to turn the card 90 degrees. While a card is exhausted it cannot attack, use fringe effects or exhaust again. When a card is Un-Exhausted it is simply rested. AKA in its original upright position 
Briefing: If a unit is under your control during your rest phase you can exhaust them, move them or attack with them. If a unit was not under your control during your rest phase then the unit must first be briefed before it can exhaust itself for any reason or attack. In other words the turn you play a unit or gain control of a unit it can not exhaust itself or attack until your next turn 
Power: This is used to pay for the cost of cards. The top left number on a card is the amount of power needed to play the card. You Gain power by exhausting your Terra cards 
Unit: A Lord/Hero/Pawn 
Permanent: Any card that stays on the field after it is played. Bastions, units, terra cards, relics, and supplies 
Cost: An effect that requires a payment of power
Trigger: An effect that "activates" when a condition is met 
Fringe: If a card is rested you can activate its fringe effect once per turn. These effects can - or + health of the card. Fringe effects that deduct health for their cost cannot kill their unit unless they have the same amount of Health as required to be deducted 
Entrance: An effect that "activates" when the card enters play 
Sacrifice: Send the card to the graveyard 
Last stand: An effect that triggers when a card is sent to the graveyard after being destroyed or sacrificed 
Card Types 
Permanent: Any card that remains on the board after its played, that's every card but scroll and trice cards 
Bastion: Is your Kingdom. When its Health reaches 0 you lose! So be careful 
Terra - Basic: Can only play one per turn. You exhaust these for power 
Terra - LandMark: Same as terra but have additional effects, if you control more than 1 copy of the same Terra - LandMark you must destroy all but one copy 
Pawns: Has attack and health and you may control as many pawns with the same name as you want 
Hero: Like a pawn but far more powerful. If you control more than one copy the same hero all but one must be destroyed 
Lord: Has health but no attack, and fringe abilities to buff itself. If you control more than one copy the same lord all but one must be destroyed 
Relic: Colorless permanents with support effects. Can be played in any deck 
Scroll: Can be played during the main phases of your turn, they are discarded to the grave then the cards effect is applied 
Trice: The same as a scroll card but it can be played at any time. Even during your opponent's turn Supply: These enter play attached to a unit card. Usually giving buff/de-buff or both Advanced Rulings 
Sequence’s: When card effects are activated they await their resolution. During this time each player has time to react and play cards or effects in response. If a card or effect is activated in response to another card or effect then it creates a sequence. When all players decide that they are not going to activate any more cards or effects then the sequence resolves. Sequences resolve from the last card/effect played to the first card/effect played. A card/effect that meets a requirement to activate still gets to attempt to resolve its effect even if that it is removed from its original zone before its resolution
Timing: Most cards have normal play speed meaning they can only be played during the main phase 1 or 2 and there must be no current sequence. Some cards and effects have play speed 2 which means that it has no restriction to WHEN it can be played but only IF you can pay its cost. Cards and effects with play speed 2 include trice cards, cost effects, trigger effects(including last stand, entrance, sacrifice, expel), and exhaust effects. Units can still only activate exhaust effects after they have been briefed 
Power: After you gain power and before you use said power it is stored in a "pool", this "pool" resets at the end of each individual phase of a turn 
Losing a Health Buff: When a unit loses a health buff it cannot have its health reduced below its original printed health value 
Firm: Sometimes things will say Firm before them. This means that you can only gain that effect once per turn but, by having multiple copies of the card you can gain the effect multiple times each turn 
Hard: Sometimes things will say Hard before them. This means you can only ever gain that effect once per turn 
Strict: Sometimes things will say Strict before them. This means you can only ever gain that effect once per duel 
Tokens: Tokens can not exist anywhere but on the battlefield or in the kingdom (your relic and terra zones are part of your kingdom). If they do they are immediately destroyed, sent to the graveyard and then removed completely from the game
