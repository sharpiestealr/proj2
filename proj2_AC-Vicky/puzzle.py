#ac needs to build the puzzle room here

import pygame as pygame
import os
import stats

plat = stats.Player
plat.room = "puzzle"

#in here, please put the "solved puzzle" section too
#the bg for puzzle default is puzzle1
#the names for the pieces are their final coordinates in (x,y)
#example: 11 is top left, 12 is middle left, 13 is bottom left
#feel free to rename them tbh
#the coordinates for it are:
#   potion x 354, y 80
#all you have to do is check plat.solved for 1 instead of default 0
#then draw puzzle2 as the bg