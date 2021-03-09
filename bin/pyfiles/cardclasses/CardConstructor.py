import os
# Path to card's should bring up all folder's containing the different card types
path_to_cards = "\..\..\cards"
print("Starting")
for filename in os.listdir(os.getcwd() +path_to_cards):
    print(filename)
   #with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in readonly mode

      # do your stuff
print("Done")
