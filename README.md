# Text-Based-Adventure
First attempt at a text-based adventure.  Not quite working. Game will break somewhere in the "world.py" program.

Code runs but crashes with following message:

"
C:\Users\hp\AppData\Local\Programs\Python\Python38-32\python.exe "C:/Users/hp/Documents/Python Game/game.py"
Loading Tiles...
Find25GoldRoom
Importing tiles breaks the program.
I work
0
0
LeaveCaveRoom
Importing tiles breaks the program.
I work
3
0
LeaveCaveRoom

Importing tiles breaks the program.
Traceback (most recent call last):
  File "C:/Users/hp/Documents/Python Game/game.py", line 34, in <module>
    play()
  File "C:/Users/hp/Documents/Python Game/game.py", line 8, in play
    world.load_tiles()
  File "C:\Users\hp\Documents\Python Game\world.py", line 28, in load_tiles
    getattr(__import__('tiles'), tile_name)(x, y)
AttributeError: module 'tiles' has no attribute 'LeaveCaveRoom
'

Process finished with exit code 1
"
