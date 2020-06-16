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
import chestscreen2
import finalscreen1
import openingscreen
import creditscreen

#importing paths and infos
plat = stats.Player()
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'sprites')
sound_path = os.path.join(current_path, 'sounds')

pygame.init()

running = False #add this below the change in croom    

#defining inicial screen
plat.croom = "opening"

#main game loop, calls every screen with the name and variable croom (current room) stored in Player() class 
while plat.stop == 0: #variable to determine if the game is still running
    if plat.croom == "opening":
        plat = openingscreen.opening_run(plat)

    if (plat.croom == "cave"):
        running = True
        plat = cavescreen1.cave_run(plat, running)

    if (plat.croom == "combat"):
        #determine boss battle
        if plat.lastroom != "final":
            result = combat.combat_run(0)
        else:
            result = combat.combat_run(1)

        if result == 1: #if player wins
            if plat.lastroom == "final": #if boss battle, end game
                plat.croom = "credits"
            elif  plat.lastroom == "chest1": #if chest room, force exit
                plat.croom = "cave"
                plat.lastroom = "combat"
            elif  plat.lastroom == "chest2": #if chest room, force exit
                plat.croom = "doors"
                plat.lastroom = "combat"
            else: #return to current room where enemy was faced
                plat.croom = plat.lastroom
                plat.lastroom = "combat"     
        elif result == 2: #if player loses, quit game
            plat.stop = 1

    if (plat.croom == "chest1"): #only one chest1 room is available. Key to make sure it doesn't respawn
        if plat.chest1 == 0:
            running = True
            plat = chestscreen1.chest_run(plat, running)
        else:
            running = True
            plat = cavescreen1.cave_run(plat, running)

    if (plat.croom == "chest2"): #only one chest2 room is available. Key to make sure it doesn't respawn
        if plat.chest2 == 0:
            running = True
            plat = chestscreen2.chest_run(plat, running)
        else:
            running = True
            plat = doorscreen1.door_run(plat, running)

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
        plat = finalscreen1.final_run(plat, running)
        
    if (plat.croom == "credits"):
        running = True
        plat = creditscreen.credits_run(plat, running)
