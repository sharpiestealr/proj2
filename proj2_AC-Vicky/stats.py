class Player:
    """a place to keep player info"""
    #player stats
    level = 1
    xp = 0
    croom = "opening" #used to control the boss factor
    lastroom = ""
    coins = 0
    key_check = 0 #key check
    potion = 0 #potion inventory
    solved = 0 #check if puzzle is solved
    coin_cave = 0 #check if collect cave coin
    chest = 0 #check if done cave

    def __init__(self):
        #self.name = input("What's your name, adventurer? ")  
        self.hp = 10+2*self.level
        self.atk = 3+1*self.level
        self.df = 3+1*self.level
        self.threshold = 10*self.level

        #combat variables
        self.dmg = 0
        self.res = 0
        self.result = 0        
    
    def pattack(self, posi):
        if posi == 1:
            self.action = "attack"
        elif posi == 2:
            self.action = "defense"
        else:
            self.action = "magic"

    #check lvl up post combat
    def lvl_up(self):
        if self.xp >= self.threshold:
            self.xp = self.xp - self.threshold
            self.level = self.level + 1
            self.threshold = self.threshold*2
            print("Congratulations! You leveled up!")