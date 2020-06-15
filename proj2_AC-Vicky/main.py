import pygame
import os
import stats
import enemies
import random
import cavescreen1
import combat
import chestscreen1
import keyscreen1
import hallwayscreen1
import doorscreen1
import puzzlescreen1
import finalscreen1

plat = stats.Player()
running = False #add this below the change in croom

#draw opening title here
#new game prompts to player creation
#have title pull into cave

while plat.stop == 0:
    if (plat.croom == "cave"):
        running = True
        plat = cavescreen1.cave_run(plat, running)

    if (plat.croom == "combat"):
        plat = combat.combat_run(plat)

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