
# The point of this file is to contain all of the code to actually run the game once players are ready to play, have picked decks ect
from pyfiles.gameclasses.Player import Player
import random

# Constants
PLAYER_LIMIT = 2

# This is the enter point, for the player setup a list of decks should be provided
def run_game(decks):
    # This variable will be set to false once a player either wins, or quits the game
    game_run = True

    # These are the phases of the game, in order
    game_phases = ["Rest", "Draw", "UpKeep", "Main", "Attack", "Main2", "End"]


    # Player creation
    players = create_players(decks)

    while game_run:
        keep_going = input("Do you want to keep going? ")
        print(keep_going)
        if keep_going.lower() != "y" or len(players) < 2:
            game_run = False

        for player in players:
            for phase in game_phases:
                print("it's", player.get_name() + "'s turn, the phase is", phase)


def create_players(decks):
    players = []  # Each player created will be added to this list, then shuffle this and use it to determine turn order
    # Get a list of all deck names
    deck_names = {}

    for deck in decks:
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
                    main_picked = True

            terra_picked = False
            while not terra_picked:
                print("These are the names of the loaded decks, please enter a name of one to pick it as your terra deck")
                for deck_name in deck_names:
                    print(deck_name)
                picked_deck = input()
                if picked_deck in deck_names:
                    player.update_terra_deck(deck_names[picked_deck])
                    terra_picked = True

            players.append(player)
        elif player_name.lower() != "stop":
            print("There are only", PLAYER_LIMIT, "players allowed, auto stopping")
            player_name = "stop"
    random.shuffle(players)
    return players