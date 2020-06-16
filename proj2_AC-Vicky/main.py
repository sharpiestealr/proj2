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

opening = pygame.image.load(os.path.join(image_path, "opening.jpg"))
screen.blit(background, (0,0))
pygame.display.flip()

running = True
posi = 1

while running:
    for event in pg.event.get():
        if event.key == pg.K_ESCAPE:
            plat.stop = 1
            running = False
            break
        elif event.key == pg.K_DOWN:
            if posi < 3:
                ypos = ypos + 50
                posi = posi + 1
        elif event.key == pg.K_UP:
            if posi > 1:
                ypos = ypos - 50
                posi = posi - 1
        if event.key == pg.K_x:
            if posi == 1:
                instructions = pygame.image.load(os.path.join(image_path, "instructions.jpg"))
                screen.blit(instructions, (0,0))
                pygame.display.flip()
    

#draw opening title here
#new game prompts to player creation
#have title pull into cave

plat.croom = "cave"

while plat.stop == 0:
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