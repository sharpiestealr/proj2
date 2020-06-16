class Player:
    """a place to keep player info"""
    #player stats
    croom = "opening" #used to control the boss factor
    lastroom = "" #used for combat
    coins = 0 #collected coins
    key_check = 0 #key check
    potion = 0 #potion inventory
    solved = 0 #check if puzzle is solved
    coin_cave = 0 #check if collect cave coin
    enemy_cave = 0 #check if defeat enemy in cave
    enemy_hall = 0 #check if defeat enemy in hall
    enemy_door = 0 #check if defeat enemy in door
    enemy_key = 0 #check if defeat enemy in key room
    chest = 0 #check if done cave
    chest1 = 0 #alt chest
    chest2 = 0 #auto combat
    end = 0 #end game
    x = 0 
    y = 0 
    step_x = 0 #movement on x axis
    step_y = 0 #movement on y axis
    isJump = False #to check if player is jumping
    isFall = False #to check if player is falling
    jumpCount = 0 #duration of jump
    locat = 0 #player location
    left = False #what side is the player facing
    haveflip = 0 #has the sprite flipped yet?
    hp = 12
    atk = 4
    df = 4
    dmg = 0
    res = 0
    player = [x, y, step_x, step_y, isJump, isFall, jumpCount, locat] #sprite variables
    player_combat = [hp, atk, df, dmg, res] #combat variables
    stop = 0  #controls if game working