import pygame as pg
import os
import stats
import enemies

plat = stats.Player()
enem = enemies.Enemy('goblin', 'no')

#importing sprite folders
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'sprites')

pg.init()

#creating screen and background
screen = pg.display.set_mode((640,480))
background = pg.Surface(screen.get_size())
background.fill((17,143,139))
background = background.convert()

screen.blit(background, (0,0))
pg.display.update()

#creating box for player to pick action
box = pg.draw.rect(screen, [249, 228, 183], [0, 300, 640, 213], 0)
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

text1Rect.center = (540, 340)
text2Rect.center = (540, 390)
text3Rect.center = (540, 440)
textcRect.center = (320, 390)
textpRect.center = (100, 340)
texteRect.center = (100, 390)

screen.blit(text1, text1Rect)
screen.blit(text2, text2Rect)
screen.blit(text3, text3Rect)
screen.blit(textc, textcRect)
screen.blit(textp, textpRect)
screen.blit(texte, texteRect)
pg.display.update()

#creating cursor for choice
ypos = 340
posi = 1
choice = pg.draw.circle(screen, [0, 0, 0], [470, ypos], 9)

pg.display.update()

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
                break
            elif event.key == pg.K_DOWN:
                if posi < 3:
                    ypos = ypos + 50
                    posi = posi + 1
                    print(posi)
            elif event.key == pg.K_UP:
                if posi > 1:
                    ypos = ypos - 50
                    posi = posi - 1
            elif event.key == pg.K_RETURN:
                h = enemies.combat("goblin", "no", posi)
                healthp = h[0]
                healthe = h[1]
                textp = font.render("Player: {0}".format(healthp), True, [0, 0, 0])
                texte = font.render("{0}: {1}".format(enem.mob, healthe), True, [0, 0, 0])
    box = pg.draw.rect(screen, [249, 228, 183], [0, 300, 640, 213], 0)
    screen.blit(text1, text1Rect)
    screen.blit(text2, text2Rect)
    screen.blit(text3, text3Rect)
    screen.blit(textc, textcRect)
    screen.blit(textp, textpRect)
    screen.blit(texte, texteRect)
    choice = pg.draw.circle(screen, [0, 0, 0], [470, ypos], 9)
    pg.display.update()