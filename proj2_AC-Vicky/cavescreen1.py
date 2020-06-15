import pygame
import os
import stats
#import combat

plat = stats.Player()

#this is the walk screen for THE FIRST CAVE BEFORE THE PUZZLE

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'sprites')

pygame.init()

#setting screen size
screen = pygame.display.set_mode((1280,720))

#setting scenery and static objects
background = pygame.image.load(os.path.join(image_path, "walk.jpg"))
screen.blit(background, (0,0))

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
        self.rect.y = 224

class EDoor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(image_path, "door.png"))
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.x = 1230
        self.y = 605-self.image.get_height()

class Player_s(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(image_path, "player.png"))
        self.rect = self.image.get_rect()
        self.x = 100
        self.y = 405
        self.right = False
        self.left = False
        self.step_x = 30
        self.step_y = 230
        self.isJump = False
        self.jumpCount = 11
    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

class Enemy_s(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(image_path, "slime mockup.png"))
        self.rect = self.image.get_rect()
        self.step = 10
    def update(self):
        self.rect.x = 780
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
item.add(coin)
player_group.add(player)
enemy_group.add(enemy)

all_sprites.update()
all_sprites.draw(screen)
pygame.display.flip()

transparent = (0, 0, 0, 0)
    
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

    if not(player.isJump):
        if keys[pygame.K_UP]:
            player.isJump = True
    else:
        if player.jumpCount >= -11:
           player.y -= (player.jumpCount * abs(player.jumpCount)) * 0.5
           player.jumpCount -= 1
        else: # This will execute if our jump is finished
           player.jumpCount = 11
           player.isJump = False
           # Resetting our Variables

    if keys[pygame.K_RIGHT] and player.x < 1150:
        player.x = player.x + player.step_x
       
    if keys[pygame.K_LEFT] and player.x > 100:
       player.x = player.x - player.step_x

    hit_ledge = pygame.sprite.spritecollide(player, cenario_l, False)

    if player.isJump and hit_ledge:
        player.rect.y = ledge.rect.y + player.image.get_height()
        player.isJump = False
    elif not(hit_ledge):
        if player.rect.y != 605 - player.image.get_height():
            player.isJump = True

    hit_coin = pygame.sprite.spritecollide(player, item, True)

    if hit_coin:
        plat.coins += 1
    
    hit_enemy = pygame.sprite.spritecollide(player, enemy_group, True)

    if hit_enemy:
        import combat
        
    screen.blit(background, (0,0))
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()