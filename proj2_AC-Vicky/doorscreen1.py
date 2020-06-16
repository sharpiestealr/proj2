import pygame
import os
import stats

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'sprites')
sound_path = os.path.join(current_path, 'sounds')
running = False

pygame.init()

def door_run(plat, running):
    #setting screen size
    screen = pygame.display.set_mode((1280,720))

    #setting scenery and static objects
    background = pygame.image.load(os.path.join(image_path, "doors.jpg"))
    screen.blit(background, (0,0))

    #importing sounds and music
    coin_sound = pygame.mixer.Sound(os.path.join(sound_path, "coin_collect.wav"))
    door_sound = pygame.mixer.Sound(os.path.join(sound_path, "close_door_1.wav"))
    music = pygame.mixer.music.load(os.path.join(sound_path, "walk.wav"))

    font = pygame.font.Font('freesansbold.ttf', 36)
    text1 = font.render('LEFT', True, [0, 0, 0])
    text1Rect = text1.get_rect()
    text1Rect.center = (400, 150)
    text2 = font.render('UP', True, [0, 0, 0])
    text2Rect = text2.get_rect()
    text2Rect.center = (1280/2, 150)
    text3 = font.render('RIGHT', True, [0, 0, 0])
    text3Rect = text3.get_rect()
    text3Rect.center = (850, 150)

    textreturn = font.render('Press x to return', True, [0, 0, 0])
    textreturnRect = textreturn.get_rect()
    textreturnRect.center = (1280/2, 600)

    screen.blit(text1, text1Rect)
    screen.blit(text2, text2Rect)
    screen.blit(text3, text3Rect)
    screen.blit(textreturn, textreturnRect)

    pygame.display.flip()
    pygame.mixer.music.play()

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

        if keys[pygame.K_LEFT]:
            pygame.mixer.Sound.play(door_sound)
            pygame.mixer.music.stop()
            plat.lastroom = plat.croom
            plat.croom = "chest2"
            running = False
            break

        if keys[pygame.K_UP]:
            pygame.mixer.Sound.play(door_sound)
            pygame.mixer.music.stop()
            plat.lastroom = plat.croom
            plat.croom = "final"
            running = False
            break

        if keys[pygame.K_RIGHT]:
            pygame.mixer.Sound.play(door_sound)
            pygame.mixer.music.stop()
            plat.lastroom = plat.croom
            plat.enemy_door = 1
            plat.croom = "combat"
            running = False
            break

        if keys[pygame.K_x]:
            pygame.mixer.Sound.play(door_sound)
            pygame.mixer.music.stop()
            plat.lastroom = plat.croom
            plat.croom = "hallway"
            plat.stop = 0
            running = False
            break

        screen.blit(background, (0,0))
        screen.blit(text1, text1Rect)
        screen.blit(text2, text2Rect)
        screen.blit(text3, text3Rect)
        screen.blit(textreturn, textreturnRect)
        pygame.display.flip()

    return plat
