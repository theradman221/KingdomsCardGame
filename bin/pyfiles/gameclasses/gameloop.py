
# The point of this file is to contain all of the code to actually run the game once players are ready to play, have picked decks ect
from pyfiles.gameclasses.Player import Player
import random

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
    player_names = ["Bobby", "Jill", "Fred", "Brian", "George"]
    for name in player_names:
        player = Player(name)
        players.append(player)
    random.shuffle(players)
    return players