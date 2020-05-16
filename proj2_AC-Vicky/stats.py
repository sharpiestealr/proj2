class Player(object):
    """a place to keep global vars + control vars"""
        #player stats
    def name():
        self.name = input("What's your name, adventurer? ")  
    self.hp = 10+2*Player.level
    self.atk = 3+1*Player.level
    self.df = 3+1*Player.level
    self.xp = 0
    self.threshold = 10
    self.level = 1
    self.chapter = 1
      
    #combat variables
    self.dmg = 0
    self.res = 0
    self.attack = " "

#player choice, going to be buttons in final version. Using input as a preliminary version
Player.attack = input("attack, defense or magic")

#check lvl up post combat
def lvl_up(Player.xp, Player.threshold, Player.level):
    if Player.xp >= Player.threshold:
        Player.xp = Player.xp - Player.threshold
        Player.level = Player.level + 1
        Player.threshold = Player.threshold*2