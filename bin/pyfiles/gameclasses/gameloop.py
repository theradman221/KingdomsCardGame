
# The point of this file is to contain all of the code to actually run the game once players are ready to play, have picked decks ect
from pyfiles.gameclasses.Player import Player
import random

# Constants
PLAYER_LIMIT = 2
DRAW_PHASE_LIMIT = 2

# This is the enter point, for the player setup a list of decks should be provided
def run_game(decks):
    # This variable will be set to false once a player either wins, or quits the game
    game_run = True

    # Variables for different quadrants of the screen WITH ONLY 2 PLAYERS
    player1_bastion_coordinates = []


    # These are the phases of the game, in order
    game_phases = ["Rest", "Draw", "UpKeep", "Main", "Attack", "Main2", "End"]
    # These are all the different zones that units update in, most don't update in hand or deck so they're not included
    zones = ["Kingdom", "Battlefield", "Relic-Zone", "Terra-Zone", "Graveyard", "Exiled", "Player-Hand", "Main-Deck", "Terra-Deck"]


    # Player creation
    players = create_players(decks)
    first_player = True
    while game_run:
        keep_going = input("Do you want to keep going? ")
        print(keep_going)
        if keep_going.lower() != "y" or len(players) < 2:
            # Using break instead of = False here so that all of the turn logic doesn't need != False logic
            break


        for player in players:
            for phase in game_phases:
                # Rest Phase
                if phase == "Rest":
                    # Get the players cards for each area, for this phase we only care about the first 4 zones
                    kingdom_cards = player.get_kingdom()
                    battlefield_cards = player.get_battlefield()
                    relic_cards = player.get_relic_zone()
                    terra_cards = player.get_terra_zone()
                    player.update_kingdom(process_rest_phase(kingdom_cards))
                    player.update_battlefield(process_rest_phase(battlefield_cards))
                    player.update_relic_zone(process_rest_phase(relic_cards))
                    player.update_terra_zone(process_rest_phase(terra_cards))

                # Draw Phase
                if phase == "Draw":
                    drawn = False
                    if first_player:
                        draw_limit = 1
                        first_player = False
                    else:
                        draw_limit = DRAW_PHASE_LIMIT
                    have_drawn = 0
                    while not drawn:
                        print(player.get_name(), "it's your turn to draw: Please enter M to draw from your main deck or T to draw from your terra deck.\nIf you wish to skip drawing enter skip.\nYou have", (draw_limit - have_drawn), "cards left to draw")
                        to_draw = input()
                        if to_draw.lower() == "m":
                            card = player.draw_from_main_deck()
                            print(player.get_name(), "you drew", card.get_name())
                            player.add_to_player_hand(card)
                            have_drawn += 1

                        elif to_draw.lower() == "t":
                            card = player.draw_from_terra_deck()
                            print(player.get_name(), "you drew", card.get_name())
                            player.add_to_player_hand(card)
                            have_drawn += 1

                        elif to_draw.lower() == "skip":
                            break

                        if have_drawn == draw_limit:
                            drawn = True

                    # TESTING
                    hand_after_drawing = player.get_player_hand()
                    for card in hand_after_drawing:
                        print(card)
                        # card.print_all_details()




                print("it's", player.get_name() + "'s turn, the phase is", phase)

def process_rest_phase(cards_list):
    updated_cards = []
    briefable_units = ["Lord", "Hero", "Pawn", "Token"]
    for card in cards_list:
        # Rest and brief all cards, all card can be exhausted, not all can be briefed
        if card.get_is_exhausted():
            card.set_is_exhausted(False)

        if card.get_unit() in briefable_units:
            card.set_briefed(True)
        updated_cards.append(card)
    return updated_cards




def create_players(decks):
    players = []  # Each player created will be added to this list, then shuffle this and use it to determine turn order
    # Get a list of all deck names
    deck_names = {}

    for deck in decks:
        deck.verify_deck()
        print(deck.get_name(), deck.get_type())
        print(deck.get_verification_notes())
        deck_names[deck.get_name()] = deck

    player_name = ""
    while player_name.lower() != "stop":
        player_name = input("Please enter the name of the next player, or enter \"stop\" to quit adding new players. \n")
        if len(players) + 1 <= PLAYER_LIMIT and player_name.lower() != "stop":
            player = Player(player_name)
            # Picking decks for main and terra for each player
            main_picked = False
            while not main_picked:
                print("These are the names of the loaded decks, please enter a name of one to pick it as your main deck")
                for deck_name in deck_names:
                    print(deck_name)
                picked_deck = input()
                if picked_deck in deck_names:
                    player.update_main_deck(deck_names[picked_deck])
                    player.shuffle_main_deck()
                    main_picked = True

            terra_picked = False
            while not terra_picked:
                print("These are the names of the loaded decks, please enter a name of one to pick it as your terra deck")
                for deck_name in deck_names:
                    print(deck_name)
                picked_deck = input()
                if picked_deck in deck_names:
                    player.update_terra_deck(deck_names[picked_deck])
                    player.shuffle_terra_deck()
                    terra_picked = True

            players.append(player)
        elif player_name.lower() != "stop":
            print("There are only", PLAYER_LIMIT, "players allowed, auto stopping player creation")
            player_name = "stop"
    random.shuffle(players)
    return players