class Player:
    """a place to keep player info"""
    #player stats
    croom = "opening" #used to control the boss factor
    lastroom = ""
    coins = 0
    key_check = 0 #key check
    potion = 0 #potion inventory
    solved = 0 #check if puzzle is solved
    coin_cave = 0 #check if collect cave coin
    enemy_cave = 0
    enemy_hall = 0
    enemy_door = 0
    enemy_key = 0
    chest = 0 #check if done cave
    chest1 = 0 #alt chest
    chest2 = 0 #auto combat
    x = 0
    y = 0
    step_x = 0
    step_y = 0
    isJump = False
    isFall = False
    jumpCount = 0
    locat = 0
    left = False
    haveflip = 0
    hp = 12
    atk = 4
    df = 4
    dmg = 0
    res = 0
    player = [x, y, step_x, step_y, isJump, isFall, jumpCount, locat]
    player_last = [x, y, step_x, step_y, isJump, isFall, jumpCount, locat, left, haveflip]
    player_combat = [hp, atk, df, dmg, res]
    stop = 0  