import pygame
import os
import stats
import random
import cavescreen1
import combat
import chestscreen1
import keyscreen1
import hallwayscreen1
import doorscreen1
import puzzlescreen1
import finalscreen1
import openingscreen

plat = stats.Player()
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'sprites')
sound_path = os.path.join(current_path, 'sounds')

pygame.init()

running = False #add this below the change in croom    

#draw opening title here
#new game prompts to player creation
#have title pull into cave

plat.croom = "opening"

while plat.stop == 0:
    if plat.croom == "opening":
        plat = openingscreen.opening_run(plat)

    if (plat.croom == "cave"):
        running = True
        plat = cavescreen1.cave_run(plat, running)

    if (plat.croom == "combat"):
        result = combat.combat_run()
        if result == 1:
            if plat.lastroom != "chest":
                plat.croom = plat.lastroom
                plat.lastroom = "combat"
            else:
                plat.croom = "cave"
                plat.lastroom = "combat"
        elif result == 2:
            plat.stop = 1

    if (plat.croom == "chest"):
        if plat.chest == 0:
            running = True
            plat = chestscreen1.chest_run(plat, running)
        else:
            running = True
            plat = cavescreen1.cave_run(plat, running)

    if (plat.croom == "key"):
        running = True
        plat = keyscreen1.key_run(plat, running)

    if (plat.croom == "hallway"):
        running = True
        plat = hallwayscreen1.hallway_run(plat, running)
    
    if (plat.croom == "doors"):
        running = True
        plat = doorscreen1.door_run(plat, running)
    
    if (plat.croom == "final"):
        running = True
        plat = finalscreen1.door_run(plat, running)

    #gen credits outside loop?