import pygame
import os
import stats

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'sprites')
sound_path = os.path.join(current_path, 'sounds')

pygame.init()

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

def hallway_run(plat, running):

    plat.lastroom = plat.croom
    plat.croom = "hallway"
    #this is the walk screen for the random hallway

    current_path = os.path.dirname(__file__)
    image_path = os.path.join(current_path, 'sprites')
    sound_path = os.path.join(current_path, 'sounds')

    pygame.init()

    #setting screen size
    screen = pygame.display.set_mode((1280,720))

    #setting scenery and static objects
    background = pygame.image.load(os.path.join(image_path, "hallway.jpg"))
    screen.blit(background, (0,0))

    music = pygame.mixer.music.load(os.path.join(sound_path, "walk.wav"))

    all_sprites = pygame.sprite.Group()
    cenario = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()

    plat.player = Player_s()
    enemy = Enemy_s()

    all_sprites.add(plat.player)
    player_group.add(plat.player)

    if plat.enemy_hall == 0:
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

    textidoor = font.render("Press x to enter", True, [0, 0, 0])
    textidoorRect = textidoor.get_rect()
    textidoorRect.center = (700, 50)

    textedoor = font.render("Press x to enter", True, [0, 0, 0])
    textedoorRect = textedoor.get_rect()
    textedoorRect.center = (700, 50)

    attempt = 0
    key_enter = 0
    doors_enter = 0

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
            if plat.player.x <= 150:
                plat.lastroom = plat.croom
                plat.croom = "key"
                running = False
                break
            elif plat.player.x >= 1050:
                plat.lastroom = plat.croom
                plat.croom = "doors"
                running = False
                break

        if keys[pygame.K_UP]:
            attempt = 1

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

        if plat.player.x >= 1100:
            doors_enter = 1
        else:
            doors_enter = 0

        if plat.player.x <= 109:
            key_enter = 1
        else:
            key_enter = 0
    
        if plat.enemy_hall == 0:
            hit_enemy = pygame.sprite.spritecollide(plat.player, enemy_group, True)

            if hit_enemy:
                plat.lastroom = plat.croom
                plat.croom = "combat"
                plat.enemy_hall = 1
                pygame.mixer.music.stop()
                running = False
                break
        
        screen.blit(background, (0,0))
        all_sprites.update()
        enemy.tick -= 1
        all_sprites.draw(screen)
        if attempt == 1:
            screen.blit(textjump, textjumpRect)
        if doors_enter == 1:
            screen.blit(textedoor, textedoorRect)
        if key_enter == 1:
            screen.blit(textidoor, textidoorRect)
        pygame.display.flip()
    
    return plat