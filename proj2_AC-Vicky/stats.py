class Player(object):
    """a place to keep player info"""
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

jogador = Player()

#player choice, going to be buttons in final version. Using input as a preliminary version
Player.attack = input("Choose between attack, defense or magic, {0}".format(jogador.name))

#check lvl up post combat
def lvl_up(jogador):
    if jogador.xp >= jogador.threshold:
        jogador.xp = jogador.xp - jogador.threshold
        jogador.level = jogador.level + 1
        jogador.threshold = jogador.threshold*2