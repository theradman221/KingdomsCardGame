import os
os.add_dll_directory(os.getcwd())

from steamworks import STEAMWORKS

steamworks = STEAMWORKS()
steamworks.initialize()

my_steam64 = steamworks.Users.GetSteamID()
my_steam_level = steamworks.Users.GetPlayerSteamLevel()

print(f'Logged on as {my_steam64}, level: {my_steam_level}')
print('Is subscribed to current app?', steamworks.Apps.IsSubscribed())