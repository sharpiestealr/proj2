import pygame
import os
import stats
import enemies
import random
import cavescreen1

plat = stats.Player()

#draw opening title here
#new game prompts to player creation
#have title pull into cave

plat.croom = cavescreen1.cave_assets(plat)
if (plat.croom == "cave"):
    running = True
plat.croom = cavescreen1.cave_run(plat)

#no need to pull into other files because cave pulls into chest and key, which will pull the next ones  