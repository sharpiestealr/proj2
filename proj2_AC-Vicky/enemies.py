import stats
import random
plat = stats.Player()

class Enemy(object): #pygame.sprite no pygame
    """a place to create enemy variables, generate enemies and combats"""
    
    def __init__(self, enemy_type, boss): #generates the enemies
        #chooses the enemy class
        if enemy_type == 'goblin':
            self.hp = 6+2*plat.level
            self.atk = 2+1*plat.level
            self.df = 2+1*plat.level
            self.xp = 5+2*plat.level
            self.mob = "Goblin"
        elif enemy_type == 'gnome':
            self.hp = 5+2*plat.level
            self.atk = 2+1*plat.level
            self.df = 3+2*plat.level
            self.xp = 4+2*plat.level
            self.mob = "Gnome"
        elif enemy_type == 'slime':
            self.hp = 8+2*plat.level
            self.atk = 2+1*plat.level
            self.df = 2+2*plat.level
            self.xp = 6+2*plat.level
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
        if (plat.action == self.attack):
            if plat.action == 'attack':
                plat.dmg = plat.atk +1
                plat.res = 1
                self.dmg = self.atk +1
                self.res = 1
            elif plat.action == 'defense':
                plat.dmg = plat.atk -1
                plat.res = -1
                self.dmg = self.atk -1
                self.res = -1
            elif plat.action == 'magic':
                plat.dmg = plat.atk
                plat.res = 0
                self.dmg = self.atk
                self.res = 0
        #if they are different - by player
        elif (plat.action == 'attack'):
            plat.dmg = plat.atk +1
            plat.res = +1
            if (self.attack == 'defense'):
                self.dmg = self.atk -1
                self.res = -1
            elif (self.attack == 'magic'):
                self.dmg = self.atk
                self.res = 0
        elif (plat.action == 'defense'):
            plat.dmg = plat.atk -1
            plat.res = -1
            if (self.attack == 'attack'):
                self.dmg = self.atk +1
                self.res = +1
            elif (self.attack == 'magic'):
                self.dmg = self.atk
                self.res = 0
        elif (plat.action == 'magic'):
            plat.dmg = plat.atk
            plat.res = 0
            if (self.attack == 'attack'):
                self.dmg = self.atk +1
                self.res = +1
            elif (self.attack == 'defense'):
                self.dmg = self.atk -1
                self.res = -1
            

#add this to start of combat so that they will reset
enemy = Enemy('goblin', 'no')

def combat(enemy_type, boss, posi): #, mob_size to add if necessary
    #generating enemy
    #generating each single attack
    #defining enemy attack and player attack
    if enemy_type == 'goblin':
       enemy.gob_ATK()
    elif enemy_type == 'gnome':
       enemy.gno_ATK()
    elif enemy_type == 'slime':
       enemy.sli_ATK()

    #calculate damage, place damage
    enemy.rps(plat.pattack(posi))
    enemy.hp = enemy.hp - (plat.dmg + enemy.res)
    plat.hp = plat.hp - (enemy.dmg + plat.res)
    health = [plat.hp, enemy.hp]
    return health
