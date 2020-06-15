import pygame
import os
import stats

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
        self.locat = 1 # 1 = ground
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

class IDoor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.xmax = 110
        self.y = 338
        self.ymax = 622
        self.rect = pygame.rect(self.x, self.y, self.xmax-self.x, self.ymax-self.y)

class EDoor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 1233
        self.xmax = 1280
        self.y = 320
        self.ymax = 622
        self.rect = pygame.rect(self.x, self.y, self.xmax-x, self.ymax-y)

def hallway_assets(plat):
    plat.lastroom = plat.croom
    plat.croom = "hallway"
    #this is the walk screen for the random hallway

    current_path = os.path.dirname(__file__)
    image_path = os.path.join(current_path, 'sprites')

    pygame.init()

    #setting screen size
    screen = pygame.display.set_mode((1280,720))

    #setting scenery and static objects
    background = pygame.image.load(os.path.join(image_path, "hallway.jpg"))
    screen.blit(background, (0,0))

    music = pygame.mixer.Sound(os.path.join(sound_path, "walk.wav"))

    all_sprites = pygame.sprite.Group()
    cenario = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()

    idoor = IDoor()
    edoor = EDoor()
    player = Player_s()
    enemy = Enemy_s()
    key = Key()

    all_sprites.add(edoor)
    all_sprites.add(player)
    all_sprites.add(enemy)
    all_sprites.add(idoor)
    cenario.add(edoor)
    cenario.add(idoor)
    player_group.add(player)
    enemy_group.add(enemy)

    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()

    font = pygame.font.Font('freesansbold.ttf', 36)
    textjump = font.render("You can't jump here", True, [0, 0, 0])
    textjumpRect = textjump.get_rect()
    textjumpRect.center = (700, 100)

    textidoor = font.render("Press x to enter", True, [0, 0, 0])
    textidoor = textcave.get_rect()
    textidoor.center = (700, 50)

    textedoor = font.render("Press x to enter", True, [0, 0, 0])
    textedoorRect = texthallway.get_rect()
    textedoorRect.center = (700, 50)

    attempt = 0
    key_enter = 0
    doors_enter = 0
    
    return plat

def hallway_run(plat):
    while running:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
    
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            running = False
            break
 
        if keys[pygame.K_x] and player.locat == 1:
            if player.x <= 150:
                plat.lastroom = plat.croom
                plat.croom = "key"
                running = False
                break
            elif player.x >= 1050:
                plat.lastroom = plat.croom
                plat.croom = "door"
                running = False
                break

        if not(player.isJump):
            if keys[pygame.K_UP] and player.locat < 3:
                player.isJump = True
            elif keys[pygame.K_UP] and player.locat == 3 :
                attempt = 1
        else:
            if player.locat !=3:
                if player.jumpCount >= -11:
                   player.y -= (player.jumpCount * abs(player.jumpCount)) * 0.5
                   player.jumpCount -= 1
                else: # This will execute if our jump is finished
                   player.jumpCount = 11
                   player.isJump = False
                   # Resetting our Variables
            else:
                if player.jumpCount >= -50 or player.isFall == True:
                    player.y -= (player.jumpCount * abs(player.jumpCount)) * 0.5
                    player.jumpCount -= 1
                    if player.y > 600-player.image.get_height():
                        player.locat = 1
                        player.y = 600-player.image.get_height()
                        player.jumpCount = 11
                        player.isJump = False
                        player.isFall = False

        if keys[pygame.K_RIGHT] and player.x < 1150:
            player.x = player.x + player.step_x
       
        if keys[pygame.K_LEFT] and player.x > 50:
           player.x = player.x - player.step_x

        if player.locat == 1:
            if player.isJump:
                player.rect.y = player.image.get_height() + player.step_y
                player.isJump = False
                player.isFall = False
                jump_temp = player.jumpCount
                player.jumpCount = 11
                player.locat = 2
        elif player.locat == 2:
            if player.isJump:
                if hit_tledge:
                    player.rect.y = player.step_y + player.image.get_height()
                    player.locat = 3
                    player.isJump = False
                    player.jumpCount = 0
                    chest_enter = 1

        if player.x >= 1232 and player.locat == 1:
            doors_enter = 1
        else:
            doors_enter = 0

        if player.x <= 109 and player.locat == 1:
            key_enter = 1
        else:
            key_enter = 0
    
        hit_enemy = pygame.sprite.spritecollide(player, enemy_group, True)

        if hit_enemy:
            if player.locat != 1:
                player.rect.y = 600-player.image.get_height()
                if player.locat == 2:
                    player.locat = 1
            plat.lastroom = plat.croom
            plat.croom = "combat"
            break
        
        screen.blit(background, (0,0))
        all_sprites.update()
        enemy.tick -= 1
        all_sprites.draw(screen)
        if attempt == 1:
            screen.blit(textjump, textjumpRect)
        if door_enter == 1:
            screen.blit(textedoor, textedoorRect)
        if key_enter == 1:
            screen.blit(textidoor, textidoorRect)
        pygame.display.flip()
    
    return plat