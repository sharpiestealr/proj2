import pygame
import os
import stats

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'sprites')
sound_path = os.path.join(current_path, 'sounds')
running = False

pygame.init()

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

def door_run(plat, running):
    plat.player = Player_s()

    plat.lastroom = plat.croom
    plat.croom = "doors"
    #this is the walk screen for the 3 doors scene

    #setting screen size
    screen = pygame.display.set_mode((1280,720))

    #setting scenery and static objects
    background = pygame.image.load(os.path.join(image_path, "doors.jpg"))
    screen.blit(background, (0,0))

    #importing sounds and music
    coin_sound = pygame.mixer.Sound(os.path.join(sound_path, "coin_collect.wav"))
    door_sound = pygame.mixer.Sound(os.path.join(sound_path, "close_door_1.wav"))

    all_sprites = pygame.sprite.Group()
    plat.player_group = pygame.sprite.Group()

    all_sprites.add(plat.player)

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
                plat.stop = 1 
                running = False
                break

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            plat.stop = 1
            running = False
            break

        if keys[pygame.K_x] and 482 >= plat.player.x >= 300:
            pygame.mixer.Sound.play(door_sound)
            pygame.mixer.music.stop()
            plat.lastroom = plat.croom
            plat.croom = "puzzle"
            running = False
            break
        elif keys[pygame.K_x] and 540 >= plat.player.x >= 700:
            pygame.mixer.Sound.play(door_sound)
            pygame.mixer.music.stop()
            plat.lastroom = plat.croom
            plat.croom = "final"
            running = False
            break
        elif keys[pygame.K_x] and 760 >= plat.player.x >= 927:
            if plat.enemy_door == 0:
                pygame.mixer.Sound.play(door_sound)
                pygame.mixer.music.stop()
                plat.lastroom = plat.croom
                plat.enemy_door = 1
                plat.croom = "combat"
                running = False
                break

        if keys[pygame.K_RIGHT] and plat.player.x < 1200:
            if plat.player.y > 402:
                plat.player.x = plat.player.x + plat.player.step_x
                plat.player.y = plat.player.y - plat.player.step_y
            if plat.player.y < 400:
                plat.player.y = 402
                if plat.player.x < 300:
                    plat.player.x = 300
                elif plat.player.x > 927:
                    plat.player.x = 927

        if keys[pygame.K_LEFT] and plat.player.x > 100:
           if plat.player.y > 402:
                plat.player.x = plat.player.x + plat.player.step_x
                plat.player.y = plat.player.y - plat.player.step_y
           if plat.player.y < 400:
                plat.player.y = 402
                if plat.player.x < 300:
                    plat.player.x = 300
                elif plat.player.x > 927:
                    plat.player.x = 927

        screen.blit(background, (0,0))
        all_sprites.update()
        all_sprites.draw(screen)
        if plat.player.x >= 500:
            screen.blit(text1, text1Rect)
        if plat.player.x <= 150:
            screen.blit(textreturn, textreturnRect)
        pygame.display.flip()
