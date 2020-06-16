import pygame
import os
import stats

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'sprites')
sound_path = os.path.join(current_path, 'sounds')
running = False

pygame.init()

class LLedge(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(image_path, "long.png"))
        self.rect = self.image.get_rect()        
    def update(self):
        self.rect.x = 522
        self.rect.y = 410

class TLedge(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(image_path, "ledge.png"))
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.x = 150
        self.rect.y = 200

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
        self.y = 600-self.image.get_height()
        self.step_x = 30
        self.step_y = 150
        self.isJump = False
        self.isFall = False
        self.jumpCount = 11
        self.locat = 1 # 1 = ground; 2 = LLedge; 3 = TLedge
        self.left = False
        self.haveflip = 1
    def update(self):
        if self.haveflip == 0:
            self.image = pygame.transform.flip(self.image, True, False)
            self.haveflip = 1
        self.rect.x = self.x
        self.rect.y = self.y

class Enemy_s(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(image_path, "overworld.png"))
        self.step = 20
        self.right = True
        self.tick = 5
        self.x = 1000
        self.y = 600-self.image.get_height()
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
        self.rect.y = 600-self.image.get_height()

class Key(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(image_path, "key.png"))
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.x = 240
        self.rect.y = 134

def key_run(plat, running):
    plat.croom = "key"
    #this is the walk screen for the key room

    #setting screen size
    screen = pygame.display.set_mode((1280,720))

    #setting scenery and static objects
    background = pygame.image.load(os.path.join(image_path, "keybg.jpg"))
    screen.blit(background, (0,0))

    #importing sounds and music
    coin_sound = pygame.mixer.Sound(os.path.join(sound_path, "coin_collect.wav"))
    door_sound = pygame.mixer.Sound(os.path.join(sound_path, "close_door_1.wav"))
    key_sound = pygame.mixer.Sound(os.path.join(sound_path, "key_collect.wav"))
    music = pygame.mixer.music.load(os.path.join(sound_path, "walk.wav"))

    all_sprites = pygame.sprite.Group()
    cenario_t = pygame.sprite.Group()
    cenario_l = pygame.sprite.Group()
    cenario = pygame.sprite.Group()
    item = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()

    lledge = LLedge()
    tledge = TLedge()
    edoor = EDoor()
    plat.player = Player_s()
    enemy = Enemy_s()
    key = Key()

    all_sprites.add(lledge)
    all_sprites.add(tledge)
    all_sprites.add(edoor)
    all_sprites.add(plat.player)
    cenario_l.add(lledge)
    cenario_t.add(tledge)
    cenario.add(edoor)
    if plat.key_check == 0:
        all_sprites.add(key)
        item.add(key)
    player_group.add(plat.player)
    if plat.enemy_key == 0:
        all_sprites.add(enemy)
        enemy_group.add(enemy)

    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    pygame.mixer.music.play()

    font = pygame.font.Font('freesansbold.ttf', 36)
    textjump = font.render("You can't jump here", True, [0, 0, 0])
    textjumpRect = textjump.get_rect()
    textjumpRect.center = (700, 100)

    textcave = font.render("Press x to enter", True, [0, 0, 0])
    textcaveRect = textcave.get_rect()
    textcaveRect.center = (700, 50)

    texthallway = font.render("Press x to enter", True, [0, 0, 0])
    texthallwayRect = texthallway.get_rect()
    texthallwayRect.center = (700, 50)

    attempt = 0
    cave_enter = 0
    hallway_enter = 0
    
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
 
        if keys[pygame.K_x] and plat.player.locat == 1:
            if plat.player.x <= 150:
                pygame.mixer.Sound.play(door_sound)
                pygame.mixer.music.stop()
                plat.lastroom = plat.croom
                plat.croom = "cave"
                running = False
                break
            elif plat.player.x >= 1050:
                pygame.mixer.Sound.play(door_sound)
                pygame.mixer.music.stop()
                plat.lastroom = plat.croom
                plat.croom = "hallway"
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
                    if plat.player.y > 600-plat.player.image.get_height():
                        plat.player.locat = 1
                        plat.player.y = 600-plat.player.image.get_height()
                        plat.player.jumpCount = 11
                        plat.player.isJump = False
                        plat.player.isFall = False

        if keys[pygame.K_RIGHT] and plat.player.x < 1150:
            if plat.player.left == True:
                plat.player.left = False
                plat.player.haveflip = 0
                plat.player.x = plat.player.x + plat.player.step_x
            else:
                plat.player.x = plat.player.x + plat.player.step_x       
        if keys[pygame.K_LEFT] and plat.player.x > 50:
            if plat.player.left == False:
                plat.player.left = True
                plat.player.haveflip = 0
                plat.player.x = plat.player.x - plat.player.step_x
            else:
                plat.player.x = plat.player.x - plat.player.step_x
        hit_lledge = pygame.sprite.spritecollide(plat.player, cenario_l, False)

        if plat.player.locat == 1:
            if plat.player.isJump and hit_lledge:
                plat.player.rect.y = lledge.rect.y + plat.player.image.get_height()
                plat.player.isJump = False
                plat.player.isFall = False
                jump_temp = plat.player.jumpCount
                plat.player.jumpCount = 11
                plat.player.locat = 2
        elif plat.player.locat == 2:
            if plat.player.isJump:
                hit_tledge = pygame.sprite.spritecollide(plat.player, cenario_t, False)
                if hit_tledge:
                    plat.player.rect.y = tledge.rect.y + plat.player.image.get_height()
                    plat.player.locat = 3
                    plat.player.isJump = False
                    plat.player.jumpCount = 0
                    chest_enter = 1
            elif not(hit_lledge):
                plat.player.locat = 1
                plat.player.isJump = True
                plat.player.jumpCount = jump_temp
    
        hit_tledge = pygame.sprite.spritecollide(plat.player, cenario_t, False)

        if plat.player.locat == 3:
            if plat.player.x < tledge.rect.x or plat.player.x > tledge.rect.x + tledge.image.get_width():
                plat.player.isFall = True
                plat.player.isJump = True
                attempt = 0

        if plat.player.x >= 1050 and plat.player.locat == 1:
            hallway_enter = 1
        else:
            hallway_enter = 0

        if plat.player.x <= 150 and plat.player.locat == 1:
            cave_enter = 1
        else:
            cave_enter = 0

        if plat.key_check == 0:
            hit_key = pygame.sprite.spritecollide(plat.player, item, True)
            if hit_key:
                pygame.mixer.Sound.play(key_sound)
                #pygame.mixer.music.stop()
                plat.key_check = 1
    
        if plat.enemy_key == 0:
            hit_enemy = pygame.sprite.spritecollide(plat.player, enemy_group, True)

            if hit_enemy:
                if plat.player.locat != 1:
                    plat.player.rect.y = 600-player.image.get_height()
                    if plat.player.locat == 2:
                        plat.player.locat = 1
                plat.lastroom = plat.croom
                plat.croom = "combat"
                plat.enemy_key = 1
                break
                pygame.mixer.Sound.play(coin_sound)
                pygame.mixer.music.stop()
        
        screen.blit(background, (0,0))
        all_sprites.update()
        enemy.tick -= 1
        all_sprites.draw(screen)
        if attempt == 1:
            screen.blit(textjump, textjumpRect)
        if hallway_enter == 1:
            screen.blit(texthallway, texthallwayRect)
        if cave_enter == 1:
            screen.blit(textcave, textcaveRect)
        pygame.display.flip()

    return plat