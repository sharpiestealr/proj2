import pygame
import os
import stats

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'sprites')
sound_path = os.path.join(current_path, 'sounds')
running = False

pygame.init()

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
        self.step_x = 30
        self.step_y = 235
        self.isJump = False
        self.isFall = False
        self.jumpCount = 11
        self.locat = 1 # 1 = ground; 2 = ledge; 3 = hill
    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

class Enemy_s(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(image_path, "overworld.png"))
        self.step = 20
        self.right = True
        self.tick = 5
        self.x = 740
        self.y = 605 - self.image.get_height()
        self.rect = self.image.get_rect()
    def update(self):
        if self.right == True:
            if self.tick > 0:
                self.x = self.x + self.step
            else:
                self.right = False
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
    music = pygame.mixer.Sound(os.path.join(sound_path, "walk.wav"))

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
    if plat.coin_cave == 0:
        all_sprites.add(coin)
        item.add(coin)
    plat.player_group.add(plat.player)
    if plat.enemy_cave == 0:
        all_sprites.add(enemy)
        enemy_group.add(enemy)

    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()

    font = pygame.font.Font('freesansbold.ttf', 36)
    textjump = font.render("You can't jump here", True, [0, 0, 0])
    textjumpRect = textjump.get_rect()
    textjumpRect.center = (700, 100)

    textchest = font.render("Press x to enter", True, [0, 0, 0])
    textchestRect = textchest.get_rect()
    textchestRect.center = (700, 50)

    textnochest = font.render("The room has caved in", True, [0, 0, 0])
    textnochestRect = textnochest.get_rect()
    textnochestRect.center = (700, 50)

    textdoor = font.render("Press x to enter", True, [0, 0, 0])
    textdoorRect = textdoor.get_rect()
    textdoorRect.center = (700, 50)

    attempt = 0
    chest_enter = 0
    key_enter = 0
    nochest_enter = 0
    
    while running:
        pygame.time.delay(100)

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
            if chest_enter == 1 and plat.chest == 0:
                pygame.mixer.Sound.play(door_sound)
                pygame.mixer.music.stop()
                plat.lastroom = plat.croom
                plat.croom = "chest"
                running = False
                break
            elif chest_enter == 1 and plat.chest == 1:
                nochest_enter = 1
            elif key_enter == 1:
                pygame.mixer.Sound.play(door_sound)
                pygame.mixer.music.stop()
                plat.lastroom = plat.croom
                plat.croom = "key"
                running = False
                break

        if not(plat.player.isJump):
            if keys[pygame.K_UP] and plat.player.locat < 3:
                plat.player.isJump = True
            elif keys[pygame.K_UP] and plat.player.locat == 3 :
                attempt = 1
        else:
            if plat.player.locat !=3:
                if plat.player.jumpCount >= -11:
                   plat.player.y -= (plat.player.jumpCount * abs(plat.player.jumpCount)) * 0.5
                   plat.player.jumpCount -= 1
                else: # This will execute if our jump is finished
                   plat.player.jumpCount = 11
                   plat.player.isJump = False
                   # Resetting our Variables
            else:
                if plat.player.jumpCount >= -50 or plat.player.isFall == True:
                    plat.player.y -= (plat.player.jumpCount * abs(plat.player.jumpCount)) * 0.5
                    plat.player.jumpCount -= 1
                    if plat.player.y > 605-plat.player.image.get_height():
                        plat.player.locat = 1
                        plat.player.y = 605-plat.player.image.get_height()
                        plat.player.jumpCount = 11
                        plat.player.isJump = False
                        plat.player.isFall = False

        if keys[pygame.K_RIGHT] and plat.player.x < 1150:
            plat.player.x = plat.player.x + plat.player.step_x
       
        if keys[pygame.K_LEFT] and plat.player.x > 100:
           plat.player.x = plat.player.x - plat.player.step_x

        hit_ledge = pygame.sprite.spritecollide(plat.player, cenario_l, False)

        if plat.player.locat == 1:
            if plat.player.isJump and hit_ledge:
                plat.player.rect.y = ledge.rect.y + plat.player.image.get_height()
                plat.player.isJump = False
                plat.player.isFall = False
                jump_temp = plat.player.jumpCount
                plat.player.jumpCount = 11
                plat.player.locat = 2
        elif plat.player.locat == 2:
            if plat.player.isJump:
                hit_hill = pygame.sprite.spritecollide(plat.player, cenario_h, False)
                if hit_hill:
                    plat.player.rect.y = hill.rect.y + plat.player.image.get_height()
                    plat.player.locat = 3
                    plat.player.isJump = False
                    plat.player.jumpCount = 0
                    chest_enter = 1
            elif not(hit_ledge):
                plat.player.locat = 1
                plat.player.isJump = True
                plat.player.jumpCount = jump_temp
    
        hit_hill = pygame.sprite.spritecollide(plat.player, cenario_h, False)

        if plat.player.x < 974 and plat.player.locat == 3:
            plat.player.isFall = True
            plat.player.isJump = True
            attempt = 0
            chest_enter = 0

        if plat.player.x >= 1050 and plat.player.locat == 1:
            key_enter = 1
        else:
            key_enter = 0

        if plat.coin_cave == 0:
            hit_coin = pygame.sprite.spritecollide(plat.player, item, True)

            if hit_coin:
                pygame.mixer.Sound.play(coin_sound)
                pygame.mixer.music.stop()
                plat.coins += 1
                plat.coin_cave = 1

        if plat.enemy_cave == 0:
            hit_enemy = pygame.sprite.spritecollide(plat.player, enemy_group, True)

            if hit_enemy:
                if plat.player.locat != 1:
                    plat.player.rect.y = 605-plat.player.image.get_height()
                    if plat.player.locat == 2:
                        plat.player.locat = 1
                if (plat.player.locat == 1):
                    plat.lastroom = plat.croom
                    plat.croom = "combat"
                    plat.enemy_cave = 1
                    running = False
                    break
                pygame.mixer.Sound.play(coin_sound)
                pygame.mixer.music.stop()
        
        screen.blit(background, (0,0))
        all_sprites.update()
        enemy.tick -= 1
        all_sprites.draw(screen)
        if attempt == 1:
            screen.blit(textjump, textjumpRect)
        if chest_enter == 1 and plat.chest == 0:
            screen.blit(textchest, textchestRect)
        if nochest_enter == 1 and plat.chest == 1:
            screen.blit(textnochest, textnochestRect)
        if key_enter == 1:
            screen.blit(textdoor, textdoorRect)
        pygame.display.flip()

    return plat