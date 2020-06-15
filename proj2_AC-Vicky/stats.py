class Player:
    """a place to keep player info"""
        #player stats
    
    def __init__(self):
        #self.name = input("What's your name, adventurer? ")  
        self.level = 1
        self.hp = 10+2*self.level
        self.atk = 3+1*self.level
        self.df = 3+1*self.level
        self.xp = 0
        self.threshold = 10
        
        #check variables
        self.chapter = 1
        self.croom = "opening" #used to control the boss factor
        self.lastroom = ""
        self.coins = 0
        self.door = 0 #only becomes 1 to enter door, entering new room wipes this
        self.key = 0 #key check
        self.potion = 0 #potion inventory
        self.solved = 0 #check if puzzle is solved

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