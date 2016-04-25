from pygame import *
import sys

##################################################################
#                                       Music ft. Platform Deathmatch                                                       #
#                           Dallas Dituri, Bryan Rodriguez, Jennifer Nguyen                                           #
#                               https://github.com/DCDituri/Platformer                                                 #
##################################################################

#########################Classes####################################
class Player(sprite.Sprite):
    def __init__ (self, x, y):
        
        sprite.Sprite.__init__(self)
        self.image = image.load("beach.png")
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.onGround = False
        #Set speed of the player
        self.change_x = 0
        self.change_y = 0
        self.level = None

    def update(self):
        #Gravity
        if (self.onGround == False):
            self.change_y += gravity
        #Move left/right
        self.rect.x += self.change_x

        #Horizontal Collision Detection
        block_hit_list = sprite.spritecollide(self, blockList, False)
        for block in block_hit_list:
            #Moving Right
            if self.change_x > 0:
                self.rect.right = block.rect.x
            #Moving Left
            elif self.change_x < 0:
                self.rect.left = block.rect.x + size

        #Move up/down
        self.rect.y += self.change_y

        #Vertical Collision Detection
        block_hit_list = sprite.spritecollide(self, blockList, False)
        for block in block_hit_list:
            #Falling
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
                self.onGround = True

            else:
                self.onGround = False
                
            #Rising
            if self.change_y < 0:
                self.rect.top = block.rect.bottom

            #Stop Vertical Movement
            self.change_y = 0

    def jump(self):
        if (onGround == False):
            return

        self.change_y = 13
        self.onGround = False

    def go_left(self):
        self.change_x = -speed

    def go_right(self):
        self.change_x = speed

    def stop(self):
        self.change_x = 0

    def draw(self, window):
        draw.rect(window, self.image, [self.x, self.y])
        
class Block:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.width = size
        self.height = size

    def render(self, window):
        pygame.draw.rect(window, black, [self.x, self.y, self.width, self.height])

class Walls(sprite.Sprite):
    def __init__(self, blockList):

        for block in blockList:
            self.image = Surface([width, height])
            self.image.fill(black)

        self.rect = self.image.get_rect()
################################################################

################### Initializing Variables ################################
wWidth = 800
wHeight = 600
window = display.set_mode([wWidth, wHeight])
display.set_caption("It's About Damn Time")

blue = (51, 199, 255, 196)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 36, 0)
silver = (192, 192, 192)

gravity = -0.5
speed = 5
size = 32
FPS = 60
clock = time.Clock()

gameLoop = True

player = Player(100, 500)
##################################################################

####################### Classes #####################################

level = [
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
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

blockList = []
for y in range(0, len(level)):
    for x in range(0, len(level[y])):
        if (level[y][x]==1):
            blockList.append(Block(x*32, y*32))
                    
while gameLoop:
    for e in event.get():
        if e.type == QUIT:
            gameLoop = False

        if e.type == KEYDOWN:
            if e.key == K_LEFT:
                player.go_left()
            if e.key == K_RIGHT:
                player.go_right()
            if e.key == K_UP:
                player.jump()

        if e.type == KEYUP:
            if e.key == K_LEFT and player.change_x < 0:
                player.stop()
            if e.key == K_RIGHT and player.change_x > 0:
                player.stop()

    player.update()
    
    Level.draw(window)
    player.draw(window)
    

    
    
    
    clock.tick(FPS)
    display.flip()

quit()
sys.exit()


        
