import pygame
from pygame import *
from pygame import mixer
import sys, os

pygame.init()

#Window Options
WINDOW = pygame.display.set_mode([800,600])
pygame.display.set_caption("Aww Yeah!")

#Playing sounds
folder = os.path.dirname(os.path.realpath('__file__'))
fileName = os.path.join(folder, 'Sounds\\')
fileName = os.path.abspath(os.path.realpath(fileName))
namesList = ["Walk", "Jump", "Background", "Blast"] #name of the song files
songList = [] #puts the song paths into a list
for names in namesList:
    songPath = fileName + "\\" + names + ".wav"
    songList.append(songPath)

mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
walk = mixer.Sound(songList[0])
jump = mixer.Sound(songList[1])
bg = mixer.Sound(songList[2])
blast = mixer.Sound(songList[3])

#Colors
black = (0, 0, 0)
white = (255, 255, 255)
purple = (160, 32, 240, 155)
blue = (51, 199, 255, 196)
silver = (192, 192, 192, 192)
scarlet = (255, 36, 0, 200)

RIGHT = "right"
LEFT = "left"

running = True
FPS = 60
bulletCD = 0
clock = pygame.time.Clock()

step = 5
gravity = -0.5
gameLoop = True
GAMESTART = 1
GAMERUNNING = 2
GAMEFINISHED = 3
GAMEQUIT = 4
STATUS = GAMESTART

#############################PLAYER 1###############################################


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
        self.user = 1
        self.direction = RIGHT
        self.bulletCount = 0
        self.collect = 0
        
        self.image = pygame.image.load("Player1.png")
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def jump(self):
                if (self.onGround == False):
                        return

                self.velocity = 13
                self.onGround = False

    def detectCollisions(self, x1, y1, w1, h1, x2, y2, w2, h2):
                if (x2+w2 >= x1 >= x2 and y2+h2 >= y1+h1 >= y2): #Top
                        return True
                elif (x2+w2 >= x1+w1 >= x2 and y2+h2 >= y1+h1 >= y2): #Top
                        return True
                else:
                        return False

    def borders(self):
        if (self.x + self.width) >= 768: #Right border
            self.x = 768 - self.width
            
        elif self.x <= 32: #left border
            self.x = 32

        if self.y <= 32: #top border
            self.y = 32
            self.velocity = 0 #stops upward movement
                            
    def update(self):
        if(self.velocity < 0):
            self.falling = True

        #Checking for Collisions
        for block in blockList:
            collisionDown = self.detectCollisions(self.x, self.y, self.width, self.height, block.x, block.y, block.width, block.height)
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

        #Checking for Collection
        for item in itemList:
            collection = self.detectCollisions(self.x, self.y, self.width, self.height, item.x, item.y, item.width, item.height)
            if (collection == True):
                blockList.append(Block(item.x, item.y))
                itemList.remove(item)
                self.collect = self.collect + 1
                blast.play()
                break

        self.borders() #Makes sure the player does not exit the 

        if self.onGround == False:
            self.velocity += gravity
        self.y -= self.velocity
        self.x += self.movex
        WINDOW.blit(self.image, (self.x, self.y))
        pygame.display.update()

    def render(self, WINDOW):
        WINDOW.blit(self.image, (self.x, self.y))
###############################END PLAYER 1###################################################################

################################PLAYER 2#####################################################################
class Player2(sprite.Sprite):
    def __init__ (self):
        sprite.Sprite.__init__(self)
        self.velocity = 0
        self.onGround = False
        self.falling = True
        self.x = 650
        self.y = 450
        self.user = 2
        self.movex = 0
        collisionDown = False
        self.direction = LEFT
        self.collect = 0
        
        self.image = pygame.image.load("Player2.png")
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def jump(self):
                if (self.onGround == False):
                        return

                self.velocity = 13
                self.onGround = False

    def detectCollisions(self, x1, y1, w1, h1, x2, y2, w2, h2):
                if (x2+w2 >= x1 >= x2 and y2+h2 >= y1+h1 >= y2): #Top
                        return True
                elif (x2+w2 >= x1+w1 >= x2 and y2+h2 >= y1+h1 >= y2): #Top
                        return True
                else:
                        return False



    def borders(self):
        if (self.x + self.width) >= 768: #Right border
            self.x = 768 - self.width
            
        elif self.x <= 32: #left border
            self.x = 32

        if self.y <= 32: #top border
            self.y = 32
            self.velocity = 0 #stops upward movement
                   
    def update(self):
        if(self.velocity < 0):
            self.falling = True

        #Checking for Collisions
        for block in blockList:
            collisionDown = self.detectCollisions(self.x, self.y, self.width, self.height, block.x, block.y, block.width, block.height)
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
            
        #Checking for Collection
        for item in itemList:
            collection = self.detectCollisions(self.x, self.y, self.width, self.height, item.x, item.y, item.width, item.height)
            if (collection == True):
                blockList.append(Block(item.x, item.y))
                itemList.remove(item)
                self.collect = self.collect + 1
                blast.play()
                break
            
        self.borders() #Makes sure the player does not exit the 

        if self.onGround == False:
            self.velocity += gravity
        self.y -= self.velocity
        self.x += self.movex
        WINDOW.blit(self.image, (self.x, self.y))
        pygame.display.update()

    def render(self, WINDOW):
        WINDOW.blit(self.image, (self.x, self.y))
########################################################END PLAYER 2###########################################################3     
        
class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32

    def render(self, WINDOW):
        pygame.draw.rect(WINDOW, silver, (self.x, self.y, self.width, self.height))


class Items:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32

    def render(self, WINDOW):
        pygame.draw.rect(WINDOW, scarlet, (self.x, self.y, self.width, self.height))


def levelRender():

    level1 = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 2, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    

    for y in range (0, len(level1)):
        for x in range (0, len(level1[y])):
            if (level1[y][x]==1):
                blockList.append(Block(x*32, y*32))

    for y in range (0, len(level1)):
        for x in range (0, len(level1[y])):
            if (level1[y][x]==2):
                itemList.append(Items(x*32, y*32))

while STATUS == GAMESTART:
    titleScreen  = pygame.image.load("TitleScreen.jpg")
    WINDOW.blit(titleScreen, (0, 0))
    pygame.display.update()
    for event in pygame. event.get():
        if (event.type == QUIT):
            STATUS = GAMEQUIT
            pygame.quit()
            sys.exit()
        if (event.type == KEYDOWN):
            if (event.key == K_SPACE):
                STATUS = GAMERUNNING
    

blockList = []
itemList = []

player = Player()
player.__init__()
player2 = Player2()
player2.__init__()
levelRender()

while STATUS == GAMERUNNING:
    bg.play()
    for event in pygame.event.get():
        if (event.type==QUIT):
            STATUS = GAMEQUIT
            pygame.quit()
            sys.exit()
        #####Player 1 Inputs######
        if (player.user == 1):
            if (event.type == KEYDOWN):
                if (event.key == K_d):
                    player.movex = step
                    player.direction = RIGHT
                    walk.play(loops=-1)
                elif (event.key == K_a):
                    player.movex = -step
                    player.direction = LEFT
                    walk.play(loops=-1)
                if (event.key == K_w):
                    player.jump()
                    jump.play()
 
                if (event.key == K_SPACE):#Will stop the program to play the music
                    print "DJ Start the music"
            if (event.type == KEYUP):
                walk.stop()
                if (event.key == K_d):
                    player.movex = 0
                if (event.key == K_a):
                    player.movex = 0

        #####Player 2 Inputs######
        if (player2.user == 2):
            if (event.type == KEYDOWN):
                if (event.key == K_RIGHT):
                    player2.movex = step
                    player2.direction = RIGHT
                    walk.play(loops=-1)
                if (event.key == K_LEFT):
                    player2.movex = -step
                    player2.direction = LEFT
                    walk.play(loops=-1)
                if (event.key == K_UP):
                    player2.jump()
                    jump.play()
                                    
            if (event.type == KEYUP):
                walk.stop()
                if (event.key == K_RIGHT):
                    player2.movex = 0
                if (event.key == K_LEFT):
                    player2.movex = 0
            
    WINDOW.fill(black)
    for item in itemList:
        item.render(WINDOW)
    for block in blockList:
        block.render(WINDOW)
    player.update()
    player2.update()
    player.render(WINDOW)
    player2.render(WINDOW)
    clock.tick(FPS)
    pygame.display.update()
    print itemList
    if itemList == []:
        STATUS = GAMEFINISHED

    while STATUS == GAMEFINISHED:
        if player.collect > player2.collect:
            endScreen = pygame.image.load("player1victory.jpg")
        elif player2.collect > player.collect:
            endScreen = pygame.image.load("player2victory.jpg")
        else:
            endScreen = pygame.image.load("novictory.jpg")
        WINDOW.blit(endScreen, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if (event.type==QUIT):
                STATUS = GAMEQUIT
                pygame.quit()
                sys.exit()


