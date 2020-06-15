import pygame
import os
import stats

plat = stats.Player()
plat.croom = "doors"
plat.lastroom = "doors"
#this is the walk screen for the 3 doors scene

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'sprites')

pygame.init()

#setting screen size
screen = pygame.display.set_mode((1280,720))

#setting scenery and static objects
background = pygame.image.load(os.path.join(image_path, "doors.jpg"))
screen.blit(background, (0,0))

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

    if keys[pygame.K_LEFT]:
        plat.lastroom = "doors"
        plat.croom = "puzzle"
        import puzzlescreen1
        running = False
        break

    if keys[pygame.K_UP]:
        plat.lastroom = "doors"
        plat.croom = "final"
        import finalscreen1
        running = False
        break

    if keys[pygame.K_RIGHT]:
        plat.lastroom = "doors"
        plat.croom = "door3"
        import combat

    if keys[pygame.K_x]:
        import hallwayscreen1
        running = False
        break

    screen.blit(background, (0,0))
    screen.blit(text1, text1Rect)
    screen.blit(text2, text2Rect)
    screen.blit(text3, text3Rect)
    screen.blit(textreturn, textreturnRect)
    pygame.display.flip()
