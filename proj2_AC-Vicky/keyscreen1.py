import pygame
import os
import stats

plat = stats.Player()
plat.croom = "key"
#this is the walk screen for the key room

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'sprites')

pygame.init()

#setting screen size
screen = pygame.display.set_mode((1280,720))

#setting scenery and static objects
background = pygame.image.load(os.path.join(image_path, "keybg.jpg"))
screen.blit(background, (0,0))

all_sprites = pygame.sprite.Group()
cenario_t = pygame.sprite.Group()
cenario_l = pygame.sprite.Group()
cenario = pygame.sprite.Group()
item = pygame.sprite.Group()
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

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
        self.image = pygame.image.load(os.path.join(image_path, "player.png"))
        self.rect = self.image.get_rect()
        self.x = 100
        self.y = 600-self.image.get_height()
        self.step_x = 30
        self.step_y = 150
        self.isJump = False
        self.isFall = False
        self.jumpCount = 11
        self.locat = 1 # 1 = ground; 2 = LLedge; 3 = TLedge
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

lledge = LLedge()
tledge = TLedge()
edoor = EDoor()
player = Player_s()
enemy = Enemy_s()
key = Key()

all_sprites.add(lledge)
all_sprites.add(tledge)
all_sprites.add(edoor)
all_sprites.add(player)
all_sprites.add(enemy)
all_sprites.add(key)
cenario_l.add(lledge)
cenario_t.add(tledge)
cenario.add(edoor)
if plat.key_check == 0:
    item.add(key)
player_group.add(player)
enemy_group.add(enemy)

all_sprites.update()
all_sprites.draw(screen)
pygame.display.flip()

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
 
    if keys[pygame.K_x] and player.locat == 1:
        if player.x <= 150:
            import cavescreen1
            running = False
            break
        elif player.x >= 1050:
            import hallwayscreen1
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

    hit_lledge = pygame.sprite.spritecollide(player, cenario_l, False)

    if player.locat == 1:
        if player.isJump and hit_lledge:
            player.rect.y = lledge.rect.y + player.image.get_height()
            player.isJump = False
            player.isFall = False
            jump_temp = player.jumpCount
            player.jumpCount = 11
            player.locat = 2
    elif player.locat == 2:
        if player.isJump:
            hit_tledge = pygame.sprite.spritecollide(player, cenario_t, False)
            if hit_tledge:
                player.rect.y = tledge.rect.y + player.image.get_height()
                player.locat = 3
                player.isJump = False
                player.jumpCount = 0
                chest_enter = 1
        elif not(hit_lledge):
            player.locat = 1
            player.isJump = True
            player.jumpCount = jump_temp
    
    hit_tledge = pygame.sprite.spritecollide(player, cenario_t, False)

    if player.locat == 3:
        if player.x < tledge.rect.x or player.x > tledge.rect.x + tledge.image.get_width():
            player.isFall = True
            player.isJump = True
            attempt = 0

    if player.x >= 1050 and player.locat == 1:
        hallway_enter = 1
    else:
        hallway_enter = 0

    if player.x <= 150 and player.locat == 1:
        cave_enter = 1
    else:
        cave_enter = 0

    if plat.key_check == 0:
        hit_key = pygame.sprite.spritecollide(player, item, True)

        if hit_key:
            plat.key_check = 1
    
    hit_enemy = pygame.sprite.spritecollide(player, enemy_group, True)

    if hit_enemy:
        if player.locat != 1:
            player.rect.y = 600-player.image.get_height()
            if player.locat == 2:
                player.locat = 1
        import combat
        
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