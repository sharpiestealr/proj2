import pygame as pg
import os
import stats
import random

#importing sprite folders
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'sprites')
sound_path = os.path.join(current_path, 'sounds')

pg.init()

plat = stats.Player()
posi = 1

class Enemy(object): #pygame.sprite no pygame
    """a place to create enemy variables, generate enemies and combats"""
    
    def __init__(self, enemy_type, boss): #generates the enemies
        #chooses the enemy class
        if enemy_type == 'goblin':
            self.hp = 8
            self.atk = 3
            self.df = 3
            self.mob = "Goblin"
        elif enemy_type == 'gnome':
            self.hp = 7
            self.atk = 3
            self.df = 5
            self.mob = "Gnome"
        elif enemy_type == 'slime':
            self.hp = 10
            self.atk = 3
            self.df = 4
            self.mob = "Slime"
        #checks if enemy has boss factor
        if boss == 'yes':
            self.hp = self.hp*2
            self.atk = self.atk*2
            self.df = self.df*2
            self.xp = self.xp*2
        #combat variables
        self.dmg = 0
        self.res = 0

    #methods to define the attack choice of the enemies
    def gob_ATK(self):
        chance = random.randint(0,100)
        if chance <= 30:
            self.attack = 'defense'
        else:
            self.attack = 'attack'
        
    def gno_ATK(self):
        chance = random.randint(0,100)
        if chance <= 15:
            self.attack = 'attack'
        elif chance <= 75:
            self.attack = 'defense'
        else:
            self.attack = 'magic'

    def sli_ATK(self):
        chance = random.randint(0,100)
        if chance <= 15:
            self.attack = 'attack'
        elif chance <= 40:
            self.attack = 'defense'
        else:
            self.attack = 'magic'

    #method to determine damage
    def rps(self, player_choice):
        #if both are the same
        if (plat.player_combat.action == self.attack):
            if plat.player_combat.action == 'attack':
                plat.player_combat.dmg = plat.player_combat.atk +1
                plat.player_combat.res = 1
                self.dmg = self.atk +1
                self.res = 1
            elif plat.action == 'defense':
                plat.player_combat.dmg = plat.player_combat.atk -1
                plat.player_combat.res = -1
                self.dmg = self.atk -1
                self.res = -1
            elif plat.action == 'magic':
                plat.player_combat.dmg = plat.player_combat.atk
                plat.player_combat.res = 0
                self.dmg = self.atk
                self.res = 0
        #if they are different - by player
        elif (plat.player_combat.action == 'attack'):
            plat.player_combat.dmg = plat.player_combat.atk +1
            plat.player_combat.res = +1
            if (self.attack == 'defense'):
                self.dmg = self.atk -1
                self.res = -1
            elif (self.attack == 'magic'):
                self.dmg = self.atk
                self.res = 0
        elif (plat.player_combat.action == 'defense'):
            plat.player_combat.dmg = plat.player_combat.atk -1
            plat.player_combat.res = -1
            if (self.attack == 'attack'):
                self.dmg = self.atk +1
                self.res = +1
            elif (self.attack == 'magic'):
                self.dmg = self.atk
                self.res = 0
        elif (plat.player_combat.action == 'magic'):
            plat.player_combat.dmg = plat.player_combat.atk
            plat.player_combat.res = 0
            if (self.attack == 'attack'):
                self.dmg = self.atk +1
                self.res = +1
            elif (self.attack == 'defense'):
                self.dmg = self.atk -1
                self.res = -1

class Player_c():
    def __init__(self):
        #self.name = input("What's your name, adventurer? ")  
        self.hp = 12
        self.atk = 4
        self.df = 4

        #combat variables
        self.dmg = 0
        self.res = 0

    def pattack(self, posi):
        if posi == 1:
            self.action = "attack"
        elif posi == 2:
            self.action = "defense"
        else:
            self.action = "magic"

def combat_calc(enem, attk): #, mob_size to add if necessary
    #generating enemy
    #generating each single attack
    #defining enemy attack and player attack
    if enem.mob == 'Goblin':
       enem.gob_ATK()
    elif enem.mob == 'Gnome':
       enem.gno_ATK()
    elif enem.mob == 'Slime':
       enem.sli_ATK()
    choice = enem.attack

    #calculate damage, place damage
    enem.rps(attk)
    enem.hp = enem.hp - (plat.player_combat.dmg + enem.res)
    plat.player_combat.hp = plat.player_combat.hp - (enem.dmg + plat.player_combat.res)
    info = [plat.player_combat.hp, enem.hp, choice]
    return info

def combat_run():
    plat.player_combat = Player_c()
    #determining player and enemy stats
    enem_gen = random.randint(1,3)

    boss = 'no'
    if plat.croom == "final":
            boss = 'yes'

    if enem_gen == 1:
        enem = Enemy('goblin', boss)
        enem_sprite = "goblin.png"
        enem_name = "goblin"
    elif enem_gen == 2:
        enem = Enemy('gnome', boss)
        enem_sprite = "gnome.png"
        enem_name = "gnome"
    else:
        enem = Enemy('slime', boss)
        enem_sprite = "slime.png"
        enem_name = "slime"

    result = 0

    #creating screen and background
    screen = pg.display.set_mode((1280,720))
    background = pg.image.load(os.path.join(image_path, "combat bg.jpg"))
    background = background.convert()

    screen.blit(background, (0,0))

    #creating box for player to pick action
    box = pg.image.load(os.path.join(image_path, "text box back.png"))
    box = pg.transform.scale(box, (1350, 500))
    screen.blit(box, (-50,500))

    #healthbar
    heart1 = pg.image.load(os.path.join(image_path, "hp.png"))
    heart2 = pg.image.load(os.path.join(image_path, "hp.png"))

    screen.blit(heart1, (10, 10))
    screen.blit(heart2, (1170, 10))

    #vs symbol
    vs = pg.image.load(os.path.join(image_path, "x.png"))
    screen.blit(vs, (550, 250))

    #choices
    attack_s = pg.image.load(os.path.join(image_path, "attack.png"))
    def_s = pg.image.load(os.path.join(image_path, "defense.png"))
    magic_s = pg.image.load(os.path.join(image_path, "magic.png"))

    font = pg.font.Font('freesansbold.ttf', 36)
    text1 = font.render('Attack', True, [0, 0, 0])
    text2 = font.render('Defense', True, [0, 0, 0])
    text3 = font.render("Magic", True, [0, 0, 0])
    textc = font.render("Choose an action", True, [0, 0, 0])
    textp = font.render("{0}".format(plat.hp), True, [0, 0, 0])
    texte = font.render("{0}".format(enem.hp), True, [0, 0, 0])

    text1Rect = text1.get_rect()
    text2Rect = text2.get_rect()
    text3Rect = text3.get_rect()
    textcRect = textc.get_rect()
    textpRect = text3.get_rect()
    texteRect = textc.get_rect()

    text1Rect.center = (900, 560)
    text2Rect.center = (900, 610)
    text3Rect.center = (900, 660)
    textcRect.center = (550, 610)
    textpRect.center = (1250, 50)
    texteRect.center = (200, 50)

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
    cursor = pg.image.load(os.path.join(image_path, "arrow.png"))
    cursor = pg.transform.scale(cursor, (int(cursor.get_width()*0.25), int(cursor.get_height()*0.25)))

    #placing character and enemy sprites
    player_char = pg.image.load(os.path.join(image_path, "man still.png"))
    player_char = pg.transform.flip(player_char, True,False)
    enem_char = pg.image.load(os.path.join(image_path, enem_sprite))

    screen.blit(player_char, (1030,200))
    screen.blit(enem_char, (150,200))
    screen.blit(cursor, (750, ypos))
    pg.display.update()

    running = True

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                plat.stop = 1 
                running = False
            elif event.type == pg.KEYDOWN:
                if result != 0:
                    return result
                    running = False
                    break
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
                elif event.key == pg.K_x:
                    attk = plat.player_combat.pattack(posi)
                    print(posi)
                    print(attk)
                    h = combat_calc(enem, attk)
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

                    textp = font.render("{0}".format(healthp), True, [0, 0, 0])
                    texte = font.render("{0}".format(healthe), True, [0, 0, 0]) 

        screen.blit(background, (0,0))
        screen.blit(player_char, (1030,200))
        screen.blit(enem_char, (150,200))
        screen.blit(box, (-50,500))
        screen.blit(heart1, (10, 10))
        screen.blit(heart2, (1170, 10))
        screen.blit(text1, text1Rect)
        screen.blit(text2, text2Rect)
        screen.blit(text3, text3Rect)
        screen.blit(textc, textcRect)
        screen.blit(textp, textpRect)
        screen.blit(texte, texteRect)
        screen.blit(cursor, (750, ypos))
        screen.blit(vs, (550, 250))
        if result == 1:
            result_text = pg.image.load(os.path.join(image_path, "victory.png"))
            screen.blit(result_text, (550, 250))
        elif result == 2:
            result_text = pg.image.load(os.path.join(image_path, "you died.png"))
            screen.blit(result_text, (550, 250))  

        pg.display.update()