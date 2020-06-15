import pygame
import os
import stats
import random

#big bounds: x 365-913, y 88-623
#x1 x365 xmax539 y88 ymax262
#x2 x553 xmax78 y267 ymax441
#x3 x740 xmax913 y452 ymax623
#potion bounds: x 354-913, y 80-630

#generate big bounds box to determine blocks can't move past them
#generate 8 visible boxes and 9 transparent boxes
#   randomize the 8 visible boxes within big bounding box locating them by the transparent boxes
#   the transparent boxes are location markers to determine click area
#check for clicked area in transparent block bounding boxes and swap both blocks? sliding is harder
#check if all 8 boxes are where they should be
#   if they are, draw "solved" screen over by adding in a white flash? for transition
#   in place of the puzzle scene, lies big strength potion

#ORIENT PUZZLE FOR MOUSE CLICKING

transparent = (0, 0, 0, 0)
