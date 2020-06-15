import pygame
import os
import stats

plat = stats.Player()
plat.croom = "cave"
#this is the walk screen for THE FIRST CAVE BEFORE THE PUZZLE

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'sprites')
sound_path = os.path.join(current_path, 'sounds')

pygame.init()

#setting screen size
screen = pygame.display.set_mode((1280,720))

#setting scenery and static objects
background = pygame.image.load(os.path.join(image_path, "walk.jpg"))
screen.blit(background, (0,0))

#importing sounds and music
coin_sound = pygame.mixer.Sound(os.path.join(sound_path, "coin_collect.wav"))
door_sound = pygame.mixer.Sound(os.path.join(sound_path, "close_door_1.wav"))

all_sprites = pygame.sprite.Group()
cenario_l = pygame.sprite.Group()
cenario_h = pygame.sprite.Group()
cenario = pygame.sprite.Group()
item = pygame.sprite.Group()
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

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
        self.image = pygame.image.load(os.path.join(image_path, "player.png"))
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
        self.image = pygame.image.load(os.path.join(image_path, "slime mockup.png"))
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

ledge = Ledge()
hill = Hill()
edoor = EDoor()
player = Player_s()
enemy = Enemy_s()
coin = Coin()

all_sprites.add(ledge)
all_sprites.add(hill)
all_sprites.add(edoor)
all_sprites.add(player)
all_sprites.add(enemy)
all_sprites.add(coin)
cenario_l.add(ledge)
cenario_h.add(hill)
cenario.add(edoor)
if plat.coin_cave == 0:
    item.add(coin)
player_group.add(player)
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

textdoor = font.render("Press x to enter", True, [0, 0, 0])
textdoorRect = textdoor.get_rect()
textdoorRect.center = (700, 50)

attempt = 0
chest_enter = 0
key_enter = 0
    
running = True

while running:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        running = False
        break
 
    if keys[pygame.K_x]:
        if chest_enter == 1:
            pygame.mixer.Sound.play(door_sound)
            pygame.mixer.music.stop()
            import chestscreen1
            running = False
            break
        elif key_enter == 1:
            pygame.mixer.Sound.play(door_sound)
            pygame.mixer.music.stop()
            import keyscreen1
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
                if player.y > 605-player.image.get_height():
                    player.locat = 1
                    player.y = 605-player.image.get_height()
                    player.jumpCount = 11
                    player.isJump = False
                    player.isFall = False

    if keys[pygame.K_RIGHT] and player.x < 1150:
        player.x = player.x + player.step_x
       
    if keys[pygame.K_LEFT] and player.x > 100:
       player.x = player.x - player.step_x

    hit_ledge = pygame.sprite.spritecollide(player, cenario_l, False)

    if player.locat == 1:
        if player.isJump and hit_ledge:
            player.rect.y = ledge.rect.y + player.image.get_height()
            player.isJump = False
            player.isFall = False
            jump_temp = player.jumpCount
            player.jumpCount = 11
            player.locat = 2
    elif player.locat == 2:
        if player.isJump:
            hit_hill = pygame.sprite.spritecollide(player, cenario_h, False)
            if hit_hill:
                player.rect.y = hill.rect.y + player.image.get_height()
                player.locat = 3
                player.isJump = False
                player.jumpCount = 0
                chest_enter = 1
        elif not(hit_ledge):
            player.locat = 1
            player.isJump = True
            player.jumpCount = jump_temp
    
    hit_hill = pygame.sprite.spritecollide(player, cenario_h, False)

    if player.x < 974 and player.locat == 3:
        player.isFall = True
        player.isJump = True
        attempt = 0
        chest_enter = 0

    if player.x >= 1050 and player.locat == 1:
        key_enter = 1
    else:
        key_enter = 0

    if plat.coin_cave == 0:
        hit_coin = pygame.sprite.spritecollide(player, item, True)

        if hit_coin:
            pygame.mixer.Sound.play(coin_sound)
            pygame.mixer.music.stop()
            plat.coins += 1
            plat.coin_cave = 1
    
    hit_enemy = pygame.sprite.spritecollide(player, enemy_group, True)

    if hit_enemy:
        if player.locat != 1:
            player.rect.y = 605-player.image.get_height()
            if player.locat == 2:
                player.locat = 1
        import combat
        pygame.mixer.Sound.play(coin_sound)
        pygame.mixer.music.stop()
        
    screen.blit(background, (0,0))
    all_sprites.update()
    enemy.tick -= 1
    all_sprites.draw(screen)
    if attempt == 1:
        screen.blit(textjump, textjumpRect)
    if chest_enter == 1:
        screen.blit(textchest, textchestRect)
    if key_enter == 1:
        screen.blit(textdoor, textdoorRect)
    pygame.display.flip()