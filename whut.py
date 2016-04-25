import random
import pygame
import sys
from pygame.locals import *

pygame.init()

#Colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (51, 199, 255, 196)
red (255, 0, 0)
bg = black
#End Colors

FPS = 30
SCREEN = display.set_mode((800,600))
FONT = 'freesansbold.ttf'
IMG_NAMES = {"Block", "Background"}
IMAGES = {name: image.load("Sprite/{}.png".format(name)).convert_alpha()
          for name in IMG_NAMES}

UP = 'up'
DOWN = 'down'
RIGHT = 'right'
LEFT = 'left'

class Hero(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = IMAGES["Block"]
        self.rect = self.image.get_rect(topleft = (375, 540))
        self.speed = 5

    def update(self, keys, *args):
        if keys[K_LEFT] and self.rect.x > 10:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 740:
            self.rect.x += self.speed
        game.screen.blit(self.image, self.rect)

class Text(object):
    def __init__(self, textFont, size, message, color, xpos, ypos):
        self.font = font.Font(textFont, size)
        self.surface = self.font.render(message, True, color)
        self.rect = self.surface.get_rect(topleft=(xpos, ypos))

    def draw(self, surface):
        surface.blit(self.surface, self.rect)

class Game(object):
    def __init__(self):
        init()
        self.caption = display.set_caption("Base Game")
        self.screen = SCREEN
        self.background = IMAGES["Background"].convert()

    def check_input(self):
        self.keys = key.get_pressed()
        for e in event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()

    
                






        
