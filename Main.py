import pygame
from pygame import *
import sys

pygame.init()

WINDOW = pygame.display.set_mode([800,600])
pygame.display.set_caption("Aww Yeah!")

black = (0,0,0)
white = (255, 255, 255)

running = True
FPS = 60
clock = pygame.time.Clock()

step = 5
gravity = -0.5
gameLoop = True

class Player(sprite.Sprite):
    def __init__ (self):
        sprite.Sprite.__init__(self)
        self.velocity = 0
        self.onGround = False
        self.falling = True
        self.x = 50
        self.y = 450
        self.movex = 0
        
        self.image = pygame.image.load("beach.png")
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def jump(self):
                if (self.onGround == False):
                        return

                self.velocity = 13
                self.onGround = False

    def update(self):
        if(self.velocity < 0):
            self.falling = True
            
       
        self.x += self.movex
        WINDOW.blit(self.image, (self.x, self.y))
        pygame.display.update()

    def render(self, WINDOW):
        WINDOW.blit(self.image, (self.x, self.y))


    
class Walls:
    def __init__ (self):
        self.w1 = [0, 500, 800, 100]
        self.w2 = [350, 450, 50, 50]
        self.wallOne = pygame.draw.rect(WINDOW, white, self.w1)
        self.wallTwo = pygame.draw.rect(WINDOW, white, self.w2)

    def update(self):
        pygame.display.update()

    def render(self):
        pygame.draw.rect(WINDOW, white, self.w1)
        pygame.draw.rect(WINDOW, white, self.w2)


player = Player()
player.__init__()
walls = Walls()
walls.__init__()

while running:
    for event in pygame.event.get():
        if (event.type==QUIT):
            running = False
            pygame.quit()
            sys.exit()
        if (event.type == KEYDOWN):
            if (event.key == K_RIGHT):
                player.movex = step
            if (event.key == K_LEFT):
                player.movex = -step

            #if (event.key == K_UP):
                #player.jump()
                                
        if (event.type == KEYUP):
            if (event.key == K_RIGHT):
                player.movex = 0
            if (event.key == K_LEFT):
                player.movex = 0
            
                                
    WINDOW.fill(black)
    walls.render()
    player.update()
    player.render(WINDOW)
    clock.tick(FPS)
    pygame.display.update()
    print player.x


