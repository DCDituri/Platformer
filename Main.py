import pygame
from pygame import *
import sys

pygame.init()

#Window Options
WINDOW = pygame.display.set_mode([800,600])
pygame.display.set_caption("Aww Yeah!")

#Colors
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
        collisionLeft = False
        collisionDown = False
        collisionRIght = False
        
        self.image = pygame.image.load("beach.png")
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def jump(self):
                if (self.onGround == False):
                        return

                self.velocity = 13
                self.onGround = False

    def detectCollisionsDown(self, x1, y1, w1, h1, x2, y2, w2, h2):
                if (x2+w2 >= x1 >= x2 and y2+h2 >= y1+h1 >= y2): #Top
                        return True
                elif (x2+w2 >= x1+w1 >= x2 and y2+h2 >= y1+h1 >= y2): #Top
                        return True
                else:
                        return False
                    
    def update(self):
        if(self.velocity < 0):
            self.falling = True

        #Checking for Collisions
        for block in blockList:
            collisionDown = self.detectCollisionsDown(self.x, self.y, self.width, self.height, block.x, block.y, block.width, block.height)
            if (collisionDown == True):
                break

        #Reacting to Collisions
        if collisionDown == True:
            if(self.falling == True): #only if falling
                self.falling = False
                self.onGround = True
                self.velocity = 0
                self.y = block.y - self.height
        else:
            self.onGround = False

        if self.onGround == False:
            self.velocity += gravity
        self.y -= self.velocity
        self.x += self.movex
        WINDOW.blit(self.image, (self.x, self.y))
        pygame.display.update()

    def render(self, WINDOW):
        WINDOW.blit(self.image, (self.x, self.y))


class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32

    def render(self, WINDOW):
        pygame.draw.rect(WINDOW, white, (self.x, self.y, self.width, self.height))

player = Player()
player.__init__()


level1 = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
blockList = []

for y in range (0, len(level1)):
    for x in range (0, len(level1[y])):
        if (level1[y][x]==1):
            blockList.append(Block(x*32, y*32))



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

            if (event.key == K_UP):
                player.jump()
                                
        if (event.type == KEYUP):
            if (event.key == K_RIGHT):
                player.movex = 0
            if (event.key == K_LEFT):
                player.movex = 0
            
                                
    WINDOW.fill(black)
    for block in blockList:
        block.render(WINDOW)
    player.update()
    player.render(WINDOW)
    clock.tick(FPS)
    pygame.display.update()


