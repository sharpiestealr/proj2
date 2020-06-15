import pygame
import os
import stats

class Player_s(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(image_path, "player.png"))
        self.rect = self.image.get_rect()
        self.x = 640
        self.y = background.image.get_height() - 20
        self.step_x = 30
        self.step_y = 10
    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y


plat.lastroom = plat.croom
plat.croom = "doors"
#this is the walk screen for the 3 doors scene

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'sprites')

pygame.init()

#setting screen size
screen = pygame.display.set_mode((1280,720))

#setting scenery and static objects
background = pygame.image.load(os.path.join(image_path, "doors.jpg"))
screen.blit(background, (0,0))

all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()

player = Player_s()
all_sprites.add(player)

all_sprites.update()
all_sprites.draw(screen)
pygame.display.flip()

font = pygame.font.Font('freesansbold.ttf', 36)
text1 = font.render('Press x to open the chest', True, [0, 0, 0])
text1Rect = text1.get_rect()
text1Rect.center = (1280/2, 600)

textreturn = font.render('Press x to return', True, [0, 0, 0])
textreturnRect = textreturn.get_rect()
textreturnRect.center = (1280/2, 600)

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

    if keys[pygame.K_x] and 482 >= player.x >= 300:
        plat.lastroom = "doors"
        plat.croom = "puzzle"
        import puzzlescreen1
        running = False
        break
    elif keys[pygame.K_x] and 540 >= player.x >= 700:
        plat.lastroom = "doors"
        plat.croom = "final"
        import finalscreen1
        running = False
        break
    elif keys[pygame.K_x] and 760 >= player.x >= 927:
        plat.lastroom = "doors"
        plat.croom = "door3"
        import combat
        running = False
        break

    if keys[pygame.K_RIGHT] and player.x < 1200:
        if player.y > 402:
            player.x = player.x + player.step_x
            player.y = player.y - player.step_y
        if player.y < 400:
            player.y = 402
            if player.x < 300:
                player.x = 300
            elif player.x > 927:
                player.x = 927
       
    if keys[pygame.K_LEFT] and player.x > 100:
       if player.y > 402:
            player.x = player.x + player.step_x
            player.y = player.y - player.step_y
       if player.y < 400:
            player.y = 402
            if player.x < 300:
                player.x = 300
            elif player.x > 927:
                player.x = 927

    screen.blit(background, (0,0))
    all_sprites.update()
    all_sprites.draw(screen)
    if player.x >= 500:
        screen.blit(text1, text1Rect)
    if player.x <= 150:
        screen.blit(textreturn, textreturnRect)
    pygame.display.flip()
