# THE-NEW-GAME
This game is developed in python 2.
Then converted to python 3.

Creator: Brandon Robinson

Code Updated Date: 10/31/21

Current Version: 0.2.9

Next Version: 0.3.0 #This will be a Patch Version

Github Updated Date: 11/01/21 9:39 AM Eastern Time

Files updated:
  1. patch_notes_next.txt

Files created:
  1. None

Things to note:
  1. None

Save file problems:
  1. Make sure the save file is exactly named "Save.gsf".
  2. Open the save file and go to the bottom. If the version does not match game version the 
file will not work.
  3. If you cannot find a newer/older version of a save file for the version of the game you have you can change the variable version_save = ''.
  4. Note you may encounter problems if the save file is older than the game version. Try and use a newer save file than older if possible. Older save files are missing required variables.
  5. If a save file will no longer load. Try making a new one with save_file_maker.py.

To start the game:
1. To start the game. You need to change the file name Version #.#.#.py to main.py.
2. Then in the file renamed to main.py change the variable (path) to the directory where all the game files will be stored.
3. Make sure path has 2 slashes instead of 1.
4. Check to see if you are running python 2 or 3. Python 2 is not compatible with this version.
5. Make sure you have a compatible save file(Save.gsf).
6. If dev mode is enabled and you encounter problems try disabling it either with the variable or in the game menu.
7. Play the game.

Files required to start:
  1. Save.gsf
  2. error_stuff.py #Not required but will cause problems without it.
  3. main.py
