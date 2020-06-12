import pygame
import os

#this is the walk screen for THE FIRST CAVE BEFORE THE PUZZLE

current_path = os.path.dirname(_file_)
image_path = os.path.join(current_path, 'sprites')

pygame.init()

#setting screen size
screen = pygame.display.set_mode((1280,720))

#setting scenery and static objects
background = pygame.image.load(os.path.join(image_patg, "walk.jpg"))
screen.blit(background, (0,0))

ledge = pygame.image.load(os.path.join(image_path, "ledge.png"))
ledge_info = ["ledge", x, y]
x = background.get_width() - ledge.get_width()
y = background.get_height() - ledge.get_height()
screen.blit(ledge, (x,y))

hill = pygame.image.load(os.path.join(image_path, "hill.png"))
hill_info = ["hill", w, h]
w = background.get_width() - hill.get_width()
h = background.get_height() - hill.get_height()
screen.blit(hill, (w, h))
    
#setting player
#note that player does not currently have art, will use stand-in image
player = pygame.image.load(os.path.join(image_path,"player.png"))
player_coord = [player, xpos, ypos]
xpos = 100
ypos = background.get_height() - 75
step_x = 30
step_y = 100
screen.blit(player, (xpos, ypos))

#setting enemy
#neither each class nor overworld enemy art exist yet
overworld = pygame.image.load(os.path.join(image_path,"overworld.png"))
overworld_info = ["enemy", wpos, hpos]
wpos = background.get_width() - 300
hpos = background.get_height() - 75
step = 10

screen.blit(overworld, (wpos, hpos))
pygame.display.update()

#collision check
def collision (player_info, object_info):

    sprite = player_info[0]
    xpos = player_info[1]
    ypos = player_info[2]

    #locating player
    pxm = xpos
    pxM = xpos + player.get_width()
    pym = ypos
    pyM = ypos + player.get_height()
    
    #locating object to check collision
    xm = object_info[1]
    ym = object_info[2]
    collider = object_info[0]
    
    if collider == "ledge":
        xM = x + ledge.get_width()
        yM = y + ledge.get_height()
    elif collider == "hill":
        xM = x + hill.get_width()
        yM = y + hill.get_height()
    elif collider == "enemy":
        xM = x + overworld.get_width()
        yM = y + overworld.get_height()
    
    #checking if both objects occupy the same space on screen, then offsetting position to "fix" the problem
    #will there be a thud sound? (how will player know they've collided if we don't provide feedback?)
    #lmk if this is confusing and/or will need explaining -v
    if (pxm in range (xm, xM)):
        xpos = xpos + 20
    elif (pxM in range (xm, xM)):
        xpos = xpos - 20

    if (pym in range (ym, yM)):
        ypos = ypos + 20
    elif (pyM in range (ym, yM)):
        ypos = ypos - 20

    return player_info 

def at_door (player_info):

    door = 0
    #check for if the player enters a door
    #default is 0 for "no door", if door is a go, 1

    sprite = player_info[0]
    xpos = player_info[1]
    ypos = player_info[2]

    #locating player
    pxm = xpos
    pxM = xpos + player.get_width()
    pym = ypos
    pyM = ypos + player.get_height()
    
    exit1m = 0 #entry door
    exit1M = 20

    exit2m = background.get_width()-20 #exit door
    exit2M = background.get_width()

    chestm = background.get_width() - 300
    chestM = baground.get_width() - 20

    if (pxm in range (exit1m, exit1M)) or (pxm in range (exit2m, exit2M)) or (pxm in range (chestm, chestM)):
        #print message prompting to interact with door
        print("Press z to enter.")
        if event.key == pygame.X:
            door = 1
        #proxy message while we don't actually get the things done
    elif (pxM in range (exit1m, exit1M)) or (pxM in range (exit2m, exit2M)) or (pxM in range (chestm, chestM)):
        print("Press z to enter.")
        if event.key == pygame.X:
            door = 1
    return door
    
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
                ypos = ypos + step_y
                player_coord = collision(player_coord, ledge_info)
                player_coord = collision(player_coord, hill_info)
                player_coord = collision(player_coord, overworld_info)
            elif event.key == pygame.K_UP:
                ypos = ypos - step_y
                player_coord = collision(player_coord, ledge_info)
                player_coord = collision(player_coord, hill_info)
                player_coord = collision(player_coord, overworld_info)
            elif event.key == pygame.K_RIGHT:
                xpos = xpos + step_x
                player_coord = collision(player_coord, ledge_info)
                player_coord = collision(player_coord, hill_info)
                player_coord = collision(player_coord, overworld_info)
            elif event.key == pygame.K_LEFT:
                xpos = xpos - step_x
                player_coord = collision(player_coord, ledge_info)
                player_coord = collision(player_coord, hill_info)
                player_coord = collision(player_coord, overworld_info)

                #i made the door check method already but i haven't actually implemented it yet ok

    screen.blit(background, (0,0))
    screen.blit(ledge, (x, y))
    screen.blit(hill, (w, h))
    screen.blit(overworld, (wpos, hpos))
    screen.blit(player, (xpos, ypos))
    pygame.display.update()