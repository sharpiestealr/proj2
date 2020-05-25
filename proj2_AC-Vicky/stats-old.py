
class Player:
    """a place to keep player info"""
        #player stats
    
    def __init__(self):
        self.name = input("What's your name, adventurer? ")  
        self.level = 1
        self.hp = 10+2*self.level
        self.atk = 3+1*self.level
        self.df = 3+1*self.level
        self.xp = 0
        self.threshold = 10
        self.chapter = 1

        #combat variables
        self.dmg = 0
        self.res = 0
    
    def pattack(self):
        self.action = input("Choose between attack, defense or magic, {0} ".format(self.name))

    #check lvl up post combat
    def lvl_up(self):
        if self.xp >= self.threshold:
            self.xp = self.xp - self.threshold
            self.level = self.level + 1
            self.threshold = self.threshold*2
            print("Congratulations! You leveled up!")
