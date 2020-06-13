import pygame as pygame
import os
import stats
import enemies
import combat
import cave
import hallway

plat = stats.Player()
plat.room = "key"
plat.door = 0

#this is the walk screen for THE FIRST CAVE BEFORE THE PUZZLE

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'sprites')

pygame.init()

#setting screen size
screen = pygame.display.set_mode((1280,720))

#setting scenery and static objects
background = pygame.image.load(os.path.join(image_path, "keybg.jpg"))
screen.blit(background, (0,0))

ledge = pygame.image.load(os.path.join(image_path, "ledge.png"))
x = 250
y = 225
ledge_info = ["ledge", x, y]
screen.blit(ledge, (x,y))

long = pygame.image.load(os.path.join(image_path, "long.png"))
w = 522
h = 410
hill_info = ["long", w, h]
screen.blit(hill, (w, h))

edoor = pygame.image.load(os.path.join(image_path, "door.png"))
lm = 1228
lM = lm + edoor.get_width()
pm = 600
pM = pm + edoor.get_height()
edoor_info = ["exit", lm, pm, lM, pM]
screen.blit(door, (lm, pm))

    #idoor is the entry back into cave, no sprite
cm = 0
cM = 20
dm = 0
dM = 720
idoor_info = ["entry", cm, dm, cM, dM]

#setting non-static layers
#setting player (note that player does not currently have art, will use stand-in image)
player = pygame.image.load(os.path.join(image_path,"player.png"))
xpos = 100
ypos = 600
step_x = 30
step_y = 100
player_coord = [player, xpos, ypos]
screen.blit(player, (xpos, ypos))

#setting enemy (neither each class nor overworld enemy final art exist yet)
overworld = pygame.image.load(os.path.join(image_path,"slime mockup.png"))
wpos = 1080
hpos = ypos
step = 10
overworld_info = ["enemy", wpos, hpos]
screen.blit(overworld, (wpos, hpos))

#setting key
key = pygame.image.load(os.path.join(image_path, "key.png"))
lpos = 504
ppos = 234
key_info = ["key", lpos, ppos]
if plat.key == 0:
    screen.blit(key, (lpos, ppos))

pygame.display.update()

transparent = (0, 0, 0, 0)

def gamestate_checks(player_info):

    #colliders
    player_info = collision(player_info, ledge_info)
    player_info = collision(player_info, long_info)
    player_info = collision(player_info, overworld_info)
    if plat.key == 0:
        player_info = collision(player_info, key_info)
    
    #door checks
    while plat.door == 0:
        player_info = collision(player_info, edoor_info)
        player_info = collision(player_info, idoor_info)
    
    #checks which door to send to right room
    if plat.door == 1:
        hallway
    elif plat.door == 2:
        cave

    return player_info

def collision (player_info, object_info):

    #player info
    player = player_info[0]
    pxm = player_info[1]
    pxM = pxm + player.get_width()
    pym = player_info[2]
    pyM = pym + player.get_height()
    
    #locating object to check collision
    xm = object_info[1]
    ym = object_info[2]
    collider = object_info[0]
    
    #finding how to proceed based off of what object it is
    #this generally means finding accurate dimensions for things
    if collider == "ledge":
        xM = x + ledge.get_width()
        yM = y + ledge.get_height()
    elif collider == "long":
        xM = x + long.get_width()
        yM = y + long.get_height()
    elif collider == "enemy":
        combat
    elif collider == "key":
        #play kaching sound?
        plat.key = plat.key + 1
        key.fill(transparent)
    else:
        at_door(player_info)
        return plat.door

    #checking if both objects occupy the same space on screen, then offsetting position to "fix" the problem
    #will there be a thud sound? (how will player know they've collided if we don't provide feedback?)
    #lmk if this is confusing and/or will need explaining -v
    if (pxm in range (xm, xM)):
        #play thud noise here
        xpos = xpos + 20
    elif (pxM in range (xm, xM)):
        #play thud noise here
        xpos = xpos - 20

    if (pym in range (ym, yM)):
        #play thud noise here
        ypos = ypos + 20
    elif (pyM in range (ym, yM)):
        #play thud noise here
        ypos = ypos - 20

    return player_info 

def at_door (player_info, door_info):

    #player info
    player = player_info[0]
    pxm = player_info[1]
    pxM = pxm + player.get_width()
    pym = player_info[2]
    pyM = pym + player.get_height()

    #door info
    door = door_info[0]
    dxm = door_info[1]
    dym = door_info[2]
    dxM = door_info[3]
    dyM = door_info[4]

    if (pxm in range (dxm, dxM)):
        #print message prompting to interact with door
        print("Press X to enter.")
        if event.key == pygame.X:
            if door == "exit":
                plat.door = 1
            else:
                plat.door = 2
        #proxy message while we don't actually get the things done
    elif (pxM in range (dxm, dxM)):
        print("Press X to enter.")
        if event.key == pygame.X:
            if door == "exit":
                plat.door = 1
            else:
                plat.door = 2
    
    return plat.door
    
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                break
            elif event.key == pygame.K_DOWN:
                while event.key == pygame.K_DOWN:
                    ypos = ypos + step_y
                    gamestate_checks(player_coords)

            elif event.key == pygame.K_UP:
                while event.key == pygame.K_UP:
                    ypos = ypos - step_y
                    gamestate_checks(player_coords)

            elif event.key == pygame.K_RIGHT:
                while event.key == pygame.K_RIGHT:
                    xpos = xpos + step_x
                    gamestate_checks(player_coords)

            elif event.key == pygame.K_LEFT:
                while event.key == pygame.K_LEFT:
                    xpos = xpos - step_x
                    gamestate_checks(player_coords)

    screen.blit(background, (0,0))
    screen.blit(ledge, (x, y))
    screen.blit(long, (w, h))
    screen.blit(overworld, (wpos, hpos))
    screen.blit(key, (lpos, ppos))
    screen.blit(edoor, (lm,pm))
    screen.blit(player, (xpos, ypos))
    pygame.display.update()
