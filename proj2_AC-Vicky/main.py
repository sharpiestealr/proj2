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

plat.croom = "cave"

if (plat.croom == "cave"):
    running = True
plat = cavescreen1.cave_run(plat, running)

if (plat == "combat"):
    plat = combat.combat(plat)

if (plat == "chest"):
    running = True
plat = chestscreen1.chest_run(plat, running)

if (plat == "key"):
    running = True
plat = keyscreen1.key_run(plat, running)

if (plat == "hallway"):
    running = True
plat = hallwayscreen1.hallway_run(plat, running)