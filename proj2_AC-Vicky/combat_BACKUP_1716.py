import pygame as pg
import os
import stats
import enemies
import random

#determining player and enemy stats
plat = stats.Player()
<<<<<<< HEAD:proj2_AC-Vicky/combat.py
enem = enemies.Enemy('goblin', 'no')
enem_gen = random.randint(0,3)
boss = 'no'
    if plat.room == "final":
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
=======
enem_gen = random.randint(0,3)
if enem_gen == 1:
    enem = enemies.Enemy('goblin', 'no')
    enem_sprite = "goblin mockup.png"
    enem_name = "goblin"
elif enem_gen == 2:
    enem = enemies.Enemy('gnome', 'no')
    enem_sprite = "gnome mockup.png"
    enem_name = "gnome"
else:
    enem = enemies.Enemy('slime', 'no')
>>>>>>> c261457a15a0b3e5986d8502b13f4ab191292d67:proj2_AC-Vicky/combatscreen.py
    enem_sprite = "slime mockup.png"
    enem_name = "slime"

result = 0

#importing sprite folders
current_path = os.path.dirname(__file__)
@@ -13,16 +29,15 @@
pg.init()

#creating screen and background
<<<<<<< HEAD:proj2_AC-Vicky/combat.py
screen = pg.display.set_mode((640,480))
background = pg.Surface(screen.get_size())
background.fill((17,143,139))
=======
>>>>>>> c261457a15a0b3e5986d8502b13f4ab191292d67:proj2_AC-Vicky/combatscreen.py
screen = pg.display.set_mode((1280,720))
background = pg.image.load(os.path.join(image_path, "combat bg.jpg"))
background = background.convert()

screen.blit(background, (0,0))
pg.display.update()

#creating box for player to pick action
<<<<<<< HEAD:proj2_AC-Vicky/combat.py
box = pg.draw.rect(screen, [249, 228, 183], [0, 300, 640, 213], 0)
=======
>>>>>>> c261457a15a0b3e5986d8502b13f4ab191292d67:proj2_AC-Vicky/combatscreen.py
box = pg.draw.rect(screen, [249, 228, 183], [0, 500, 1280, 213], 0)
pg.display.update()

font = pg.font.Font('freesansbold.ttf', 24)
@@ -40,12 +55,12 @@
textpRect = textp.get_rect()
texteRect = texte.get_rect()

<<<<<<< HEAD:proj2_AC-Vicky/combat.py
text1Rect.center = (540, 340)
text2Rect.center = (540, 390)
text3Rect.center = (540, 440)
textcRect.center = (320, 390)
textpRect.center = (100, 340)
texteRect.center = (100, 390)
=======
>>>>>>> c261457a15a0b3e5986d8502b13f4ab191292d67:proj2_AC-Vicky/combatscreen.py
text1Rect.center = (1100, 540)
text2Rect.center = (1100, 590)
text3Rect.center = (1100, 640)
textcRect.center = (880, 590)
textpRect.center = (100, 540)
texteRect.center = (100, 590)

screen.blit(text1, text1Rect)
screen.blit(text2, text2Rect)
@@ -56,43 +71,75 @@
pg.display.update()

#creating cursor for choice
<<<<<<< HEAD:proj2_AC-Vicky/combat.py
ypos = 340
ypos = 540
posi = 1
choice = pg.draw.circle(screen, [0, 0, 0], [470, ypos], 9)
choice = pg.draw.circle(screen, [0, 0, 0], [1030, ypos], 9)

pg.display.update()

#placing character and enemy sprites
player_char = pg.image.load(os.path.join(image_path, "player.png"))
enem_char = pg.image.load(os.path.join(image_path, enem_sprite))
=======
ypos = 540
posi = 1
choice = pg.draw.circle(screen, [0, 0, 0], [1030, ypos], 9)
>>>>>>> c261457a15a0b3e5986d8502b13f4ab191292d67:proj2_AC-Vicky/combatscreen.py

screen.blit(player_char, (1030,200))
screen.blit(enem_char, (250,200))
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
            if result != 0:
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
<<<<<<< HEAD:proj2_AC-Vicky/combat.py
                h = enemies.combat("goblin", "no", posi)
                healthp = h[0]
                healthe = h[1]
=======
>>>>>>> c261457a15a0b3e5986d8502b13f4ab191292d67:proj2_AC-Vicky/combatscreen.py
                h = enemies.combat(enem_name, "no", posi)
                if h[0] <= 0:
                    healthp = 0
                    result = 2
                else:
                    healthp = h[0]

                if h[1] <= 0:
                    healthe = 0
                    result = 1
                else:
                    healthe = h[1]

                textp = font.render("Player: {0}".format(healthp), True, [0, 0, 0])
                texte = font.render("{0}: {1}".format(enem.mob, healthe), True, [0, 0, 0])
<<<<<<< HEAD:proj2_AC-Vicky/combat.py
    box = pg.draw.rect(screen, [249, 228, 183], [0, 300, 640, 213], 0)

=======
                
>>>>>>> c261457a15a0b3e5986d8502b13f4ab191292d67:proj2_AC-Vicky/combatscreen.py
    if result == 1:
        result_text = font.render('Victory!', True, [0, 0, 0],[249,228, 183])
        resultRect = result_text.get_rect()
        resultRect.center = (640, 360)
        screen.blit(result_text, resultRect)
    elif result == 2:
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
<<<<<<< HEAD:proj2_AC-Vicky/combat.py
    choice = pg.draw.circle(screen, [0, 0, 0], [470, ypos], 9)
=======
>>>>>>> c261457a15a0b3e5986d8502b13f4ab191292d67:proj2_AC-Vicky/combatscreen.py
    choice = pg.draw.circle(screen, [0, 0, 0], [1030, ypos], 9)
    pg.display.update()