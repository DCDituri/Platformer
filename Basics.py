import random
import pygame
import sys
from pygame.locals import *

pygame.init()

#Colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (51, 199, 255, 196)
red = (255, 0, 0)
bg = black

FPS = 30
dispWidth = 800
dispHeight = 600
cellSize = 10

UP = 'up'
DOWN = 'down'
RIGHT = 'right'
LEFT = 'left'

deadZones = []

def whatNext():
    for event in pygame.event.get([KEYDOWN, KEYUP, QUIT]):
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            continue
        return event.key
    return None

def makeTextObjs(text, font, tcolor):
    textSurface = font.render(text, True, tcolor)
    return textSurface, textSurface.get_rect()

def msgSurface(text, textColor):
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    largeText = pygame.font.Font('freesansbold.ttf', 150)
    
    titleTextSurf, titleTextRect = makeTextObjs(text, largeText, textColor)
    titleTextRect.center = (int(dispWidth/2),int(dispHeight/2))
    setDisplay.blit(titleTextSurf, titleTextRect)

    typTextSurf, typTextRect = makeTextObjs('Press any key to continue', smallText, white)
    typTextRect.center = (int(dispWidth/2),int(dispHeight/2)+120)
    setDisplay.blit(typTextSurf, typTextRect)
    pygame.display.update()
    fpsTime.tick()

    while whatNext() == None:
        for event in pygame.event.get([QUIT]):
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fpsTime.tick()

    runGame()

def evilMove(evilGuy):
    evilCoords = []
 
    randomMovex = random.randrange(-1, 2)
    randomMovey = random.randrange(-1, 2)
    
    newCell = {'x':evilGuy[0]['x'] + randomMovex, 'y':evilGuy[0]['y'] + randomMovey}
    if (newCell['x'] < 0 or newCell['y'] < 0 or newCell['x'] > dispWidth/cellSize or newCell['y'] > dispHeight/cellSize):
                newCell = {'x': dispWidth/(2*cellSize), 'y':dispHeight/(2*cellSize)}
    del evilGuy[-1]
    evilCoords.append(newCell['x'])
    evilCoords.append(newCell['y'])
    deadZones.append(evilCoords)
    evilGuy.insert(0, newCell)

def runGame():
    global deadZones
    startx = 10
    starty = 10
    coords = [{'x':startx, 'y':starty}]
    eCoords1 = [{'x': dispWidth/(2*cellSize), 'y':dispHeight/(2*cellSize)}]
    eCoords2 = [{'x': dispWidth/(2*cellSize), 'y':dispHeight/(2*cellSize)}]
    eCoords3 = [{'x': dispWidth/(2*cellSize), 'y':dispHeight/(2*cellSize)}]
    eCoords4 = [{'x': dispWidth/(2*cellSize), 'y':dispHeight/(2*cellSize)}]
    eCoords5 = [{'x': dispWidth/(2*cellSize), 'y':dispHeight/(2*cellSize)}]
    eCoords6 = [{'x': dispWidth/(2*cellSize), 'y':dispHeight/(2*cellSize)}]
    eCoords7 = [{'x': dispWidth/(2*cellSize), 'y':dispHeight/(2*cellSize)}]
    eCoords8 = [{'x': dispWidth/(2*cellSize), 'y':dispHeight/(2*cellSize)}]
    eCoords9 = [{'x': dispWidth/(2*cellSize), 'y':dispHeight/(2*cellSize)}]
    
    direction = RIGHT
    isAlive = 'yes'

    while True:

        while (isAlive == 'yes'):
            deadZones = []
        
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == KEYDOWN:
                    if event.key == (K_LEFT or K_A):
                        direction = LEFT
                    elif event.key == (K_RIGHT or K_D):
                        direction = RIGHT
                    elif event.key == (K_UP or K_W):
                        direction = UP
                    elif event.key == (K_DOWN or K_S):
                        direction = DOWN

            if direction == UP:
                newCell = {'x':coords[0]['x'], 'y':coords[0]['y']-1}
            elif direction == DOWN:
                newCell = {'x':coords[0]['x'], 'y':coords[0]['y']+1}
            elif direction == LEFT:
                newCell = {'x':coords[0]['x']-1, 'y':coords[0]['y']}
            elif direction == RIGHT:
                newCell = {'x':coords[0]['x']+1, 'y':coords[0]['y']}

            del coords[-1]

            coords.insert(0, newCell)
            setDisplay.fill(bg)

            evilMove(eCoords1)
            evilMove(eCoords2)
            evilMove(eCoords3)
            evilMove(eCoords4)
            evilMove(eCoords5)
            evilMove(eCoords6)
            evilMove(eCoords7)
            evilMove(eCoords8)
            evilMove(eCoords9)
            
            drawCell(coords, white)
            drawCell(eCoords1, red)
            drawCell(eCoords2, red)
            drawCell(eCoords3, red)
            drawCell(eCoords4, red)
            drawCell(eCoords5, red)
            drawCell(eCoords6, red)
            drawCell(eCoords7, red)
            drawCell(eCoords8, red)
            drawCell(eCoords9, red)

            currentPos = [newCell['x'], newCell['y']]

            for eachDeathCoord in deadZones:
                if eachDeathCoord == currentPos:
                    isAlive = 'no'
            
            pygame.display.update()
            fpsTime.tick(FPS)

            if (newCell['x'] < 0 or newCell['y'] < 0 or newCell['x'] > dispWidth/cellSize or newCell['y'] > dispHeight/cellSize):
                isAlive = 'no'

        msgSurface('You Died!', red)

def drawCell(coords, ccolor):
    for coord in coords:
        x = coord['x']*cellSize
        y = coord['y']*cellSize
        makeCell = pygame.Rect(x, y, cellSize, cellSize)
        pygame.draw.rect(setDisplay, ccolor, makeCell)

while True:
    global fpsTime, setDisplay

    fpsTime = pygame.time.Clock()
    setDisplay = pygame.display.set_mode((dispWidth,dispHeight))
    pygame.display.set_caption('Practice')
    runGame()


                    
