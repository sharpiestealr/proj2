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
        self.image = pygame.image.load(os.path.join(image_path, "player.png"))
        self.rect = self.image.get_rect()
        self.x = 75
        self.y = 400
        self.step_x = 30
        self.step_y = 10
    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

def chest_run(plat, running):

    plat.lastroom = plat.croom
    plat.croom = "chest"
    
    plat.player = Player_s()

    #setting screen size
    screen = pygame.display.set_mode((1280,720))

    #setting scenery and static objects
    background = pygame.image.load(os.path.join(image_path, "chest.jpg"))
    screen.blit(background, (0,0))

    #importing sounds and music
    coin_sound = pygame.mixer.Sound(os.path.join(sound_path, "coin_collect.wav"))
    door_sound = pygame.mixer.Sound(os.path.join(sound_path, "close_door_1.wav"))

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
    
    while running:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                plat.stop = 1  
                running = False
                break
    
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            running = False
            plat.stop = 1 
            break

        if keys[pygame.K_x] and player.x >= 501:
            pygame.mixer.Sound.play(door_sound)
            pygame.mixer.music.stop()
            plat.lastroom = plat.croom
            plat.croom = "combat"
            plat.chest = 1
            running = False
            break
        elif keys[pygame.K_x] and player.x <= 150:
            plat.lastroom = plat.croom
            plat.croom = "cave"
            pygame.mixer.Sound.play(door_sound)
            pygame.mixer.music.stop()
            running = False
            break

        if keys[pygame.K_RIGHT] and player.x < 525:
            player.x = player.x + player.step_x
            player.y = player.y - player.step_y
       
        if keys[pygame.K_LEFT] and player.x > 100:
           player.x = player.x - player.step_x
           player.y = player.y + player.step_y

        screen.blit(background, (0,0))
        all_sprites.update()
        all_sprites.draw(screen)
        if player.x >= 500:
            screen.blit(text1, text1Rect)
        if player.x <= 150:
            screen.blit(textreturn, textreturnRect)
        pygame.display.flip()

    return plat