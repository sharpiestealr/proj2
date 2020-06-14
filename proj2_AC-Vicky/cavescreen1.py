import pygame
import os
#import combat

#this is the walk screen for THE FIRST CAVE BEFORE THE PUZZLE

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'sprites')

pygame.init()

#setting screen size
screen = pygame.display.set_mode((1280,720))

#setting scenery and static objects
background = pygame.image.load(os.path.join(image_path, "walk.jpg"))
screen.blit(background, (0,0))

ledge = pygame.image.load(os.path.join(image_path, "ledge.png"))
x = 442
y = 368
ledge_info = ["ledge", x, y]
screen.blit(ledge, (x,y))
ledge_hitbox = ledge.get_rect()


hill = pygame.image.load(os.path.join(image_path, "hill.png"))
w = 974
h = 224
hill_info = ["hill", w, h]
screen.blit(hill, (w, h))
hill_hitbox = hill.get_rect()

edoor = pygame.image.load(os.path.join(image_path, "door.png"))
lm = 1230
lM = lm + edoor.get_width()
pm = 605
pM = pm + edoor.get_height()
edoor_info = ["exit", lm, pm, lM, pM]
screen.blit(edoor, (lm, pm))

    #pdoor is puzzle door, no extra sprite for it
am = 1082
aM = 1280
bm = 0
bM = 224
pdoor_info = ["puzzle", am, bm, aM, bM]

    #idoor is entry door, no extra sprite either
cm = 0
cM = 95
dm = 378
dM = 605
idoor_info = ["entry", cm, dm, cM, dM]
    
#setting player
#note that player does not currently have art, will use stand-in image
player = pygame.image.load(os.path.join(image_path,"player.png"))
xpos = 100
ypos = 405
step_x = 30
step_y = 230
isJump = False
jumpCount = 11
player_coord = [player, xpos, ypos]
screen.blit(player, (xpos, ypos))
player_hitbox = player.get_rect()

#setting enemy
#neither each class nor overworld enemy art exist yet
overworld = pygame.image.load(os.path.join(image_path,"slime mockup.png"))
wpos = 780
hpos = 405
step = 10
overworld_info = ["enemy", wpos, hpos]
screen.blit(overworld, (wpos, hpos))
overworld_hitbox = player.get_rect()

#setting coin
coin = pygame.image.load(os.path.join(image_path, "coin.png"))
lpos = 514
ppos = 234
coin_info = ["coin", lpos, ppos]
screen.blit(coin, (lpos, ppos))
coin_hitbox = player.get_rect()

pygame.display.update()

transparent = (0, 0, 0, 0)
    
running = True

while running:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        running = False
        break

    if not(isJump):
        if keys[pygame.K_UP]:
            isJump = True
    else:
        if jumpCount >= -11:
           ypos -= (jumpCount * abs(jumpCount)) * 0.5
           jumpCount -= 1
        else: # This will execute if our jump is finished
           jumpCount = 11
           isJump = False
           # Resetting our Variables

    if keys[pygame.K_RIGHT] and xpos < 1100:
        xpos = xpos + step_x
       
    if keys[pygame.K_LEFT] and xpos > 100:
       xpos = xpos - step_x

    hit_ledge = pygame.sprite.collide_rect(player_hitbox, ledge_hitbox)

    if hit_ledge:
        ypos = 368

    screen.blit(background, (0,0))
    screen.blit(ledge, (x, y))
    screen.blit(hill, (w, h))
    screen.blit(overworld, (wpos, hpos))
    overworld_hitbox = overworld.get_rect()
    screen.blit(player, (xpos, ypos))
    player_hitbox = player.get_rect()
    screen.blit(coin, (lpos, ppos))
    pygame.display.update()