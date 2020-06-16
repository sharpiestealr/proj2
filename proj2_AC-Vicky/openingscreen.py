import pygame
import os
import stats

plat = stats.Player()
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'sprites')
sound_path = os.path.join(current_path, 'sounds')

pygame.init()

running = False #add this below the change in croom

def opening_run(plat):
    plat.croom = "opening"

    screen = pygame.display.set_mode((1280,720))

    background = pygame.image.load(os.path.join(image_path, "opening.jpg"))
    screen.blit(background, (0,0))

    #creating cursor
    cursor = pygame.image.load(os.path.join(image_path, "arrow.png"))
    cursor_x = 343 - cursor.get_width()
    cursor_y = 360
    posi = 1
    screen.blit(cursor, (cursor_x, cursor_y))
    music = pygame.mixer.music.load(os.path.join(sound_path, "open.wav"))

    pygame.display.flip()
    pygame.mixer.music.play()

    instruct = 0

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                plat.stop = 1 
                running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    plat.stop = 1
                    running = False
                    break
                elif event.key == pygame.K_DOWN:
                    if posi < 3:
                        cursor_y = cursor_y + 90
                        posi = posi + 1
                elif event.key == pygame.K_UP:
                    if posi > 1:
                        cursor_y = cursor_y - 90
                        posi = posi - 1
                if event.key == pygame.K_x:
                    if posi == 1:
                        instruct = 1
                    elif posi == 2:
                        plat.lastroom = plat.croom
                        plat.croom = "credits"
                        running = False
                        break
                    elif posi == 3:
                        plat.stop = 1
                        running = False
                        break
                    if instruct == 1:
                        plat.croom = "cave"
                        running = False
                        break

        if instruct == 1:
            instructions = pygame.image.load(os.path.join(image_path, "instructions.jpg"))
            screen.blit(instructions, (0,0))
        else:
            screen.blit(background, (0,0))
            screen.blit(cursor, (cursor_x, cursor_y))
        pygame.display.flip()

    return plat