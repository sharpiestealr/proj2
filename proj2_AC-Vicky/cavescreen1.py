import pygame
import os
import stats

#importing paths
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'sprites')
sound_path = os.path.join(current_path, 'sounds')
running = False

pygame.init()

#determining sprite classes
class Ledge(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(image_path, "ledge.png"))
        self.rect = self.image.get_rect()        
    def update(self):
        self.rect.x = 442
        self.rect.y = 368

class Hill(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(image_path, "hill.png"))
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.x = 974
        self.rect.y = 210

class EDoor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(image_path, "door.png"))
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.x = 1230
        self.rect.y = 605-self.image.get_height()

class Player_s(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(image_path, "man still.png"))
        self.rect = self.image.get_rect()
        self.x = 100
        self.y = 605 - self.image.get_height()
        self.step_x = 30 #movement on the x axis
        self.step_y = 235 #movement on the y axis
        self.isJump = False #to check if player is jumping
        self.isFall = False #to check if player is falling
        self.jumpCount = 11 #duration of jump
        self.locat = 1 # location of player; key: 1 = ground; 2 = ledge; 3 = hill
        self.left = False #what side is the player facing
        self.haveflip = 1 #has the sprite flipped yet?
    def update(self):
        if self.haveflip == 0: #sprite hasn't been flipped
            self.image = pygame.transform.flip(self.image, True, False) #flip the sprite
            self.haveflip = 1 #it has been flipped
        self.rect.x = self.x
        self.rect.y = self.y

class Enemy_s(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(image_path, "overworld.png"))
        self.step = 20 #movement on the x axis
        self.right = True #what side it has moved to
        self.tick = 5 #amount of times it can move to one side at a time
        self.x = 740
        self.y = 605 - self.image.get_height()
        self.rect = self.image.get_rect()
    def update(self):
        if self.right == True: #automatic movement
            if self.tick > 0:
                self.x = self.x + self.step
            else:
                self.right = False #after 5 ticks, change side and reset tick
                self.tick = 5
        else:
            if self.tick > 0:
                self.x = self.x - self.step
            else:
                self.right = True
                self.tick = 5
        self.rect.x = self.x
        self.rect.y = 605-self.image.get_height()

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(image_path, "coin.png"))
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.x = 514
        self.rect.y = 243

#main game loop
def cave_run(plat, running):
    
    plat.player = Player_s()

    plat.lastroom = plat.croom
    plat.croom = "cave"
    #this is the walk screen for THE FIRST CAVE BEFORE THE PUZZLE

    #setting screen size
    screen = pygame.display.set_mode((1280,720))

    #setting scenery and static objects
    background = pygame.image.load(os.path.join(image_path, "walk.jpg"))
    screen.blit(background, (0,0))

    #importing sounds and music
    coin_sound = pygame.mixer.Sound(os.path.join(sound_path, "coin_collect.wav"))
    door_sound = pygame.mixer.Sound(os.path.join(sound_path, "close_door_1.wav"))
    music = pygame.mixer.music.load(os.path.join(sound_path, "walk.wav"))

    #creating sprite groups
    all_sprites = pygame.sprite.Group()
    cenario_l = pygame.sprite.Group()
    cenario_h = pygame.sprite.Group()
    cenario = pygame.sprite.Group()
    item = pygame.sprite.Group()
    plat.player_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()

    ledge = Ledge()
    hill = Hill()
    edoor = EDoor()
    enemy = Enemy_s()
    coin = Coin()

    all_sprites.add(ledge)
    all_sprites.add(hill)
    all_sprites.add(edoor)
    all_sprites.add(plat.player)
    cenario_l.add(ledge)
    cenario_h.add(hill)
    cenario.add(edoor)
    if plat.coin_cave == 0: #only one coin in the cave per game, avoid respawn
        all_sprites.add(coin)
        item.add(coin)
    plat.player_group.add(plat.player) 
    if plat.enemy_cave == 0: #only one enemy in the cave per game, avoid respawn
        all_sprites.add(enemy)
        enemy_group.add(enemy)

    #update screen
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    pygame.mixer.music.play(-1)

    #messages
    font = pygame.font.Font('freesansbold.ttf', 36)
    #Error message when trying to jump on ledge
    textjump = font.render("You can't jump here", True, [0, 0, 0])
    textjumpRect = textjump.get_rect()
    textjumpRect.center = (300, 100)

    #interact prompt to enter chest room
    textchest = font.render("Press x to enter", True, [0, 0, 0])
    textchestRect = textchest.get_rect()
    textchestRect.center = (700, 50)

    #Error message if player tries to enter chest room twice
    textnochest = font.render("The room has caved in", True, [0, 0, 0])
    textnochestRect = textnochest.get_rect()
    textnochestRect.center = (700, 100)

    #interact prompt to enter key room
    textdoor = font.render("Press x to enter", True, [0, 0, 0])
    textdoorRect = textdoor.get_rect()
    textdoorRect.center = (700, 50)

    #variables to determine the messages
    attempt = 0
    chest_enter = 0
    key_enter = 0
    nochest_enter = 0
    
    while running:
        pygame.time.delay(100) #smooth movement of player

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                plat.stop = 1 
                running = False
                break
    
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            plat.stop = 1
            running = False
            break
 
        if keys[pygame.K_x]:
            if chest_enter == 1 and plat.chest1 == 0: #if player interacts with chest for the first time
                pygame.mixer.Sound.play(door_sound) #play sound
                pygame.mixer.music.stop()
                plat.lastroom = plat.croom #set last room (needed to exit combat)
                plat.croom = "chest1" #set current room
                running = False #leave cave
                break
            elif chest_enter == 1 and plat.chest1 == 1: #if player interacts with chest for the second time
                nochest_enter = 1
            elif key_enter == 1: #if player interacts with the door to key room
                pygame.mixer.Sound.play(door_sound) #play sound
                pygame.mixer.music.stop()
                plat.lastroom = plat.croom #set last room
                plat.croom = "key" #set current room
                running = False
                break

        if not(plat.player.isJump): #variable to determine jumping
            if keys[pygame.K_UP] and plat.player.locat < 3: #if player tries to jump and is not on hill, let jump
                plat.player.isJump = True
            elif keys[pygame.K_UP] and plat.player.locat == 3 : # if player on ledge and tries to jump, error message
                attempt = 1
        else:
            if plat.player.locat !=3: #if not on hill
                if plat.player.jumpCount >= -11:
                   plat.player.y -= (plat.player.jumpCount * abs(plat.player.jumpCount)) * 0.5 #simulation of a parabola to jump
                   plat.player.jumpCount -= 1 #11 ticks up and 11 ticks down
                else: # This will execute if our jump is finished
                   plat.player.jumpCount = 11
                   plat.player.isJump = False
                   # Resetting our Variables
            else:
                if plat.player.jumpCount >= -50 or plat.player.isFall == True: #if on hill and falling
                    plat.player.y -= (plat.player.jumpCount * abs(plat.player.jumpCount)) * 0.5 #complete parabola till floor
                    plat.player.jumpCount -= 1
                    if plat.player.y > 605-plat.player.image.get_height(): #when reach floor or if pass floor
                        plat.player.locat = 1 #set location to floor
                        plat.player.y = 605-plat.player.image.get_height() #set position on floor
                        plat.player.jumpCount = 11
                        plat.player.isJump = False
                        plat.player.isFall = False
                        # Resetting our Variables

        if keys[pygame.K_RIGHT] and plat.player.x < 1150: #moving right within boundaries
            if plat.player.left == True: #if facing left
                plat.player.left = False #facing right
                plat.player.haveflip = 0 #need to flip
                plat.player.x = plat.player.x + plat.player.step_x #move
            else:
                plat.player.x = plat.player.x + plat.player.step_x
       
        if keys[pygame.K_LEFT] and plat.player.x > 100: #moving left within boundaries
            if plat.player.left == False: #same idea as above, but moving left
                plat.player.left = True
                plat.player.haveflip = 0
                plat.player.x = plat.player.x - plat.player.step_x
            else:
                plat.player.x = plat.player.x - plat.player.step_x

        hit_ledge = pygame.sprite.spritecollide(plat.player, cenario_l, False) #check for collision with ledge

        if plat.player.locat == 1: 
            if plat.player.isJump and hit_ledge: #if jumping from floor to ledge
                plat.player.rect.y = ledge.rect.y + plat.player.image.get_height() #place player on ledge
                plat.player.isJump = False #reset variables to interrupt jump
                plat.player.isFall = False
                jump_temp = plat.player.jumpCount #necessary to complete fall of ledge
                plat.player.jumpCount = 11 #reset
                plat.player.locat = 2 #set new location
        elif plat.player.locat == 2: #on ledge
            if plat.player.isJump: #jumping from ledge
                hit_hill = pygame.sprite.spritecollide(plat.player, cenario_h, False) #can only jump from ledge to hill
                if hit_hill:
                    plat.player.rect.y = hill.rect.y + plat.player.image.get_height() #update position
                    plat.player.locat = 3
                    plat.player.isJump = False #reset jump
                    plat.player.jumpCount = 0 #can't jump from ledge, so only down part of parabola needed to fall
                    chest_enter = 1 #interact message
            elif not(hit_ledge): #leave ledge, fall to floor based on what was left of inicial jump to ledge
                plat.player.locat = 1
                plat.player.isJump = True
                plat.player.jumpCount = jump_temp
    
        hit_hill = pygame.sprite.spritecollide(plat.player, cenario_h, False)

        if plat.player.x < 974 and plat.player.locat == 3: #if not on hill, fall and reset variables
            plat.player.isFall = True
            plat.player.isJump = True
            attempt = 0
            chest_enter = 0

        if plat.player.x >= 1050 and plat.player.locat == 1: #condition to enter key room
            key_enter = 1
        else:
            key_enter = 0

        if plat.coin_cave == 0: #spawn coin; only one cave coin per game
            hit_coin = pygame.sprite.spritecollide(plat.player, item, True)

            if hit_coin: #collect coin and activate key
                pygame.mixer.Sound.play(coin_sound)
                #pygame.mixer.music.stop()
                plat.coins += 1
                plat.coin_cave = 1

        if plat.enemy_cave == 0: #only one cave enemy per game
            hit_enemy = pygame.sprite.spritecollide(plat.player, enemy_group, True)

            if hit_enemy:
                if plat.player.locat != 1: #if falling on enemy, set player position to floor
                    plat.player.rect.y = 605-plat.player.image.get_height()
                    if plat.player.locat == 2:
                        plat.player.locat = 1
                if (plat.player.locat == 1): #call combat
                    plat.lastroom = plat.croom
                    plat.croom = "combat"
                    plat.enemy_cave = 1
                    running = False
                    break
                pygame.mixer.Sound.play(coin_sound)
                pygame.mixer.music.stop()
        
        #update screen and display messages from keys
        screen.blit(background, (0,0))
        all_sprites.update()
        enemy.tick -= 1
        all_sprites.draw(screen)
        if attempt == 1:
            screen.blit(textjump, textjumpRect)
        if chest_enter == 1 and plat.chest1 == 0:
            screen.blit(textchest, textchestRect)
        if nochest_enter == 1 and plat.chest1 == 1:
            screen.blit(textnochest, textnochestRect)
        if key_enter == 1:
            screen.blit(textdoor, textdoorRect)
        pygame.display.flip()

    return plat