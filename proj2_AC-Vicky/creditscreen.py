import pygame
import os
import stats

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'sprites')
sound_path = os.path.join(current_path, 'sounds')

pygame.init()

def credits_run(plat, running):

    plat.lastroom = plat.croom
    plat.croom = "credits"
 
 #setting screen size
    screen = pygame.display.set_mode((1280,720))

    #setting scenery and static objects
    background = pygame.image.load(os.path.join(image_path, "credits.jpg"))
    screen.blit(background, (0,0))

    #importing sounds and music
    music = pygame.mixer.music.load(os.path.join(sound_path, "ending.wav"))
    
    pygame.display.flip()
    pygame.mixer.music.play()

    while running:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                plat.stop = 1  
                running = False
                break
            elif event.type == pygame.KEYDOWN:
                plat.croom = "opening"
                running = False
                break

        screen.blit(background, (0,0))
        pygame.display.flip()

    return plat
