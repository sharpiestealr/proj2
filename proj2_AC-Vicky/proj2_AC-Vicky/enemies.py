class Enemy(object): #pygame.sprite no pygame
    """a place to create enemy variables, generate enemies and combats"""
    
    def __init__(self, enemy_type, boss): #generates the enemies
        #chooses the enemy class
        if enemy_type == 'goblin':
            self.hp = 6+2*Player.level
            self.atk = 2+1*Player.level
            self.df = 2+1*Player.level
            self.xp = 5+2*Player.level
        elif enemy_type == 'gnome':
            self.hp = 5+2*Player.level
            self.atk = 2+1*Player.level
            self.df = 3+2*Player.level
            self.xp = 4+2*Player.level
        elif enemy_type == 'slime':
            self.hp = 8+2*Player.level
            self.atk = 2+1*Player.level
            self.df = 2+2*Player.level
            self.xp = 6+2*Player.level
        #checks if enemy has boss factor
        if boss == 'yes':
            self.hp = self.hp*2
            self.atk = self.atk*2
            self.df = self.df*2
            self.xp = self.xp*2
        #combat variables
        self.dmg = 0
        self.res = 0
        self.attack = " "
            

#add this to start of combat so that they will reset
goblin = Enemy('goblin', 'no')
gnome = Enemy('gnome', 'no')
slime = Enemy('slime', 'no')

def combat(enemy_type, boss): #, mob_size to add if necessary
    #generating enemy
    enemy = Enemy(enemy_type, boss)

    #generating each single attack
    while enemy.hp > 0:
        #0, 1: defining enemy attack
        if enemy_type == 'goblin':
            enemy.attack = gob_ATK()
        elif enemy_type == 'gnome':
            enemy.attack = gno_ATK()
        elif enemy_type == 'slime':
            enemy.attack = sli_ATK()
        #steps 2, 3 don't actually exist (yet, may never)
        #4, 5: calculate damage, place damage
        enemy.dmg = rps(enemy)
        #Player.dmg = rps(Player, Player.attack) - in theory, the values for this are being set before as they're public and mutable
        enemy.hp = enemy.hp - (Player.dmg + enemy.res)
        Player.hp = Player.hp - (enemy.dmg + Player.res)
        #steps 6, 7 don't actually exist (yet, may never)
        #steps 8, 9, 10 are redundant because of while-loop
    
    return xp_yield

#methods to define the attack choice of the enemies
def gob_ATK():
    chance = random.randint(0,100)
    if chance <= 0:
        attack_choice = 'magic'
    elif chance <= 30:
        attack_choice = 'defense'
    elif chance <= 70:
        attack_choice = 'attack'
    return attack_choice

def gno_ATK():
    chance = random.randint(0,100)
    if chance <= 15:
        self.attack_choice = 'attack'
    elif chance <= 75:
        self.attack_choice = 'defense'
    elif chance <= 90:
        self.attack_choice = 'magic'
    return attack_choice

def sli_ATK():
    chance = random.randint(0,100)
    if chance <= 15:
        self.attack_choice = 'attack'
    elif chance <= 40:
        self.attack_choice = 'defense'
    elif chance <= 60:
        self.attack_choice = 'magic'
    return attack_choice

#method to determine damage
def rps(enemy):
    #if both are the same
    if (Player.attack == enemy.attack):
        if Player.attack == 'attack':
            Player.dmg = Player.atk +1
            Player.res = -1
            enemy.dmg = enemy.atk +1
            enemy.res = -1
        elif Player.attack == 'defense':
            Player.dmg = Player.atk -1
            Player.res = +1
            enemy.dmg = enemy.atk -1
            enemy.res = +1
        elif Player.attack == 'magic':
            Player.dmg = Player.atk
            Player.res = 0
            enemy.dmg = enemy.atk
            enemy.res = 0
    #if they are different - by player
    elif (Player.attack == 'attack'):
        Player.dmg = Player.atk +1
        Player.res = -1
        if (enemy.attack == 'defense'):
            enemy.dmg = enemy.atk -1
            enemy.res = +1
        elif (enemy.attack == 'magic'):
            enemy.dmg = enemy.atk
            enemy.res = 0
    elif (Player.attack == 'defense'):
        Player.dmg = Player.atk -1
        Player.res = +1
        if (enemy.attack == 'attack'):
            enemy.dmg = enemy.atk +1
            enemy.res = -1
        elif (enemy.attack == 'magic'):
            enemy.dmg = enemy.atk
            enemy.res = 0
    elif (Player.attack == 'magic'):
        Player.dmg = Player.atk
        Player.res = 0
        if (enemy.attack == 'attack'):
            enemy.dmg = enemy.atk +1
            enemy.res = -1
        elif (enemy.attack == 'defense'):
            enemy.dmg = enemy.atk -1
            enemy.res = +1
