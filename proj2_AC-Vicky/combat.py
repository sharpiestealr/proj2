import pygame as pg
import os
import stats
import enemies
import random

#determining player and enemy stats
plat = stats.Player()
enem_gen = random.randint(0,3)

boss = 'no'
if plat.croom == "final":
        boss = 'yes'

if enem_gen == 1:
    enem = enemies.Enemy('goblin', boss)
    enem_sprite = "goblin mockup.png"
    enem_name = "goblin"
elif enem_gen == 2:
    enem = enemies.Enemy('gnome', boss)
    enem_sprite = "gnome mockup.png"
    enem_name = "gnome"
else:
    enem = enemies.Enemy('slime', boss)
    enem_sprite = "slime mockup.png"
    enem_name = "slime"

result = 0

#importing sprite folders
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'sprites')

pg.init()

#creating screen and background
screen = pg.display.set_mode((1280,720))
background = pg.image.load(os.path.join(image_path, "combat bg.jpg"))
background = background.convert()

screen.blit(background, (0,0))
pg.display.update()

#creating box for player to pick action
box = pg.draw.rect(screen, [249, 228, 183], [0, 500, 1280, 213], 0)
pg.display.update()

font = pg.font.Font('freesansbold.ttf', 24)
text1 = font.render('Attack', True, [0, 0, 0])
text2 = font.render('Defense', True, [0, 0, 0])
text3 = font.render("Magic", True, [0, 0, 0])
textc = font.render("Choose an action", True, [0, 0, 0])
textp = font.render("Player: {0}".format(plat.hp), True, [0, 0, 0])
texte = font.render("{0}: {1}".format(enem.mob, enem.hp), True, [0, 0, 0])

text1Rect = text1.get_rect()
text2Rect = text2.get_rect()
text3Rect = text3.get_rect()
textcRect = textc.get_rect()
textpRect = textp.get_rect()
texteRect = texte.get_rect()

text1Rect.center = (1100, 540)
text2Rect.center = (1100, 590)
text3Rect.center = (1100, 640)
textcRect.center = (880, 590)
textpRect.center = (100, 540)
texteRect.center = (100, 590)

screen.blit(text1, text1Rect)
screen.blit(text2, text2Rect)
screen.blit(text3, text3Rect)
screen.blit(textc, textcRect)
screen.blit(textp, textpRect)
screen.blit(texte, texteRect)
pg.display.update()

#creating cursor for choice
ypos = 540
posi = 1
choice = pg.draw.circle(screen, [0, 0, 0], [1030, ypos], 9)

pg.display.update()

#placing character and enemy sprites
player_char = pg.image.load(os.path.join(image_path, "player.png"))
enem_char = pg.image.load(os.path.join(image_path, enem_sprite))

screen.blit(player_char, (1030,200))
screen.blit(enem_char, (250,200))
pg.display.update()

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            running = False
        elif event.type == pg.KEYDOWN:
            if plat.result != 0:
                running = False
                break
            if event.key == pg.K_ESCAPE:
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
            elif event.key == pg.K_RETURN:
                h = enemies.combat(enem_name, "no", posi)
                if h[0] <= 0:
                    healthp = 0
                    plat.result = 2
                else:
                    healthp = h[0]

                if h[1] <= 0:
                    healthe = 0
                    plat.result = 1
                else:
                    healthe = h[1]

                textp = font.render("Player: {0}".format(healthp), True, [0, 0, 0])
                texte = font.render("{0}: {1}".format(enem.mob, healthe), True, [0, 0, 0])
                
    if plat.result == 1:
        result_text = font.render('Victory!', True, [0, 0, 0],[249,228, 183])
        resultRect = result_text.get_rect()
        resultRect.center = (640, 360)
        screen.blit(result_text, resultRect)
    elif plat.result == 2:
        result_text = font.render('Lost!', True, [0, 0, 0],[249,228, 183])
        resultRect = result_text.get_rect()
        resultRect.center = (640, 360)
        screen.blit(result_text, resultRect)     

    box = pg.draw.rect(screen, [249, 228, 183], [0, 500, 1280, 213], 0)
    screen.blit(text1, text1Rect)
    screen.blit(text2, text2Rect)
    screen.blit(text3, text3Rect)
    screen.blit(textc, textcRect)
    screen.blit(textp, textpRect)
    screen.blit(texte, texteRect)
    choice = pg.draw.circle(screen, [0, 0, 0], [1030, ypos], 9)
    pg.display.update()