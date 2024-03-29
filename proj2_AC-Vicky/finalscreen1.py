import pygame
import os
import stats

#import paths
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, 'sprites')
sound_path = os.path.join(current_path, 'sounds')

pygame.init()

#determining sprite classes
class Player_s(pygame.sprite.Sprite): #definition of each variable in stats.py
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(image_path, "man still.png"))
        self.rect = self.image.get_rect()
        self.x = 75
        self.y = 400
        self.step_x = 30
        self.step_y = 10
    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

class Boss_s(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(image_path, "goblin.png"))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*2, self.image.get_height()*2))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.x = 730
        self.y = 80
    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

def final_run(plat, running):
    plat.croom = "final"
    plat.lastroom = "doors"
    #this is the walk screen for the final boss screen

    #setting screen size
    screen = pygame.display.set_mode((1280,720))

    #setting scenery and static objects
    background = pygame.image.load(os.path.join(image_path, "ending.jpg"))
    screen.blit(background, (0,0))

    #importing sounds and music
    door_sound = pygame.mixer.Sound(os.path.join(sound_path, "close_door_1.wav"))
    music = pygame.mixer.music.load(os.path.join(sound_path, "combat.wav"))

    #creating sprites groups
    all_sprites = pygame.sprite.Group()
    player_group = pygame.sprite.Group()

    player = Player_s()
    boss = Boss_s()
    all_sprites.add(player)
    all_sprites.add(boss)

    #update screen
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    pygame.mixer.music.play()

    #messages
    font = pygame.font.Font('freesansbold.ttf', 36)
    #interact with boss
    text1 = font.render('Press x to fight', True, [0, 0, 0])
    text1Rect = text1.get_rect()
    text1Rect.center = (1280/2, 600)

    #return to doors
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
            plat.stop = 1
            running = False
            break

        if keys[pygame.K_x] and player.x >= 501: #interact with boss
            plat.lastroom = plat.croom
            plat.croom = "combat"
            plat.end = 1 #set end of game
            running = False
            break
        elif keys[pygame.K_x] and player.x <= 150: #return to doors
            plat.lastroom = plat.croom
            pygame.mixer.Sound.play(door_sound)
            pygame.mixer.music.stop()
            plat.croom = "doors"
            running = False
            break

        if keys[pygame.K_RIGHT] and player.x < 525: #move diagonally to the right within boundaries
            player.x = player.x + player.step_x
            player.y = player.y - player.step_y
       
        if keys[pygame.K_LEFT] and player.x > 100: #move diagonally to the left within boundaries
           player.x = player.x - player.step_x
           player.y = player.y + player.step_y

        #update screens and messages
        screen.blit(background, (0,0))
        all_sprites.update()
        all_sprites.draw(screen)
        if player.x >= 500:
            screen.blit(text1, text1Rect)
        if player.x <= 150:
            screen.blit(textreturn, textreturnRect)
        pygame.display.flip()

    return plat
