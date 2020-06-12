import pygame
import os

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'sprites')

pygame.init()

screen = pygame.display.set_mode((640,480))
background = pygame.Surface(screen.get_size())
background.fill((17,143,139))
background = background.convert()

screen.blit(background, (0,0))
pygame.display.update()    

corgi = pygame.image.load(os.path.join(image_path,"Corgi.png"))
xpos = 50
ypos = 50
step_x = 10
step_y = 10

screen.blit(corgi, (xpos, ypos))
pygame.display.update()
xpos += step_x # move it to the right

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                break
            elif event.key == pygame.K_DOWN:
                ypos = ypos + step_y
            elif event.key == pygame.K_UP:
                ypos = ypos - step_y
            elif event.key == pygame.K_RIGHT:
                xpos = xpos + step_x
            elif event.key == pygame.K_LEFT:
                xpos = xpos - step_x
    screen.blit(background, (0,0))
    screen.blit(corgi, (xpos, ypos))
    pygame.display.update()
