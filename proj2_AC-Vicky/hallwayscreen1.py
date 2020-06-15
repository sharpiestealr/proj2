import pygame
import os
import stats

plat = stats.Player()
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

all_sprites = pygame.sprite.Group()
cenario = pygame.sprite.Group()
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

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
        self.locat = 1 # 1 = ground
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
        self.x = 800
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
        self.image = pygame.Surface((0, 338))
        self.rect = self.image.get_rect()
        self.x = 0
        self.xmax = 110
        self.y = 338
        self.ymax = 622
    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

class EDoor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1233, 320))
        self.rect = self.image.get_rect()
        self.x = 1233
        self.xmax = 1280
        self.y = 320
        self.ymax = 622
    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

idoor = IDoor()
edoor = EDoor()
player = Player_s()
enemy = Enemy_s()

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
textidoorRect = textidoor.get_rect()
textidoorRect.center = (700, 50)

textedoor = font.render("Press x to enter", True, [0, 0, 0])
textedoorRect = textedoor.get_rect()
textedoorRect.center = (700, 50)

attempt = 0
key_enter = 0
doors_enter = 0
    
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
        if player.x <= 150:
            import keyscreen1
            running = False
            break
        elif player.x >= 1050:
            import doorscreen1
            running = False
            break

    if keys[pygame.K_UP]:
        attempt = 1

    if keys[pygame.K_RIGHT] and player.x < 1150:
        player.x = player.x + player.step_x
       
    if keys[pygame.K_LEFT] and player.x > 50:
       player.x = player.x - player.step_x

    if player.x >= 1100:
        doors_enter = 1
    else:
        doors_enter = 0

    if player.x <= 109:
        key_enter = 1
    else:
        key_enter = 0
    
    hit_enemy = pygame.sprite.spritecollide(player, enemy_group, False)

    if hit_enemy:
        import combat
        enemy.kill()
        
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
